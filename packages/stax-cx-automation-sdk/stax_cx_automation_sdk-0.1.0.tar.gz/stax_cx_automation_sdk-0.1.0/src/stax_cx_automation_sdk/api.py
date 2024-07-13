from os import getenv
from retry_requests import retry, RSession

api = None

API_URL = getenv('STAX_CX_API_URL', 'https://api.cx.stax.ai')

class API:
    def __init__(self, team, aid, key):
        self.headers = {
            "x-internal-key": key,
            "x-automation-id": aid,
            "x-team-id": team
        }
        self.sess = retry(RSession(timeout=30), retries=3)
        
    def get(self, url):
        return self.sess.get(f"{API_URL}{url}", headers=self.headers)
    
    def post(self, url, data={}):
        return self.sess.post(f"{API_URL}{url}", headers=self.headers, json=data)
    
    def patch(self, url, data={}):
        return self.sess.patch(f"{API_URL}{url}", headers=self.headers, json=data)
    
    def delete(self, url):
        return self.sess.delete(f"{API_URL}{url}", headers=self.headers)
        
def init_api(team, aid, key):
    global api
    api = API(team, aid, key)