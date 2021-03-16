
def is_leap(year):
    leap = False

    # if year % 100 == 0:
    #     if year % 400 == 0:
    #         return True
    #
    #     # Not divisible by 100
    # if year % 4 == 0:
    #     return True
    # return False

    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap

    # elif year % 100 == 0:
    #     return False
    # elif year % 400 == 0:
    #     return False


year1 = int(input())
print(is_leap(year1))
