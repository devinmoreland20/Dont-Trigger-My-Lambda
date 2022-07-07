#!/usr/bin/env python3.9
def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("text.txt")   #text.txt is another file that is created with some text

if __name__=="__main__":
    main()
