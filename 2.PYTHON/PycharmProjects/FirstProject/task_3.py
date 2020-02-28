# Task_6.1
def zd6_1_mac(mac):
    mac_cisco = []
    for i in mac:
        new_mac = i.replace(':', '.')
        mac_cisco.append(new_mac)
    return mac_cisco


# Task_6.2
def zd6_2_ip(ip):
    while True:
        try:
            ip = ip.split('.')
            b1, b2, b3, b4, = ip
            b1 = int(b1)
            b2 = int(b2)
            b3 = int(b3)
            b4 = int(b4)
        except ValueError:
            return False
        else:
            if (b1 < 0) or (b1 > 255) or (b2 < 0) or (b2 > 255) or (b3 < 0) or (b3 > 255) or (b4 < 0) or (b4 > 255):
                return False
            else:
                if (b1 >= 1) and (b1 <= 223):
                    result = "Unicast"
                    return result
                elif (b1 >= 224) and (b1 <= 239):
                    result = "Multicast"
                    return result
                elif (b1 == 255) and (b2 == 255) and (b3 == 255) and (b4 == 255):
                    result = "Local broadcast"
                    return result
                elif (b1 == 0) and (b2 == 0) and (b3 == 0) and (b4 == 0):
                    result = "Unassigned"
                    return result
                else:
                    result = "Unused"
                    return result


# Task_6.3
def zd6_3_access_trunk():
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk allowed vlan']
    access = {'0/12': '10',
              '0/14': '11',
              '0/16': '17',
              '0/17': '150'}

    trunk = {'0/1': ['add', '10', '20'],
             '0/2': ['only', '11', '30'],
             '0/4': ['del', '17']}

    print("===Access ports===")
    for intf, vlan in access.items():
        print('interface FastEthernet' + intf)
        for command in access_template:
            if command.endswith('access vlan'):
                print('  {} {}'.format(command, vlan))
            else:
                print('  {}'.format(command))

    print("\n===Trunk ports===")
    for intf, vlan in trunk.items():
        print('interface FastEthernet' + intf)
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                if vlan[0] == 'add':
                    print(' {} {}'.format(command, ', '.join(vlan)))
                elif vlan[0] == 'only':
                    print(' {} {}, {}'.format(command, vlan[1], vlan[2]))
                elif vlan[0] == 'del':
                    print(' {} remove {}'.format(command, vlan[1]))
            else:
                print(' {}'.format(command))


def main():
    # print("---------------------------------------TASK-6.1---------------------------------------")
    # mac_address = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
    # print("Inserted string: ", mac_address)
    # transformed_mac = zd6_1_mac(mac_address)
    # print("New string: ", transformed_mac)
    # print("\n---------------------------------------TASK-6.2---------------------------------------")
    # ip = input("Введите IP-адрес в формате 10.0.1.1: ")
    # result = zd6_2_ip(ip)
    # if not result:
    #     print("Wrong IP-address")
    # else:
    #     print("Введённый IP: ", ip, "\n" + result)
    print("\n---------------------------------------TASK-6.3---------------------------------------")
    zd6_3_access_trunk()


main()
