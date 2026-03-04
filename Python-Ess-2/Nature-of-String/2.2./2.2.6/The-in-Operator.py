'''

    The in operator shouldn't surprise you when applied to strings it simply checks 
    if its left argument (a string) can be found anywhere within the right argument 
    (another string).

    The result of the check is simply True or False.
    
    Look at the example program below. This is how the in operator works:

'''


alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
