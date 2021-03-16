def swap_case(s):
    
    # newstring = ' '
    # for i in s:
    #     if i.isupper()==True:
    #        newstring += (i.lower())
    #     elif i.islower() == True:
    #         newstring += (i.upper())
    #     elif i.isspace()== True or i == '"' or i.isascii == True:
    #         newstring += (i)
          
    
            
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)