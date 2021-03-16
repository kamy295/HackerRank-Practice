from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    list1 = list(arr)

    set1 = set(list1)
    list2 = list(set1)
    list2.sort(reverse=True)

    print(list2[1])




