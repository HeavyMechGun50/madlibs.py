print("\nHello and welcome to Mad Libs! A popular game recreated on Python!")
import random
import time as t

ruleAsk = input("Do you know the rules? (y/n)\n")
ruleAsk = ruleAsk.lower()
if ruleAsk == "y" or ruleAsk == "yes":
    print("\nOk! Great!")
elif ruleAsk == "n" or ruleAsk == "no":
    print(
        "\nWell, it's a fairly simple game. I tell you to enter a word from different categories and then you enter them. Once the asking part's done, all you gotta do is read the craziness you've created and probably have a chuckle at it :). That's basically all to it!"
    )
# else:
# while ruleAsk != "n" or ruleAsk != "no" or ruleAsk != "y" or ruleAsk != "yes":
# ruleAsk = str(input("Sorry, I didn't really understand what you meant. Could you repeat your answer and stick to simpler words like \"no\" or \"yes\", or simply just the letter?\n"))
# ruleAsk = ruleAsk.lower()
t.sleep(1.5)
print("\nLet's get started!")

adjectives = input("\nEnter 3 adjectives\n")
adjectives = adjectives.split()
adjectivesList = list(adjectives)
if len(adjectivesList) != 3:
    while len(adjectivesList) != 3:
        adjectives = input(
            "\nSorry. There was either a problem with the code or you didn't enter 3 adjectives as I requested. Please re-enter 5 adjectives. Make sure they're split with a space and comma and make sure they're only one word each!\n"
        )
        adjectives = adjectives.split()
        adjectivesList = list(adjectives)

nouns = input("\nEnter 9 nouns\n")
nouns = nouns.split()
nounsList = list(nouns)
if len(nounsList) != 9:
    while len(nounsList) != 9:
        nouns = input(
            "\nSorry. There was either a problem with the code or you didn't enter 9 nouns as I requested. Please re-enter 5 nouns. Make sure they're split with a space and comma!\n"
        )
        nouns = nouns.split()
        nounsList = list(nouns)

verbsWithIng = input('\nEnter 4 verbs ending with "ing"\n')
verbsWithIng = verbsWithIng.split()
verbsWithIngList = list(verbsWithIng)
if len(verbsWithIngList) != 4:
    while len(verbsWithIngList) != 4:
        verbsWithIng = input(
            '\nSorry. There was either a problem with the code or you didn\'t enter 4 verbs ending with "ing" as I requested. Please re-enter 5 verbs ending with "ing". Make sure they\'re split with a space and comma!\n'
        )
        verbsWithIng = verbsWithIng.split()
        verbsWithIngList = list(verbsWithIng)

verbs = input("\nEnter 4 verbs\n")
verbs = verbs.split()
verbsList = list(verbs)
if len(verbsList) != 4:
    while len(verbsList) != 4:
        verbs = input(
            "\nSorry. There was either a problem with the code or you didn't enter 4 verbs as I requested. Please re-enter 5 verbs. Make sure they're split with a space and comma!\n"
        )
        verbs = verbs.split()
        verbsList = list(verbs)


verbsEd = input("\nEnter 3 verbs in the past tense (ending with ED)\n")
verbsEd = verbsEd.split()
verbsEdList = list(verbs)
if len(verbsEd) != 3:
    while len(verbsEd) != 3:
        verbsEd = input(
            "\nSorry. There was either a problem with the code or you didn't enter 3 past tense verbs as I requested. Please re-enter 5 past tense verbs. Make sure they're split with a space and comma!\n"
        )
        verbsEd = verbsEd.split()
        verbsEdList = list(verbsEd)


def extract(word):
    if word == "adj":
        word = random.randint(0, len(adjectivesList))
        if word == 0:
            word = adjectivesList[0]
            del adjectivesList[0]
        elif word == 1:
            word = adjectivesList[1]
            del adjectivesList[1]
        elif word == 2:
            word = adjectivesList[2]
            del adjectivesList[2]

    elif word == "noun":
        word = random.randint(0, len(nounsList))
        if word == 0:
            word = nounsList[0]
            del nounsList[0]
        elif word == 1:
            word = nounsList[1]
            del nounsList[1]
        elif word == 2:
            word = nounsList[2]
            del nounsList[2]
        elif word == 3:
            word = nounsList[3]
            del nounsList[3]
        elif word == 4:
            word = nounsList[4]
            del nounsList[4]
        elif word == 5:
            word = nounsList[5]
            del nounsList[5]
        elif word == 6:
            word = nounsList[6]
            del nounsList[6]
        elif word == 7:
            word = nounsList[7]
            del nounsList[7]
        elif word == 8:
            word = nounsList[8]
            del nounsList[8]            

    elif word == "ing":
        word = random.randint(0, len(verbsWithIngList))
        if word == 0:
            word = verbsWithIngList[0]
        elif word == 1:
            word = verbsWithIngList[1]
            del verbsWithIngList[1]
        elif word == 2:
            word = verbsWithIngList[2]
            del verbsWithIngList[2]
        elif word == 3:
            word = verbsWithIngList[3]
            del verbsWithIngList[3]

    elif word == "verb":
        word = random.randint(0, len(verbsList))
        if word == 0:
            word = verbsList[0]
            del verbsList[0]
        elif word == 1:
            word = verbsList[1]
            del verbsList[1]
        elif word == 2:
            word = verbsList[2]
            del verbsList[2]
        elif word == 3:
            word = verbsList[3]
            del verbsList[3]

    elif word == "ed":
        word = random.randint(0, len(verbsEdList))
        if word == 0:
            word = verbsEdList[0]
            del verbsEdList[0]
        elif word == 1:
            word = verbsEdList[1]
            del verbsEdList[1]
        elif word == 2:
            word = verbsEdList[2]
            del verbsEdList[2]

    return word


print("Alright! Thank you for your provided answers. Are you ready to read the story?")

print(
    "One day, I was",
    extract("ing"),
    "around in my ",
    extract("noun"),
    " when I suddenly saw a ",
    extract("noun"),
    " licking his ",
    extract("noun"),
    " on top of a ",
    extract("noun"),
    ". I found that pretty ",
    extract("adj"),
    " because of the ",
    extract("adj"),
    " place the thing ",
    extract("verb"),
    ". A few moments later, a ",
    extract("noun"),
    " came ",
    extract("ing"),
    " at a very ",
    extract("adj"),
    " speed, ",
    extract("ing"),
    " the thing away. But the thing wasn't able to ",
    extract("verb"),
    " the way he'd ",
    extract("ed"),
    " to. That ",
    extract("noun"),
    " somehow managed to ",
    extract("verb"),
    " inside the trashcan and then came ",
    extract("ing"),
    " outside of the ",
    extract("noun"),
    ", landing on the ",
    extract("noun"),
    ". Since it was ",
    extract("ed"),
    ", it ",
    extract("ed"),
    " away at the speed of light!",
)
