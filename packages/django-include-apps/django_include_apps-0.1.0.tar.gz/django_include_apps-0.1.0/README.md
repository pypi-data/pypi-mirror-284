# django-include-apps
**django-include-apps** is a CLI tool to help you manage Django apps in the INSTALLED_APPS list in your Django project's settings.py file. This tool simplifies the process of adding new apps by ensuring they are properly installed and integrated into your Django project.

# Features
- Automatically search for settings.py in the current or specified directory.
- Check if the package is installed; if not, prompt the user to install it.
- Verify if the package is related to Django before adding it to **INSTALLED_APPS**.
- Only Add the new app to the INSTALLED_APPS list if it's not already present.

# Installation.
You can install django-include-apps via pip:
```python
pip install django-include-apps
```

# Usage
## Basic Command
To add a new app to INSTALLED_APPS, use the following command:

```
django-include-apps add_app <new_app>
```

Replace **<new_app>** with the name of the Django app you want to add.

# Options:
Use **--start-dir** or **-d** to specify the directory to search for settings.py. Defaults to the current directory if not provided.


# Examples:
## Example 1: settings.py in the Current Directory
Suppose your Django project's settings.py file is in the current working directory.
Navigate to your project directory:
```sh
cd /path/to/your/django/project
```
Run the CLI command to add a new app:

```python
django-include-apps add_app my_new_app
 ```

## Example 2: settings.py in a Different Directory
Suppose your Django project's settings.py file is in a different directory, such as /path/to/your/django/project/config.
Navigate to your desired starting directory:
```sh
cd /path/to/your/django/project
```
Run the CLI command with the --start-dir or -d option:
```python
django-include-apps add_app my_new_app --start-dir ./config
```
