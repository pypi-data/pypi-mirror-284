import base64
import requests
import os
import mimetypes

class MediaManager:
    def __init__(self, site_url, auth):
        self.site_url = site_url
        self.auth = auth

        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }
        
    # UPLOAD MEDIA ADD LATER
            
    def get_media(self):
        response = requests.get(f"{self.site_url}/wp-json/wp/v2/media", auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()
