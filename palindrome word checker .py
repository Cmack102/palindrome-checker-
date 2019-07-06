def if_palindrome(test):
    word = ""
    m = -1
    length = len(test)
    length = length * -1
    while m >= length:
        word = word + test[m]
        m = m - 1
    if word == test:
        print(test, "is a palindrome")
    else:
        print(test, "is not a palindrome")

if_palindrome("chad")
    
if_palindrome("reah")
if_palindrome("lol")
