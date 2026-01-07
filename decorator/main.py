from decorator  import *


def main():
    plainText = PlainTextView("Hello, World!")

    print("Plain Text:", end="")
    print(plainText.display())
    print()

    boldText = BoldDecorator(plainText)
    print("Bold Text:", end="")
    print(boldText.display())
    print()


    italicBoldText = ItalicDecorator(boldText)
    print("Italic Bold Text:", end="")
    print(italicBoldText.display())
    print()


    underlineItalicBoldText = UnderlineDecorator(italicBoldText)
    print("Underline Italic Bold Text:", end="")
    print(underlineItalicBoldText.display())
    print()


if __name__ == "__main__":
    main()