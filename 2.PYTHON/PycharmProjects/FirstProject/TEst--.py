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
def zd3_vlan(config):
    print('Old string:', config)
    razb = config.split()
    razb = razb[-1].split(',')
    print('New string:', end=" ")
    return razb


zd_3 = zd3_vlan('switchport trunk allowed vlan 1,3,10,20,30,100')
print(zd_3)

