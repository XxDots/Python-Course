'''

    Like other kinds of data, strings have their own set of permissible operations, 
    although they're rather limited compared to numbers.
    
    In general, strings can be:

        concatenated (joined)
        replicated.
    
    The first operation is performed by the + operator (note: it's not an addition) 
    while the second by the * operator (note again: it's not a multiplication).

    The ability to use the same operator against completely different kinds of data 
    (like numbers vs. strings) is called overloading (as such an operator is overloaded with different duties).

'''

# Example 

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(str1 * 5)
print(5* str2)

