def check_palindrome(word):
    if(word == word[:: - 1]):
        status=word
        return(True)
    else:
        return(False)

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
