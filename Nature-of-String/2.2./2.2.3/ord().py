'''

    if you want to know a specific character ASCII/UNICODE code point value,
    you can use ord() as ordinal. This function need a one-character string as its argument,
    breaching this requirement causes  a TypeError exception, and return a number
    representing  the argument's code point

    Conclusion: ord() is how we ask Python: 
    “Hey, what is the sequence number of this character in the computer code table?”

'''

# Demonstrating the ord() function

char_1 = 'a'
char_2 = ' '    # space

print(ord(char_1))
print(ord(char_2))
