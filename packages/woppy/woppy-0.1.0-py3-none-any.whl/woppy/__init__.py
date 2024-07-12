import requests

class Woppy:
    def __init__(self, site_url, username, password):
        self.site_url = site_url
        self.username = username
        self.password = password
        self.token = self.get_token()

    def get_token(self):
        response = requests.post(f"{self.site_url}/wp-json/jwt-auth/v1/token", data={
            'username': self.username,
            'password': self.password
        })
        response.raise_for_status()
        return response.json()['token']

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def create_post(self, title, content, status='draft'):
        data = {
            'title': title,
            'content': content,
            'status': status
        }
        response = requests.post(f"{self.site_url}/wp-json/wp/v2/posts", headers=self.get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    def update_post(self, post_id, title=None, content=None):
        data = {}
        if title:
            data['title'] = title
        if content:
            data['content'] = content
        response = requests.post(f"{self.site_url}/wp-json/wp/v2/posts/{post_id}", headers=self.get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    def get_categories(self):
        response = requests.get(f"{self.site_url}/wp-json/wp/v2/categories", headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def create_category(self, name, description=None):
        data = {
            'name': name,
        }
        if description:
            data['description'] = description
        response = requests.post(f"{self.site_url}/wp-json/wp/v2/categories", headers=self.get_headers(), json=data)
        response.raise_for_status()
        return response.json()
