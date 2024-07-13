import requests

class PostManager:
    def __init__(self, site_url, auth):
        self.site_url = site_url
        self.auth = auth
        
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }
        
    def get_posts(self):
        response = requests.get(f"{self.site_url}/wp-json/wp/v2/posts", auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()
        
    def create_post(self, title, content, status='draft', categories=None, tags=None, featured_media=None):
        data = {
            'title': title,
            'content': content,
            'status': status
        }
        if categories:
            data['categories'] = categories
        if tags:
            data['tags'] = tags
        if featured_media:
            data['featured_media'] = featured_media
        
        response = requests.post(f"{self.site_url}/wp-json/wp/v2/posts", auth=self.auth, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_post(self, post_id, title=None, content=None, categories=None, tags=None, featured_media=None):
        data = {}
        if title:
            data['title'] = title
        if content:
            data['content'] = content
        if categories:
            data['categories'] = categories
        if tags:
            data['tags'] = tags
        if featured_media:
            data['featured_media'] = featured_media

        response = requests.post(f"{self.site_url}/wp-json/wp/v2/posts/{post_id}", auth=self.auth, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
