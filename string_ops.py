# problem 1 :Find the nth occurrence of a word in a string!

def find_nth_occurrence(substring, string, occurrence=1):
    
    occur = 0
    for i in range(0, occurrence):
        occur = string.find(substring, occur + 1)    
    return occur    
    pass

# problem 2 : Is it a palindrome?

def is_palindrome(string):
    return string.lower() == string.lower()[::-1]
    pass