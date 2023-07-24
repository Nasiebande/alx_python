#!/usr/bin/python3

if __name__ == "__main__":
    with open("variable_load_2.py", "r") as file:
        contents = file.read()

    variables = {}
    exec(contents, variables)

    if 'a' in variables:
        print(variables['a'])
