import requests

class ApiClient:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def get(self, method, params=None):
        headers = {
            "Authorization": self.api_key,
            "Accept": "application/json"
        }
        
        if params is not None:
            response = requests.get(f"{self.api_url}/{method}/", headers=headers, params=params)
        else:
            response = requests.get(f"{self.api_url}/{method}/", headers=headers)
        
        return response

    def post(self, method, data = []):
        response = requests.post(f"{self.api_url}/{method}/", headers={
            "Authorization": self.api_key,
            "Accept": "application/json"
        }, json=data)
        return response
    
    def patch(self, method, data = []):
        response = requests.patch(f"{self.api_url}/{method}/", headers={
            "Authorization": self.api_key,
            "Accept": "application/json"
        }, json=data)
        return response

    def delete(self, method):
        response = requests.delete(f"{self.api_url}/{method}/", headers={
            "Authorization": self.api_key,
            "Accept": "application/json"
        })
        return response