# from utils.ANSI_color import *
# from utils.system_control_protocol import *
# from utils.option_manager import *
# from utils import macos_system_control as MacOS
# from utils import window_system_control as Windows


from .ANSI_color import *
from .system_control_protocol import *
from .option_manager import *
from .package_directory_manager import *
from . import macos_system_control as MacOS
from . import window_system_control as Windows
import platform
import os
import random
import hashlib


__version__ = None



def check_system():
    create_database_dir()
    if platform.system() == 'Darwin':
        con = connect_check_database(get_database_path())
        check_venv_connection(con, MacOS)
        con.close()
        return 'macos'
    elif platform.system() == 'win32' or platform.system() == 'Windows':
        con = connect_check_database(get_database_path())
        check_venv_connection(con, Windows)
        con.close()
        return 'win'
    
    
    
    
def check_ui_library():
    try:
        import inquirer
    except ModuleNotFoundError as e:
        print()
        print(f'{get_color_str('inquirer', 'RED')} module have not yet installed')
        print()
        print('Do you want to download it to your machine?')
        print()
        print('The library is Required for the program to run')
        userChoice = input('Your choice (Y/n): ')
        if userChoice == 'Y' or userChoice == 'y':
            os.system('pip install inquirer')
            print()
            print('Please rerun the program after installation')
            exit()        
        else:
            print()
            print_color('Cannot process further due to the lack of library', 'RED')
            exit()

def sha256_generator():
    return hashlib.sha256(str(random.randint(-100000000000, 10000000000000)).encode('utf-8')).hexdigest()


    

def menu_choice_process(user_answer, display_function):
    if check_system() == 'macos':
        os_system_control = MacOS
    elif check_system() == 'win':
        os_system_control = Windows


    if user_answer == '1':
        return option1(display_function[0], system_control = os_system_control)
    elif user_answer == '2':
        return option2(display_function[1], system_control = os_system_control)






def get_this_project_version():
    return __version__