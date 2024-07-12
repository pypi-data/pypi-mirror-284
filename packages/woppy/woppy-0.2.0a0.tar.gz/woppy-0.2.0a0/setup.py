from setuptools import setup, find_packages

setup(
    name='woppy',
    version='0.2.0-alpha',
    description='A Python library to manage WordPress sites via the REST API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Techard',
    author_email='info@techard.net',
    url='https://github.com/techard/woppy',
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
)
