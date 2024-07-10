from setuptools import setup, find_packages

setup(
    author = 'Kirtan Patel',
    name = 'node_setup_tool',
    version = '1.0.0',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'node-setup=node_setup_tool.main:createDir'
        ]
    },
    install_requires = [],
)