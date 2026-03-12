"""

    The find() method is similar to index(). it look for a substring and 
    return the index of the first occurrence of this substring. but: 

    it safer - but doesn't generate an error for an argument containing
    a non-existment substring(it returns -1 then)
    
    it works with strings only - don't try to apply it to any other
    sequence


"""

# Example for find() method
print("Subs".find("ub"))        # Output: 1     -because "ub" starts at index 1
print("Crime".find("Su"))       # Output: -1    -because "Su" is not found
