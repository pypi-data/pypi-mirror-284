# Woppy

Woppy is a Python library to manage WordPress sites via the REST API.

## Installation

```bash
pip install woppy
```	

## Usage


```python
from woppy import Woppy

# Site URL, Username and Application Password
woppy = Woppy('https://your-wordpress-site.com', 'your-username', 'your-application-password')

# New Category
new_category = woppy.categories.create_category('New Category', 'This is a new category')

# New Tag
new_tag = woppy.tags.create_tag('New Tag', 'This is a new tag')

# New Post and assign the new category and tag
new_post = woppy.posts.create_post(
    title='My New Post',
    content='This is the content of my new post',
    status='publish',
    categories=[new_category['id']],  # Category ID
    tags=[new_tag['id']],              # Tag ID
)

# Get all plugins
plugins = woppy.plugins.get_plugins()

# Activate Akismet plugin
woppy.plugins.activate_plugin('akismet/akismet')

# Deactivate Akismet plugin
woppy.plugins.deactivate_plugin('akismet/akismet')
```

### Planned Updates

- [ ] Delete Tag
- [ ] Delete Media
- [ ] Delete Category
- [ ] Delete Post
- [ ] Upload Media
- [ ] Search Plugin From WordPress Repository