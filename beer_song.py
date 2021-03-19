
# 2 bottles of beer on the wall, 2 bottle of beer.
# Take it down and pass it around, 1 bottle of beer on the wall.
#
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take it down and pass it around, no more bottles of beer on the wall.
#
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.


def recite(start, take=1):
    number_of_bottles = start
    if number_of_bottles > 2:
        plural_1 = "s"
        plural_2 = "s"

    verse = f"{number_of_bottles} bottle{plural_1} of beer on the wall, " \
            f"{number_of_bottles} bottle{plural_1} of beer.\n" \
            f"Take it down and pass it around," \
            f" {number_of_bottles-1} bottle{plural_1} of beer on the wall."


    print(verse)
    pass

recite(5)
