import requests
from requests.auth import HTTPBasicAuth

from .category import CategoryManager
from .post import PostManager
from .tag import TagManager
from .media import MediaManager
from .plugin import PluginManager

class Woppy:
    def __init__(self, site_url, username, app_password):
        self.site_url = site_url
        self.auth = HTTPBasicAuth(username, app_password)
        self.categories = CategoryManager(site_url, self.auth)
        self.posts = PostManager(site_url, self.auth)
        self.tags = TagManager(site_url, self.auth)
        self.media = MediaManager(site_url, self.auth)
        self.plugins = PluginManager(site_url, self.auth)
        
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }
      