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


# # Task_6.3
# def zd6_3_access_trunk():
#     access_template = ['switchport mode access',
#                        'switchport access vlan',
#                        'spanning-tree portfast',
#                        'spanning-tree bpduguard enable']
#     trunk_template = ['switchport trunk encapsulation dot1q',
#                       'switchport mode trunk',
#                       'switchport trunk allowed vlan']
#     access = {'0/12': '10',
#               '0/14': '11',
#               '0/16': '17',
#               '0/17': '150'}
#
#     trunk = {'0/1': ['add', '10', '20'],
#              '0/2': ['only', '11', '30'],
#              '0/4': ['del', '17']}
#
#     print("===Access ports===")
#     for intf, vlan in access.items():
#         print('interface FastEthernet' + intf)
#         for command in access_template:
#             if command.endswith('access vlan'):
#                 print('  {} {}'.format(command, vlan))
#             else:
#                 print('  {}'.format(command))
#
#     print("\n===Trunk ports===")
#     for intf, vlan in trunk.items():
#         print('interface FastEthernet' + intf)
#         for command in trunk_template:
#             if command.endswith('allowed vlan'):
#                 if vlan[0] == 'add':
#                     print(' {} {}'.format(command, ', '.join(vlan)))
#                 elif vlan[0] == 'only':
#                     print(' {} {}, {}'.format(command, vlan[1], vlan[2]))
#                 elif vlan[0] == 'del':
#                     print(' {} remove {}'.format(command, vlan[1]))
#             else:
#                 print(' {}'.format(command))
#
#
# print("\n---------------------------------------TASK-6.3---------------------------------------")
# zd6_3_access_trunk()


# def decorator_function(func):
#     def wrapper():
#         print('Функция обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         func()
#         print('Выходим из обёртки')
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
#
#
# hello_world()

