"""
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""

def romanToInt(s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} # Dictionary creation O(1) time
    z = 0
    for i in range(0, len(s) - 1): # Loop through the input, could be up to "n" characters long so O(n)
        if roman[s[i]] < roman[s[i+1]]: # Accessing a dictionary is O(1) time
            z -= roman[s[i]] # Accessing a dictionary is O(1) time
        else:
            z += roman[s[i]] # Accessing a dictionary is O(1) time
    return z + roman[s[-1]] # Accessing a dictionary is O(1) time

input = "XIV"
print(romanToInt(input))

# Overall the time complexity looks to be O(n) time.