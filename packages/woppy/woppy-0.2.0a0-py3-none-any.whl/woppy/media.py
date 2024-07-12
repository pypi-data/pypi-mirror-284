import requests
import os

class MediaManager:
    def __init__(self, site_url, auth):
        self.site_url = site_url
        self.auth = auth

        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }

    def upload_media(self, file_path):
        filename = os.path.basename(file_path)
        self.headers['Content-Disposition'] = f'attachment; filename={filename}'
        
        with open(file_path, 'rb') as file:
            response = requests.post(
                f"{self.site_url}/wp-json/wp/v2/media", 
                headers=self.headers, 
                auth=self.auth, 
                files={'file': file}
            )
        response.raise_for_status()
        return response.json()

    def get_media(self, media_id):
        response = requests.get(f"{self.site_url}/wp-json/wp/v2/media/{media_id}", auth=self.auth)
        response.raise_for_status()
        return response.json()
