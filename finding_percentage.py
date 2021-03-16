from pip._vendor.distlib.compat import raw_input

# def add(list1):
#     for i in list1:
#
#     result =
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        scores = map(sum(scores), scores)
        #print(scores)
        student_marks[name] = scores
    print(list(student_marks))
    query_name = raw_input()
    # yes = student_marks.__contains__(query_name)
    # if yes is True:
    #     s
    #     print("YES")

