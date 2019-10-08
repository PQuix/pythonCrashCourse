for i in reversed(range(1, 100)):
    if i == 1:
        print(str(i) + " bottle of beer on the wall, " + str(i) + " bottle of beer!")
        print("You chug one down, pass it around, " + str(i-1) + " bottles of beer on the wall!\n")
    else:
        print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer!")
        print("You chug one down, pass it around, " + str(i-1) + " bottles of beer on the wall!\n")