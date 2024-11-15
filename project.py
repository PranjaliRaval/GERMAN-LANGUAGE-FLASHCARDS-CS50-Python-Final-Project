# GERMAN LANGUAGE FLASHCARDS
from tkinter import *
from random import randint

# Define words
words = [
    (("Hallo"), ("Hello")),
    (("Tschüss"), ("Goodbye")),
    (("Ja"), ("Yes")),
    (("Nein"), ("No")),
    (("Bitte"), ("Please")),
    (("Danke"), ("Thank you")),
    (("Entschuldigung"), ("Excuse me / Sorry")),
    (("Guten Morgen"), ("Good morning")),
    (("Guten Abend"), ("Good evening")),
    (("Gute Nacht"), ("Good night")),
    (("Sein"), ("To be")),
    (("Haben"), ("To have")),
    (("Machen"), ("To do / To make")),
    (("Gehen"), ("To go")),
    (("Kommen"), ("To come")),
    (("Sprechen"), ("To speak")),
    (("Essen"), ("To eat")),
    (("Trinken"), ("To drink")),
    (("Lesen"), ("To read")),
    (("Schreiben"), ("To write")),
    (("Ich"), ("I")),
    (("Du"), ("You (informal)")),
    (("Er"), ("He")),
    (("Sie"), ("She / They / You (formal)")),
    (("Es"), ("It")),
    (("Wir"), ("We")),
    (("Ihr"), ("You (plural)")),
    (("Haus"), ("House")),
    (("Auto"), ("Car")),
    (("Buch"), ("Book")),
    (("Tisch"), ("Table")),
    (("Stuhl"), ("Chair")),
    (("Wasser"), ("Water")),
    (("Essen"), ("Food")),
    (("Freund"), ("Friend (male)")),
    (("Freundin"), ("Friend (female)")),
    (("Lehrer"), ("Teacher (male)")),
    (("Lehrerin"), ("Teacher (female)")),
    (("Wer"), ("Who")),
    (("Was"), ("What")),
    (("Wann"), ("When")),
    (("Wo"), ("Where")),
    (("Warum"), ("Why")),
    (("Wie"), ("How")),
    (("Heute"), ("Today")),
    (("Morgen"), ("Tomorrow")),
    (("Gestern"), ("Yesterday")),
    (("Jetzt"), ("Now")),
    (("Immer"), ("Always")),
    (("Oft"), ("Often"))
]

# Initialize the Tkinter window
root = Tk()
root.title('German Language Flashcards')
root.geometry("550x410")

# Get a count of our word list
count = len(words)

# Global variables for tracking
hinter = ""
hint_count = 0
random_word = 0

def next_word():
    global hinter, hint_count, random_word
    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset hint tracking
    hinter = ""
    hint_count = 0
    # Create random selection
    random_word = randint(0, count-1)
    # Update label with German word
    german_word.config(text=words[random_word][0])

def check_answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")

def provide_hint():
    global hint_count, hinter
    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1

# Labels
german_word = Label(root, text="", font=("Helvetica", 36))
german_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Create Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=check_answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next_word)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint", command=provide_hint)
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Run next_word function when program starts
next_word()

root.mainloop()
