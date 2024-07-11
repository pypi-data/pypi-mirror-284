from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()


setup(
    name = 'venvgen',
    version = '0.0.0',
    packages = find_packages(),
    install_requires = [
        'pandas',
        'inquirer'
    ],
    entry_points = {
        'console_scripts': [
            'venvgen = venvgen:main',
        ]
    },
    # include_package_data = True,
    # package_data = {
    #     'venvgen': ['database/*'],
    # },
    long_description = description,
    long_description_content_type = 'text/markdown',
)