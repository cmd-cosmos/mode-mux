#pylint: skip-file
#type: ignore

import argparse
from modes import modes_map, name_func_map

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--fun",   action="store_true", help="run fun mode")
    parser.add_argument("-s", "--study", action="store_true", help="run study mode")
    parser.add_argument("-w", "--work",  action="store_true", help="run work mode")
    
    args = parser.parse_args()
    
    for name, func in name_func_map.items():
        if getattr(args, name):
            func()
            return
    
    print("Choose Mode: ")
    for num, name in modes_map.items():
        print(f"{num} : {name.capitalize()}")
    
    choice = input("Enter Mode ID: ").strip()
    try:
        choice = int(choice)
        mode = modes_map[choice]
        name_func_map[mode]()
    except (ValueError, KeyError):
        print("Invalid Choice")

if __name__ == "__main__":
    main()