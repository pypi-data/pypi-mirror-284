# Woppy

Woppy is a Python library to manage WordPress sites via the REST API.

## Installation

```bash
pip install woppy

## Usage

```python
from woppy import Woppy

woppy = Woppy('https://your-wordpress-site.com', 'your-username', 'your-password')

# Create a new post
new_post = woppy.create_post('My New Post', 'This is the content of my new post')

# Update an existing post
updated_post = woppy.update_post(new_post['id'], title='Updated Title')

# Get categories
categories = woppy.get_categories()

# Create a new category
new_category = woppy.create_category('New Category', 'This is a new category')
