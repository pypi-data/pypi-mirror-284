import requests

class TagManager:
    def __init__(self, site_url, auth):
        self.site_url = site_url
        self.auth = auth

             
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }

    def get_tags(self):
        response = requests.get(f"{self.site_url}/wp-json/wp/v2/tags", auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_tag(self, name, description=None):
        data = {
            'name': name,
        }
        if description:
            data['description'] = description
        response = requests.post(f"{self.site_url}/wp-json/wp/v2/tags", auth=self.auth, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
