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



# Task-6
def zd6_form_vuvod(ospf_route):
    ospf_route = ospf_route.replace('O', 'OSPF')
    fin = ospf_route.split(' ')
    fin[4] = fin[4].replace(',', ' ')
    fin[5] = fin[5].replace(',', ' ')
    print("OOOO", fin[3])
    # return fin
    print("New strings: ")
    print('Protocol:\t\t\t', fin[0])
    print('Prefix:\t\t\t\t', fin[1])
    print('AD/Metric:\t\t\t', fin[2])
    print('Next-Hop:\t\t\t', fin[4])
    print('Last update:\t\t', fin[5])
    print('Outbound Interface:\t', fin[6])


print("\n---------------------------------------TASK-6---------------------------------------")
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
print("Inserted string: ", ospf_route)
zd6 = zd6_form_vuvod(ospf_route)

