from setuptools import setup, find_packages

setup(
    name='woppy',
    version='1.0.0',
    description='A Python library to manage WordPress sites via the REST API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Techard',
    author_email='info@techard.net',
    maintainer='Fatih Zor',
    maintainer_email='me@fatihzor.dev',
    url='https://techard.net',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords=[
        'wordpress',
        'rest api',
        'api',
        'cms',
    ],
    platforms=['any']
)
