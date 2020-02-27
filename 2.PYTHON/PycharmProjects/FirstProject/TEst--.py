# print("Enter time range:")
# kolvo = ['\nStart', '\nEnd']
# for i in kolvo:
#     while True:
#         try:
#             h = int(input(i + " date:\nHours: "))
#             m = int(input("Minutes: "))
#             s = int(input("Seconds: "))
#             if (h > 24) or (m > 60) or (s > 60):
#                 print('Error!!! Try another one')
#                 continue
#             else:
#                 tmp_date = str(h) + str(m) + str(s)
#                 print(tmp_date)
#                 break
#         except:
#             print('Error!!! Try another one')
#     print(tmp_date)


# Task-3
def one():
    l =[]
    for i in range(10**4):
        if i % 2 == 0:
            l.append(i)
    return l


def two():
    l = [x for x in range(10**4) if x % 2 == 0]
    return l


l1 = one()
l2 = two()
print(l1)
print(l2)
