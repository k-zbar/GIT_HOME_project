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



def zd8_ip(ip):
    print("Inserted ip: ", ip)
    ip = ip.split('.')
    a, b, c, d = ip
    ip = '{0:<8} {1:<8} {2:<8} {3:<8}'.format(int(a), int(b), int(c), int(d))
    bip = '{:08b} {:08b} {:08b} {:08b}'.format(int(a), int(b), int(c), int(d))
    print(ip)
    print(bip)

zd8_ip('192.168.3.1')
