string = 'abdcab'
table = {}
def first_recurring(string):
    for n in string:
        if n in table:
            return n
        table[n] = 1
    return None
print(first_recurring(string))