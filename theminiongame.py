def minion_game(string):
    # your code goes here
    s_len = len(string)
    Stuart, Kevin = 0, 0

    for i in range(s_len):
        if string[i] in "AEIOU":
            Kevin += s_len - i
        else:
            Stuart += s_len - i
    if Stuart > Kevin:
        print("Stuart ", Stuart)
    elif Stuart < Kevin:
        print("Kevin ", Kevin)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)