from .utils.ui_controler import *
from .utils.all_system_control import check_system
import warnings
from .utils.package_directory_manager import *

__version__ = '0.0.1'

def main():
    warnings.filterwarnings("ignore")
    create_database_dir()

    THIS_MACHINE = check_system()
    end_program = False

    while not end_program:
        introduction_screen()
        end_program = menu_screen()





