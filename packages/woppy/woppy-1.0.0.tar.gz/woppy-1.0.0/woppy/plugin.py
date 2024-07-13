import requests

class PluginManager:
    def __init__(self, site_url, auth):
        self.site_url = site_url
        self.auth = auth
        
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }
        
    def get_plugins(self):
        response = requests.get(f"{self.site_url}/wp-json/wp/v2/plugins", auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def install_plugin(self, plugin_slug):
        response = requests.post(
            f"{self.site_url}/wp-json/wp/v2/plugins",
            json={"slug": plugin_slug},
            auth=self.auth,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def delete_plugin(self, plugin_slug):
        response = requests.delete(
            f"{self.site_url}/wp-json/wp/v2/plugins/{plugin_slug}",
            auth=self.auth,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def activate_plugin(self, plugin_slug):
        return self._toggle_plugin(plugin_slug, "active")

    def deactivate_plugin(self, plugin_slug):
        return self._toggle_plugin(plugin_slug, "inactive")

    def _toggle_plugin(self, plugin_slug, action):
        response = requests.post(
            f"{self.site_url}/wp-json/wp/v2/plugins/{plugin_slug}",
            json={"status": action},
            auth=self.auth,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
