from flyweight import *

def main():
    textEditor = TextEditorClient()

    str1= "Hello"
    for c in str1:
        textEditor.add_character(c, "12pt", "Arial", "Black", 0, 0)

    str2= "World"
    for c in str2:
        textEditor.add_character(c, "15pt", "Times New Roman", "Yellow", 10, 0)

    textEditor.render_document()



if __name__ == "__main__":
    main()