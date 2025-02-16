from colorama import Fore, Style
import sys
from pathlib import Path


def parse_folder(path):
    if not path.exists():
        print(Fore.RED + f"Error: La ruta '{path}' no existe." + Style.RESET_ALL)
        return
    if not path.is_dir():
        print(Fore.RED + f"Error: La ruta '{path}' no es un directorio." + Style.RESET_ALL)
        return
    for element in path.iterdir():
        if element.is_dir():
            print(Fore.RED + f"Parse folder: This is folder - {element.name}" + Style.RESET_ALL)
            parse_folder(element)
        if element.is_file():
            print(Fore.GREEN + f"Parse folder: This is file - {element.name}" + Style.RESET_ALL)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Uso: python homework_4_3.py /Users/ruslana/Desktop/homework_module_4")
        sys.exit(1)

parent_folder_path = Path(sys.argv[1])
parse_folder(parent_folder_path)