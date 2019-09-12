# Transliterates input from Latin script to Cyrillic script
# Arguments: -c copies the result to the clipboard; any other argument is
# treated as input

import pyperclip
import sys

user_mode = True
copy_to_clipboard = False
inp = ""
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if arg == "-c" or arg == "-C":
            copy_to_clipboard = True
        else:
            if inp == "":
                inp = arg
                user_mode = False
            else:
                raise ValueError("Argument \"" + arg + "\" error, input already defined as \"" + inp + "\"")
while True:
    if user_mode:
        inp = input("In: ")
        if inp == "exit" or inp == "quit":
            break
    transliterated = ""
    i = 0
    while i < len(inp):
        ch = inp[i]
        if ch == 'a':
            transliterated += 'а'
        elif ch == 'A':
            transliterated += 'А'
        elif ch == 'b':
            transliterated += 'б'
        elif ch == 'B':
            transliterated += 'Б'
        elif ch == 'c':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == 'h':
                    transliterated += 'ч'
                else:
                    transliterated += 'ц'
                    i -= 1
            else:
                transliterated += 'ц'
        elif ch == 'C':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == 'h' or ch == 'H':
                    transliterated += 'Ч'
                else:
                    transliterated += 'Ц'
                    i -= 1
            else:
                transliterated += 'Ц'
        elif ch == 'd':
            transliterated += 'д'
        elif ch == 'D':
            transliterated += 'Д'
        elif ch == 'e':
            transliterated += 'э'
        elif ch == 'E':
            transliterated += 'Э'
        elif ch == 'f':
            transliterated += 'ф'
        elif ch == 'F':
            transliterated += 'Ф'
        elif ch == 'g':
            transliterated += 'г'
        elif ch == 'G':
            transliterated += 'Г'
        elif ch == 'h':
            transliterated += 'х'
        elif ch == 'H':
            transliterated += 'Х'
        elif ch == 'i':
            transliterated += 'и'
        elif ch == 'I':
            transliterated += 'И'
        elif ch == 'j':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == 'o':
                    transliterated += 'ё'
                elif ch == 'e':
                    transliterated += 'е'
                elif ch == 'u':
                    transliterated += 'ю'
                elif ch == 'a':
                    transliterated += 'я'
                else:
                    transliterated += 'й'
                    i -= 1
            else:
                transliterated += 'й'
        elif ch == 'J':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == 'o' or ch == 'O':
                    transliterated += 'Ё'
                elif ch == 'e' or ch == 'E':
                    transliterated += 'Е'
                elif ch == 'u' or ch == 'U':
                    transliterated += 'Ю'
                elif ch == 'a' or ch == 'A':
                    transliterated += 'Я'
                else:
                    transliterated += 'Й'
                    i -= 1
            else:
                transliterated += 'Й'
        elif ch == 'k':
            transliterated += 'к'
        elif ch == 'K':
            transliterated += 'К'
        elif ch == 'l':
            transliterated += 'л'
        elif ch == 'L':
            transliterated += 'Л'
        elif ch == 'm':
            transliterated += 'м'
        elif ch == 'M':
            transliterated += 'М'
        elif ch == 'n':
            transliterated += 'н'
        elif ch == 'N':
            transliterated += 'Н'
        elif ch == 'o':
            transliterated += 'о'
        elif ch == 'O':
            transliterated += 'О'
        elif ch == 'p':
            transliterated += 'п'
        elif ch == 'P':
            transliterated += 'П'
        elif ch == 'q':
            transliterated += 'я'
        elif ch == 'Q':
            transliterated += 'Я'
        elif ch == 'r':
            transliterated += 'р'
        elif ch == 'R':
            transliterated += 'Р'
        elif ch == 's':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == 'h':
                    transliterated += 'ш'
                else:
                    transliterated += 'с'
                    i -= 1
            else:
                transliterated += 'с'
        elif ch == 'S':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == 'h' or ch == 'H':
                    transliterated += 'Ш'
                else:
                    transliterated += 'С'
                    i -= 1
            else:
                transliterated += 'С'
        elif ch == 't':
            transliterated += 'т'
        elif ch == 'T':
            transliterated += 'Т'
        elif ch == 'u':
            transliterated += 'у'
        elif ch == 'U':
            transliterated += 'У'
        elif ch == 'v':
            transliterated += 'в'
        elif ch == 'V':
            transliterated += 'В'
        elif ch == 'w':
            transliterated += 'щ'
        elif ch == 'W':
            transliterated += 'Щ'
        elif ch == 'x':
            transliterated += 'х'
        elif ch == 'X':
            transliterated += 'Х'
        elif ch == 'y':
            transliterated += 'ы'
        elif ch == 'Y':
            transliterated += 'Ы'
        elif ch == 'z':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == 'h':
                    transliterated += 'ж'
                else:
                    transliterated += 'з'
                    i -= 1
            else:
                transliterated += 'з'
        elif ch == 'Z':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == 'h' or ch == 'H':
                    transliterated += 'Ж'
                else:
                    transliterated += 'З'
                    i -= 1
            else:
                transliterated += 'З'
        elif ch == '\'':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == '\'':
                    transliterated += 'Ь'
                else:
                    transliterated += 'ь'
                    i -= 1
            else:
                transliterated += 'ь'
        elif ch == '\"':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == '\"':
                    transliterated += 'Ъ'
                else:
                    transliterated += 'ъ'
                    i -= 1
            else:
                transliterated += 'ъ'
        elif ch == '\\':
            if i + 1 < len(inp):
                i += 1
                ch = inp[i]
                transliterated += ch
        elif ch == '{':
            while i + 1 < len(inp):
                i += 1
                ch = inp[i]
                if ch == '}':
                    break
                if ch == '\\':
                    if i + 1 < len(inp):
                        i += 1
                        ch = inp[i]
                        transliterated += ch
                        continue
                transliterated += ch
        else:
            transliterated += ch
        i += 1
    if copy_to_clipboard:
        pyperclip.copy(transliterated)
    if user_mode:
        print("Out: " + transliterated)
    else:
        print(transliterated)
        break
