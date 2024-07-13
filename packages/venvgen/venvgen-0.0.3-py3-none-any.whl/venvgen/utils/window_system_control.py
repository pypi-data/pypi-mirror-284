import os
# from commands.window_command import *
from ..commands.window_command import *

def clear_screen():
    return_status = os.system(clear_screen_command)

def create_venv(project_directory, project_name):
    os.system(f'cd "{project_directory}"\n' + CREATE_VENV + project_name)

def install_libraries(project_directory, venv, libraries):
    os.system(f'cd "{project_directory}"\n' + venv + '\\Scripts\\activate.bat\npip install ' + libraries)
    
def install_libraries_with_requirement(project_directory, venv, requirement_file):
    os.system(f'cd "{project_directory}"\n' + venv + '\\Scripts\\activate.bat\npip install -r ' + f'"{requirement_file}"')

def activate_venv(project_directory, venv):
    return os.system(f'cd "{project_directory}"\n' + venv + '\\Scripts\\activate.bat\n')