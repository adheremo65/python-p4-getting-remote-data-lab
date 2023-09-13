import requests
import json

class GetRequester:
    import json

    def __init__(self, url):
        self.url = url
        
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        json_str = response_body.decode('utf-8')
        data = json.loads(json_str)
        return data
        