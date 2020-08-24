import os.path
from Flask_blog.config_loader import create_base_config


def check_config_exist(path):
    if os.path.isfile(path):
        print("Config file already exist")
        # exit(0)
    else:
        create_base_config(path)


def menu():
    default_path = ".env"
    print("Menu")
    print("1.Create Base Config")
    print("0.Exit")
    choice = int(input())
    if choice == 1:
        print("Use default path?")
        print("1.Yes 2.No")
        choice = int(input())
        if choice == 1:
            check_config_exist(default_path)
        if choice == 2:
            path = input("Type path")
            check_config_exist(path)

menu()
