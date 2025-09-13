#In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code 
# per the below, wherein is_valid still expects a str as input and returns True if that str meets 
# all requirements and False if it does not, but main is only called if the value of __name__ 
# is "__main__":

from plates import is_valid

def test_start_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False     #Starting 2 letter should be alphabet
    assert is_valid("50CS") == False    #Starting 2 letter should be alphabet

def test_length():
    assert is_valid("CS") == True        # minimum 2
    assert is_valid("CS50") == True
    assert is_valid("CS5050") == True    # maximum 6
    assert is_valid("CS50501") == False  # too long

def test_numbers_at_end():
    assert is_valid("CS50") == True      # valid, numbers at end
    assert is_valid("CS05") == False     # first number can’t be 0
    assert is_valid("CS50P") == False    # letters after number not allowed

def test_only_alnum():
    assert is_valid("CS50!") == False   #No special symbols
    assert is_valid("HELLO.") == False      #No special symbols
    assert is_valid("HELLO") == True