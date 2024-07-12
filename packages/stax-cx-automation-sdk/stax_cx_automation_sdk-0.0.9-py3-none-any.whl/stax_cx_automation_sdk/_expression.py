# See LICENSE.md file in project root directory

import re
import json
from js2py import eval_js
from db import db
from bson import ObjectId
from datetime import datetime

# Custom function to convert datetime objects to the specific format
def convert_datetimes(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, datetime):
                obj[key] = f'new Date("{value.isoformat()}")'
            elif isinstance(value, (dict, list)):
                obj[key] = convert_datetimes(value)
    elif isinstance(obj, list):
        obj = [convert_datetimes(item) for item in obj]
    return obj

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
            function replacePlaceholders(fieldValue, context) {

                // Function to convert 'new Date("...")' strings to Date objects
                function convertDateStringsToObjects(obj) {
                    if (typeof obj === 'string' && obj.indexOf('new Date') === 0) {
                        return eval(obj); // Convert the string to a Date object
                    } else if (typeof obj === 'object' && obj !== null) {
                        for (var key in obj) {
                            if (obj.hasOwnProperty(key)) {
                                obj[key] = convertDateStringsToObjects(obj[key]);
                            }
                        }
                    }
                    return obj;
                }

                // Convert the context to ensure all date strings are converted to Date objects
                context = convertDateStringsToObjects(context);

                // Convert the context to ensure all date strings are converted to Date objects
                context = convertDateStringsToObjects(context);
                return fieldValue.replace(/@@(.+?)@@/g, function(match, p1) {
                    try {
                        var contextKeys = Object.keys(context);
                        var contextValues = contextKeys.map(function(key) { return context[key]; });
                        var func = new Function(contextKeys, 'return ' + p1);
                        var result = func.apply(null, contextValues);
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
If the expression is an object, the value of the 'email' or 'name' key is returned based on the prop flag
If the expression is not an object, the value is returned as is
'''
def populate(context: dict, fieldType: str, fieldValue: str, prop: str=None):

    try:
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
                    if prop:
                        key = key + f"['{prop}']"
                    fieldValue = fieldValue.replace(f"@@{match}@@", replace_placeholders(f"@@{key}@@", context_js, prop))
                
            except json.JSONDecodeError:
                replaced_match = replace_placeholders(f"@@{match}@@", context_js)
                fieldValue = fieldValue.replace(f"@@{match}@@", replaced_match)

        #Switch case for fieldType
        if prop == '_id':
            fieldValue = ObjectId(fieldValue)
        return fieldValue

    except Exception as e:
        print(f"Failed to populate field with error: {str(e)}")

'''
Function to fill context based on teamId, taskId
The function unpacks values and populates the context object with the required values
'''
def getContext(teamId: str, taskId: str=None, projectId: str=None, clientId: str=None, planId: str=None) -> (dict):
    context = {}
    
    if taskId:
        context["task"] = db.tasks.find_one({"team": ObjectId(teamId), "_id": ObjectId(taskId), "deleted_at": None})
        if not context["task"]:
            raise Exception("Task not found")
    
    # Attempt to find projectId from task if not provided
    if not projectId and context.get("task"):
        projectId = context["task"].get("project")
        
    if projectId:
        context["project"] = db.projects.find_one({"team": ObjectId(teamId), "_id": ObjectId(projectId), "deleted_at": None})
        if not context["project"]:
            raise Exception("Project not found")
    
    # Attempt to find planId from project and then task if not provided
    if not planId and context.get("project"):
        planId = context["project"].get("plan")
        
    elif not planId and context.get("task"):
        planId = context["task"].get("plan")
        
    if planId:
        context["plan"] = db.plans.find_one({"team": ObjectId(teamId), "_id": ObjectId(planId), "deleted_at": None})
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
        context["client"] = db.clients.find_one({"team": ObjectId(teamId), "_id": ObjectId(clientId), "deleted_at": None})
        if not context["client"]:
            raise Exception("Client not found")
    
    #Unpacking fields to add to the context
    fields = db.fields.find({"team": ObjectId(teamId)})
    fields_dict = {}
    for field in fields:
        if field["on_type"] not in fields_dict:
            fields_dict[field["on_type"]] = []
        fields_dict[field["on_type"]].append({"key": field["key"], "type": field["type"]})
    
    # There are some values in the context that are not directly accessible and need to be extracted
    context["project"]["lead"] = db.users.find_one({"team": ObjectId(teamId),"_id": ObjectId(context["project"]["lead"])})

    context["task"]["assignee"] = db.users.find_one({"team": ObjectId(teamId),"_id": ObjectId(context["task"]["assignee"])})

    assignee_obj = {}
    for assignee in context["client"]["assignees"]:
        assignee_obj[assignee["role"]] = db.users.find_one({"team": ObjectId(teamId), "_id": ObjectId(assignee["user"])})
    context["client"]["assignees"] = assignee_obj
    
    for contact_key in ["contacts", "external"]:
        contact_key_obj = {}
        if contact_key not in context["client"]:
            continue
        for each_contact in context["client"][contact_key]:
            contact = db.contacts.find_one({"team": ObjectId(teamId), "_id": ObjectId(each_contact["contact"])})
            contact_key_obj[each_contact["role"]] = contact
            contact_key_obj[each_contact["role"]]["email"] = ', '.join(contact["email"])
        context["client"][contact_key] = contact_key_obj

    # Task, Project, Client and Plan have a fields attribute that is a list of dictionaries
    # We need to convert this list of dictionaries to a dictionary of key-value pairs
    for key in ["project", "client", "plan"]:
        if key in context and context[key] and "fields" in context[key] and context[key]["fields"]:
            context[key]["data"] = {}
            context[key]["data_val"] = {}
            for field in context[key]["fields"]:
                for f in fields_dict[key]:
                    if field["key"] == f["key"]:
                        if f["type"] == "User":
                            field_obj = db.users.find_one({"team": ObjectId(teamId), "_id": ObjectId(field["value"])})
                        elif f["type"] == "Date":
                            field_obj = datetime.strptime(field["value"], "%Y-%m-%dT%H:%M:%S.%fZ")
                        elif f["type"] == "Number":
                            field_obj = float(field["value"])
                        elif f["type"] == "File":
                            field_obj = db.files.find_one({"team": ObjectId(teamId), "_id": ObjectId(field["value"])})
                        else:
                            field_obj = field["value"]
                        context[key]["data"][field["key"]] = field_obj
                        context[key]["data_val"][field["key"]] = field_obj
                        break
    
    # We need to convert all datetime objects to the specific format
    context = convert_datetimes(context)
    # We need to get rid of all ObjectId references in the context and all the nested references too
    context = json.loads(json.dumps(context, default=str))
    return context
