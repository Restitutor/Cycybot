#!/usr/bin/env python


def cinput(prompt: str | None = None) -> str:
    if prompt:
        print(prompt)
    return input().strip().lower()


def ask_yes(question: str) -> bool:
    return cinput(question) == "yes"


def ask_character(name: str) -> None:
    if ask_yes(f"Is your character {name}?"):
        print("Guessed right another time :)")
    else:
        print("That's embarrassing, let's try again.")


def main() -> None:
    # Friend Guesser
    print("Welcome, I'm AkinatorGuyyy! \U0001f9de")
    print("Today I will manage to guess your friend! (As long as cycy added them!)")
    print("Please answer the following questions with 'yes' or 'no'")

    # Questions
    if ask_yes("Is your character a youtuber?"):
        if ask_yes("Does your character has more than 100 subscribers?"):
            if ask_yes("Is your character part of CyHub?"):
                if ask_yes("Does your character play chess?"):
                    if ask_yes("Is your character European"):
                        if ask_yes("Was the character's account hacked?"):
                            ask_character("Zell")
                        else:
                            ask_character("EitiFre")
                    else:
                        ask_character("Syntax")
                else:
                    ask_character("Allen")
            elif ask_yes("Does your character make fotd's?"):
                if ask_yes("Did you character reach 2 years of fotds?"):
                    ask_character("Minecraftr")
                else:
                    ask_character("Moon")
            elif ask_yes("Did your character made an entire website?"):
                ask_character("Naviary")
            else:
                ask_character("EitiFrie")
        elif ask_yes("Is you character European?"):
            if ask_yes("Does your character play chess?"):
                if ask_yes("Is your character Hungarian?"):
                    ask_character("Who am I")
                else:
                    ask_character("ChessGuyyy")
            elif ask_yes("Is your character Swedish?"):
                ask_character("Jonathan")
            else:
                ask_character("Mehball")
        else:
            ask_character("bareth")
    elif ask_yes("Is your character part of Tiger's Park (Jonathan's server)?"):
        if ask_yes("Is your character mod in that server?"):
            ask_character("Game_Nerd")
        else:
            ask_character("NonAccounter")
    elif ask_yes("Is your character part of MoonGuyyy's server?"):
        if ask_yes("Is your character Austrailian?"):
            ask_character("Robadog")
        else:
            ask_character("Res")
    elif ask_yes("Is your character Turkish?"):
        ask_character("AncasTier")
    else:
        ask_character("Sagoram/Blank")


if __name__ == "__main__":
    main()
