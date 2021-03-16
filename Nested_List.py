from pip._vendor.distlib.compat import raw_input

#
# def sort(list3):
#     return sorted(list3, key = lambda x: x[1])
#
#
# if __name__ == '__main__':
#     list1 = []
#     list2 = {}
#     list3 = []
#     for _ in range(int(raw_input())):
#         name = raw_input()
#         score = float(raw_input())
#
#         list2 = [name, score]
#         list1.append(list2)
#
#
#     list3 = sort(list1)
#
#     #print("List1 is " + list1)
#     print("List3 is ", list3)
#
#
N = int(raw_input())

students = list()
for i in range(N):
    students.append([raw_input(), float(raw_input())])

scores = set([students[x][1] for x in range(N)])
scores = list(scores)
scores.sort()

students = [x[0] for x in students if x[1] == scores[1]]
students.sort()

for s in students:
    print(s)