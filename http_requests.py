import requests

class JSONPlaceholder:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_request(self):
        response = requests.get(self.base_url)
        data = {
            "status_code": response.status_code,
            "headers": response.headers,
            # First 500 characters of the content
            "content": response.content[:500]
        }
        return data
    
    def post_request(self, data):
        response = requests.post(self.base_url, data=data)
        data = {
            "status_code": response.status_code,
            "headers": response.headers,
            # First 500 characters of the content
            "content": response.content[:500]
        }
        return data
    
    def update_user(self, userId, title, body):
        data = {
            "title": title,
            "body": body
        }
        response = requests.put(f'{self.base_url}/{userId}', data)

        data = {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content[:500]
        }
        return data

    def delete_user(self, userId):
        response = requests.delete(f'{self.base_url}/{userId}')
        data = {
            "status_code": response.status_code,
        }
        return data