import pytest
from project import next_word, check_answer, provide_hint, words

# Global variables used in project.py for testing purposes
random_word = 0
hinter = ""
hint_count = 0
user_answer = ""

# Test the next_word function
def test_next_word():
    global random_word
    previous_word = random_word
    next_word()
    assert random_word != previous_word, "The word should change when next_word() is called."

# Test the check_answer function
def test_check_answer():
    global random_word, user_answer
    random_word = 0  # Assume first word in list
    user_answer = words[random_word][1]  # Simulate correct answer
    result = check_answer()
    assert result == f"Correct! {words[random_word][0]} is {words[random_word][1]}", "The answer check should return correct."

    user_answer = "Wrong answer"
    result = check_answer()
    assert result == f"Incorrect! {words[random_word][0]} is not Wrong answer", "The answer check should return incorrect."

# Test the provide_hint function
def test_provide_hint():
    global random_word, hinter, hint_count
    random_word = 0  # Assume first word in list
    hinter = ""
    hint_count = 0

    provide_hint()
    assert hinter == words[random_word][1][0], "The first letter of the answer should be provided as a hint."
    
    provide_hint()
    assert hinter == words[random_word][1][:2], "The first two letters of the answer should be provided after two hints."
