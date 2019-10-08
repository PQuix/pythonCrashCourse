def palindrome(word):
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        print("True")
    else:
        print("False")

palindrome("Taco cat")
palindrome("A bba")
palindrome("Taco ca")