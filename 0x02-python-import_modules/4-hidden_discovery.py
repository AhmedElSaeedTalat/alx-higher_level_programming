#!/usr/bin/python3
hidden = __import__("hidden_4")
if __name__ == "__main__":
    for hide in dir(hidden):
        if hide[0] == '_':
            continue
        print(hide)
