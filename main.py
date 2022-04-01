import string_ops as s
# Testing the fuction of Find the nth occurrence of a word in a string!

string = "This is an example. Return the nth occurrence of example in this example string."
print(s.find_nth_occurrence("example", string, 1))
print(s.find_nth_occurrence("example", string, 2))
print(s.find_nth_occurrence("example", string, 3))
print(s.find_nth_occurrence("example", string, 4))

# Testing the function of Is it a palindrome?

print(s.is_palindrome('a'))
print(s.is_palindrome('Abba'))
print(s.is_palindrome('walter'))
print(s.is_palindrome('kodok'))
print(s.is_palindrome('Kasue'))
