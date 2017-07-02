import sys
class Flashcard:

    def __init__(self, word, reading, meaning):
        self.word = word
        self.reading = reading
        self.meaning = meaning

    def __str__(self):
        flash_card = ""
        flash_card += "Word: " + self.word + "\n" + "Reading: " + self.reading + "\n" + "Meaning: " + self.meaning
        return flash_card

kokusai = Flashcard("国際", "こくさい", "International")
kyouiku = Flashcard("教育", "きょういく", "Educational")
centa = Flashcard("センター", "", "Center")
toujyou = Flashcard("登場", "とうじょう", "Entry")

word_list = [kokusai, kyouiku, centa, toujyou]

user_input = str(input("Ready? (y/n)\n"))

if user_input in ["yes", "y"]:
    for every_card in word_list:
        user_input = str(input("Next Card? (y/n)\n"))
        if user_input in ["yes", "y"]:
            print("\n" + str(every_card) + "\n")
        else:
            print("Okay. Goodluck!")
else:
    sys.exit(0)
