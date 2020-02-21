import re

# # [\[][0-9]+\D\w+\D\d+\D\d+\D\d+\D\d+\D+\d+[\]]
# # [0-9]+\D\w+\D\d+(\D\d+){1,}\D{2}\d{4}

with open("test_access_log", "r") as my_file:
    all_res = []
    dict_res = {}
    str1 = my_file.readline()
    # Select the desired IP using reg expressions
    while str1:
        results = re.search(r"([:]\d{2,}){3,}", str(str1))
        results = results.group()

        results = results[1:]
        # results = results.split(':')
        print(results)
        all_res.append(results)
        str1 = my_file.readline()
    all_res = sorted(all_res)
    print(all_res)
    print("Enter time range:")
    kolvo = ['\nStart', '\nEnd']
    for i in kolvo:
        while True:
            try:
                h = int(input(i + " date:\nHours:"))
                m = int(input("Minutes:"))
                s = int(input("Seconds:"))
                if (h > 24) or (m > 60) or (s > 60):
                    print('Error!!! Try another one')
                    continue
                else:
                    st = ''.join()
                    break
            except:
                print('Error!!! Try another one')

    # for i in all_res:
    #     if i








# list = ['09:03:33', '09:01:41', '09:03:31', '09:01:42']
# print(list)
# list.sort()
# print(list)
# a = input("Input start time: ")
# b = input("Input end time: ")
# if b < a:
#     print("b<a")
# else:
#     print("a>b")
