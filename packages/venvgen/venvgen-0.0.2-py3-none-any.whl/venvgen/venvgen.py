from .utils.ui_controler import *
from .utils.all_system_control import check_system
from .utils import all_system_control
import warnings
from .utils.package_directory_manager import *

__version__ = '0.0.2'


def main():
    all_system_control.__version__ = __version__
    warnings.filterwarnings("ignore")

    THIS_MACHINE = check_system()
    end_program = False

    while not end_program:
        introduction_screen()
        print_current_page('menu')
        end_program = menu_screen()





