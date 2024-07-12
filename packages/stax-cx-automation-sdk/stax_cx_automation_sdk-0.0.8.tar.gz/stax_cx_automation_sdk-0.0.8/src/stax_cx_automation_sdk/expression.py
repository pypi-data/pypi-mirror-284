# See LICENSE.md file in project root directory

import re
import json
from js2py import eval_js
from db import db
from bson import ObjectId

# JavaScript code for template replacement
'''
This code is used to replace placeholders in a template with values from a context object.
The placeholders are denoted by @@...@@ and the values are extracted from the context object.
The context object is a JSON object that contains key-value pairs.
The placeholders can contain expressions that are evaluated using the Function constructor.
The expressions can reference values in the context object using keys.
The result of the expression is returned as the replacement value for the placeholder.
If the expression is an object, the value of the 'email' or 'name' key is returned based on the use_email flag.
If the expression is not an object, the value is returned as is.
'''
JS_CODE = """
            function replacePlaceholders(fieldValue, context, use_email) {
                return fieldValue.replace(/@@(.+?)@@/g, function(match, p1) {
                    try {
                        var contextKeys = Object.keys(context);
                        var contextValues = contextKeys.map(function(key) { return context[key]; });
                        var func = new Function(contextKeys, 'return ' + p1);
                        var result = func.apply(null, contextValues);
                        if (typeof result === 'object' && result !== null) {
                            return result[use_email ? 'email' : 'name'];
                        }
                        return result;
                    } catch (e) {
                        return '';
                    }
                });
            }
        """


'''
Function to populate a field value with values from a context object
The function replaces placeholders in the field value with values from the context object
The placeholders are denoted by @@...@@ and the values are extracted from the context object
The function evaluates expressions in the placeholders using the Function constructor
The expressions can reference values in the context object using keys
The result of the expression is returned as the replacement value for the placeholder
If the expression is an object, the value of the 'email' or 'name' key is returned based on the userProp flag
If the expression is not an object, the value is returned as is
'''
def populate(context: dict, fieldType: str, fieldValue: str, userProp: str):

    if len(fieldValue) == 0:
        return ""
    
    if fieldValue[0] == "=":
        fieldValue = fieldValue[1:]

    # Convert context dictionary to JS object notation
    context_js = eval_js(f"({json.dumps(context)})")
    replace_placeholders = eval_js(JS_CODE + "\nreplacePlaceholders")

    # We need to find regex patterns that match @@...@@ and replace it with the context
    for match in re.findall(r'@@(.+?)@@', fieldValue):
        try:
            value = json.loads(match)
            if "key" in value:
                key = value["key"]
                fieldValue = fieldValue.replace(f"@@{match}@@", replace_placeholders(f"@@{key}@@", context_js, userProp == "email"))
            
        except json.JSONDecodeError:
            replaced_match = replace_placeholders(f"@@{match}@@", context_js, userProp == "email")
            fieldValue = fieldValue.replace(f"@@{match}@@", replaced_match)
    
    return fieldValue

