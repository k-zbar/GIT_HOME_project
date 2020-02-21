import re


def zd1_most_ip(file_name, md, reg_str):
    with open(file_name, md) as my_file:
        all_res = []
        dict_res = {}
        str1 = my_file.readline()
        # Select the desired IP using reg expressions
        while str1:
            results = re.search(reg_str, str(str1))
            results = results.group()
            results = results.split(', ')
            results = [results.replace('(', '') for results in results]
            results = [results.replace(')', '') for results in results]
            all_res += results
            str1 = my_file.readline()
        for i in all_res:                                                   # Counted the dictionary elements
            if i in dict_res:
                dict_res[i] += 1
            else:
                dict_res[i] = 1
        list_dict_res = list(dict_res.items())                              # Transformed the dictionary in the list
        list_dict_res.sort(key=lambda k: k[1], reverse=True)                # Counted elements in the list
        dict_res = dict(list_dict_res)                                      # Transformed the list in the dictionary
        while True:
            try:
                kol = int(input("Enter the number of the most frequent IPs: "))
                if kol < 20:
                    break
                else:
                    print('Error!!! Try another one')
                    continue
            except:
                print('Error!!! Try another one')
        for i in dict_res:                                                  # Output the number of IPs
            if kol > 0:
                print('IP:', i, 'occurs', dict_res[i], 'times')
                kol -= 1


# print("---------------------------------------TASK-4.1---------------------------------------")
# zd1_most_ip("access_log", "r", r"[\(](\d|w|\.|,|\ |\'|(unknown)){1,}[\)]")
print("---------------------------------------TASK-4.2---------------------------------------")
