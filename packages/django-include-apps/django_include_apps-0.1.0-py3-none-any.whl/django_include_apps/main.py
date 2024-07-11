import os
import re
import subprocess
import sys
import requests
from pathlib import Path
import inquirer
import typer
from importlib.metadata import PackageNotFoundError, version

app = typer.Typer()

def find_settings_file(start_dir: Path) -> Path:
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file == "settings.py":
                return Path(root) / file
    return None

def append_to_installed_apps(file_path: Path, new_app: str):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = re.compile(r"(INSTALLED_APPS\s*=\s*\[)(.*?)(\s*])", re.DOTALL)
    match = pattern.search(content)

    if not match:
        typer.secho("The specified INSTALLED_APPS list was not found in the file.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    start, apps_list, end = match.groups()
    
    if f"'{new_app}'" in apps_list:
        typer.secho(f"The app '{new_app}' already exists and will not be added to INSTALLED_APPS.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    new_apps_list = apps_list + f"\n\t'{new_app}',"
    new_content = content[:match.start(2)] + new_apps_list + content[match.end(2):]

    with open(file_path, 'w') as file:
        file.write(new_content)

    typer.secho(f"App '{new_app}' has been added to INSTALLED_APPS.", fg=typer.colors.GREEN)

def is_package_installed(package_name: str) -> bool:
    """
    Check if a package is installed in the current environment (virtual or system).

    Args:
        package_name (str): The name of the package to check.

    Returns:
        bool: True if the package is installed, False otherwise.
    """
    try:
        version(package_name)
        return True
    except PackageNotFoundError:
        return False

def install_package(package: str):
    subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)

def is_django_package(package):
    return "django" in package.lower()

def is_django_related(package: str) -> bool:
    """Check if a package is related to Django by querying PyPI."""
    url = f"https://pypi.org/pypi/{package}/json"
    try:
        if is_django_package(package):
            return True
        else:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            keywords = data.get("info", {}).get("keywords","")
            if keywords!="":
                if isinstance(keywords,str):
                    return True if "django" in keywords.lower() else False
                elif isinstance(keywords,list):
                    return any("django" in keyword.lower() for keyword in keywords)
            else:
                classifiers = data.get("info", {}).get("classifiers")
                return any("django" in classifier.lower() for classifier in classifiers)
    
    except requests.RequestException as e:
        typer.secho(f"Error checking package '{package}' on PyPI: {e}", fg=typer.colors.RED)
        return False

@app.command()
def add_app(new_app: str = typer.Argument(..., help="The new app to add to INSTALLED_APPS"),
            start_dir: Path = typer.Option(None, "--start-dir", "-d", help="The directory to search for settings.py. Defaults to current directory.")):
    """
    Add a new app to the INSTALLED_APPS list in settings.py if it's related to Django or already installed.
    """
    start_dir = start_dir or Path.cwd()
    settings_file_path = find_settings_file(start_dir)

    if settings_file_path:
        installed = is_package_installed(new_app)
        if not installed:
            install = [inquirer.Confirm("confirm", message=f"{new_app} is not installed. Do you want to install it?")]
            install_confirm = inquirer.prompt(install)
            if install_confirm["confirm"]:
                typer.secho(f"Installing package '{new_app}'...", fg=typer.colors.BLUE)
                install_package(new_app)
                typer.secho(f"Package '{new_app}' has been installed.", fg=typer.colors.GREEN)
            else:
                typer.secho(f"Skipping installation of '{new_app}'.", fg=typer.colors.YELLOW)
                raise typer.Exit(code=1)
        else:
                typer.secho(f"Package '{new_app}' has already installed.Skipping installation", fg=typer.colors.BRIGHT_YELLOW)
            
        if is_django_related(new_app):
            typer.secho(f"Searching for settings.py in {start_dir}", fg=typer.colors.BLUE)
            confirmation = [
                    inquirer.List(
                        "choice",
                        message="Do you want to use the same username or a different one?",
                        choices=['Use same', 'Use different'],
                    ),
            ]
            answers = inquirer.prompt(confirmation)
            if answers["choice"]=="Use different":
                packagename_question = [
                        inquirer.Text('package_name', message="Enter your package name as mentioned in the souce documentation")
                ]
                second_answers = inquirer.prompt(packagename_question)
                if second_answers["package_name"]!="":
                    append_to_installed_apps(settings_file_path, second_answers["package_name"])
            else:
                typer.secho(f"Using '{new_app}' package name as the App name to be added in INSTALLED_APPS.", fg=typer.colors.BRIGHT_CYAN)
                append_to_installed_apps(settings_file_path, new_app)
        else:
            typer.secho(f"The package '{new_app}' is not related to Django and will not be added to INSTALLED_APPS.", fg=typer.colors.RED)
    else:
        typer.secho("settings.py not found in the specified directory or its subdirectories.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