'''
Function to fill context based on teamId, taskId
The function unpacks values and populates the context object with the required values
'''
def getContext(teamId: str, taskId: str=None, projectId: str=None, clientId: str=None, planId: str=None) -> dict:
    context = {}
    
    if taskId:
        context["task"] = db['tasks'].find_one({"team": ObjectId(teamId), "_id": ObjectId(taskId), "deleted_at": None})
        if not context["task"]:
            raise Exception("Task not found")
    
    # Attempt to find projectId from task if not provided
    if not projectId and context.get("task"):
        projectId = context["task"].get("project")
        
    if projectId:
        context["project"] = db['projects'].find_one({"team": ObjectId(teamId), "_id": ObjectId(projectId), "deleted_at": None})
        if not context["project"]:
            raise Exception("Project not found")
    
    # Attempt to find planId from project and then task if not provided
    if not planId and context.get("project"):
        planId = context["project"].get("plan")
        
    elif not planId and context.get("task"):
        planId = context["task"].get("plan")
        
    if planId:
        context["plan"] = db['plans'].find_one({"team": ObjectId(teamId), "_id": ObjectId(planId), "deleted_at": None})
        if not context["plan"]:
            raise Exception("Plan not found")  
    
    # Attempt to find clientId from plan, project, and then task if not provided
    if not clientId and context.get("plan"):
        clientId = context["plan"].get("client")
        
    elif not clientId and context.get("project"):
        clientId = context["project"].get("client")
        
    elif not clientId and context.get("task"):
        clientId = context["task"].get("client")
        
    if clientId:
        context["client"] = db['clients'].find_one({"team": ObjectId(teamId), "_id": ObjectId(clientId), "deleted_at": None})
        if not context["client"]:
            raise Exception("Client not found")
    
    #Unpacking fields to add to the context
    fields = db['fields'].find({"team": ObjectId(teamId)})
    fields_dict = {}
    for field in fields:
        if not field.get("on_type") or not field.get("key"):
            continue
        
        if field["on_type"] not in fields_dict:
            fields_dict[field["on_type"]] = []
        
        fields_dict[field["on_type"]].append({
            "key": field["key"],
            "type": field.get("type")
        })

    # We need to get rid of all ObjectId references in the context and all the nested references too
    context = json.loads(json.dumps(context, default=str))
    
    # There are some values in the context that are not directly accessible and need to be extracted
    if context.get("project"):
        project_lead = db['users'].find_one({"team": ObjectId(teamId),"_id": ObjectId(context["project"].get("lead"))})
        if project_lead:
            context["project"]["lead"] = {"name": project_lead["name"], "email": project_lead["email"]}

    if context.get("task"):
        task_assignee = db['users'].find_one({"team": ObjectId(teamId),"_id": ObjectId(context["task"].get("assignee"))})
        if task_assignee:
            context["task"]["assignee"] = {"name": task_assignee["name"], "email": task_assignee["email"]}

    if context.get("client"):
        if context.get("client").get("assignees"):
            assignee_obj = {}
            for assignee in context["client"]["assignees"]:
                if not assignee.get("role"):
                    continue
                
                assignee_ = db['users'].find_one({"team": ObjectId(teamId), "_id": ObjectId(assignee.get("user"))})
                if not assignee_:
                    continue
                
                assignee_obj[assignee["role"]] = {"name": assignee_.get("name"), "email": assignee_.get("email")}
            
            context["client"]["assignees"] = assignee_obj
        
        for contact_key in ["contacts", "external"]:
            contact_key_obj = {}
            if contact_key not in context["client"]:
                continue
            
            for each_contact in context["client"][contact_key]:
                if not each_contact.get("role"):
                    continue
                
                contact = db.contacts.find_one({"team": ObjectId(teamId), "_id": ObjectId(each_contact.get("contact"))})
                if not contact:
                    continue
                
                contact_key_obj[each_contact["role"]]={
                    "name": contact.get("name"),
                    "email": ', '.join(contact.get("email", default=[]))
                }
            
            context["client"][contact_key] = contact_key_obj

    # Task, Project, Client and Plan have a fields attribute that is a list of dictionaries
    # We need to convert this list of dictionaries to a dictionary of key-value pairs
    for ref in ["project", "client", "plan"]:
        if not context.get(ref) or not context[ref].get("fields"):
            continue
            
        context[ref]["data"] = {}
        context[ref]["data_val"] = {}
        
        for field in context[ref].get("fields", []):
            for f in fields_dict[ref]:
                key = f.get("key")
                if not key or not field.get("key") or not field.get("value"):
                    continue
                
                if field["key"] == key:
                    if f.get("type") == "User":
                        user_field = db['users'].find_one({"team": ObjectId(teamId), "_id": ObjectId(field.get("value"))})
                        field["value"] = {"name": user_field.get("name"), "email": user_field.get("email")}
                        
                    context[key]["data"][field["key"]] = field["value"]
                    break
    
    return context
