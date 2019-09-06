import json
from difflib import get_close_matches
from colorama import init
from colorama import Back,Fore,Style

init()
file = json.load(open("data.json"))


def openfile(word):
    view=file[word]
    for item in view:
        print(item)


def matcher(match):
    return get_close_matches(match,file.keys())[0]

def main():
    while True:
        try:
            print(Fore.RESET)
            say = input("Input your word: ")
            say=say.lower();
            if say in file:
                print(Fore.YELLOW)
                openfile(say)
            elif say.title() in file:
                print(Fore.YELLOW)
                openfile(say.title())
            elif say.upper() in file:
                print(Fore.YELLOW)
                openfile(say.upper())
            elif len(matcher(say)):
                print(Fore.RED)
                print("Did you mean %s ?" % matcher(say))
                print(Fore.RESET)
                answer=input("Y/N\n ")
                answer=answer.upper()
                if answer=="Y":
                    print(Fore.YELLOW)
                    openfile(matcher(say))
                else:
                    print("I have no info about %s .Input another word!"%say)
            elif say not in file:
                print(Fore.RED)
                print("I have no info about %s"%say)
        except:
            print(Fore.RED)
            print("You can't input %s" %say)


if __name__ == '__main__':
    main()