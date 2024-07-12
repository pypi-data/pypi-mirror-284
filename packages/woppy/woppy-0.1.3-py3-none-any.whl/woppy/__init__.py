import requests
from requests.auth import HTTPBasicAuth

class Woppy:
    def __init__(self, site_url, username, app_password):
        self.site_url = site_url
        self.auth = HTTPBasicAuth(username, app_password)

    def create_post(self, title, content, status='draft'):
        data = {
            'title': title,
            'content': content,
            'status': status
        }
        response = requests.post(f"{self.site_url}/wp-json/wp/v2/posts", auth=self.auth, json=data)
        response.raise_for_status()
        return response.json()

    def update_post(self, post_id, title=None, content=None):
        data = {}
        if title:
            data['title'] = title
        if content:
            data['content'] = content
        response = requests.post(f"{self.site_url}/wp-json/wp/v2/posts/{post_id}", auth=self.auth, json=data)
        response.raise_for_status()
        return response.json()

    def get_categories(self):
        response = requests.get(f"{self.site_url}/wp-json/wp/v2/categories", auth=self.auth)
        response.raise_for_status()
        return response.json()

    def create_category(self, name, description=None):
        data = {
            'name': name,
        }
        if description:
            data['description'] = description
        response = requests.post(f"{self.site_url}/wp-json/wp/v2/categories", auth=self.auth, json=data)
        response.raise_for_status()
        return response.json()
