from colorama import Fore
import sys

path = sys.argv[1]
from pathlib import Path

parent_folder_path = Path(path)


def parse_folder(path):
    if not path.exists():
        print(Fore.RED + f"Error: La ruta '{path}' no existe." + Style.RESET_ALL)
        return

    for element in path.iterdir():
        if element.is_dir():
            print(Fore.RED + f"Parse folder: This is folder - {element.name}")
            parse_folder(element)
        if element.is_file():
            print(Fore.GREEN + f"Parse folder: This is file - {element.name}")


if len(sys.argv) < 2:
    print(Fore.YELLOW + "Uso: python homework_4.3.py /Users/ruslana/Desktop/my_repo1/Modul_4")
    sys.exit(1)

parent_folder_path = Path(sys.argv[1])
parse_folder(parent_folder_path)