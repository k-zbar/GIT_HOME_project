# Task-1
def zd1_nat(nat, word, ch_word):
    nat = nat.replace(word, ch_word)
    return nat


# Task-2
def zd2_mac(mac, sb, ch_sb):
    mac = mac.replace(sb, ch_sb) + ' ' + mac.replace(sb, ch_sb)
    return mac


# Task-3
def zd3_vlan(config):
    razb = config.split()
    razb = razb[-1].split(',')
    return razb


# Task-4
def zd4_sort_vlan(vlans):
    # REMOVE DUPLICATE ITEMS
    vlans = set(vlans)
    sort_vlans = sorted(vlans)
    return sort_vlans


# Task-5
def zd5_same_vlan(command1, command2):
    command1 = command1.split()
    command2 = command2.split()
    command1 = command1[-1].split(',')
    command2 = command2[-1].split(',')
    sort_com = sorted(set(command1) & set(command2))
    return sort_com


# Task-6
def zd6_form_vuvod(ospf_route):
    print("Inserted string: ", ospf_route)
    ospf_route = ospf_route.replace('O', 'OSPF')
    fin = ospf_route.split(' ')
    print("New strings: ")
    print('Protocol:\t\t\t', fin[0])
    print('Prefix:\t\t\t\t', fin[1])
    print('AD/Metric:\t\t\t', fin[2])
    print('Next-Hop:\t\t\t', fin[4].replace(',', ' '))
    print('Last update:\t\t', fin[5].replace(',', ' '))
    print('Outbound Interface:\t', fin[6])


# Task-7
def zd7_preobr(mac):
    print("Inserted string: ", mac)
    mac = mac.replace(':', '')
    mac = int(mac, 16)
    mac = bin(mac)
    print("New string: ", mac[2:])


# Task-8
def zd8_ip(ip):
    print("Inserted ip: ", ip)
    ip = ip.split('.')
    a, b, c, d = ip
    ip = '{0:<8} {1:<8} {2:<8} {3:<8}'.format(int(a), int(b), int(c), int(d))
    bip = '{:08b} {:08b} {:08b} {:08b}'.format(int(a), int(b), int(c), int(d))
    print(ip)
    print(bip)


# print("---------------------------------------TASK-1---------------------------------------")
# nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
# word = "Fast"
# ch_word = "Gigabit"
# print("Old string:", nat)
# zd_1 = zd1_nat(nat, word, ch_word)
# print("New string:", zd_1)
# print("\n---------------------------------------TASK-2---------------------------------------")
# mac = 'AAAA:BBBB:CCCC'
# sb = ':'
# ch_sb = '.'
# print('Old string:', mac)
# zd_2 = zd2_mac(mac, sb, ch_sb)
# print('New string:', zd_2)
# print("\n---------------------------------------TASK-3---------------------------------------")
# config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# print('Old string:', config)
# zd_3 = zd3_vlan(config)
# print('New string:', zd_3)
# print("\n---------------------------------------TASK-4---------------------------------------")
# vlans_list = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
# print('vlans:', vlans_list)
# zd4 = zd4_sort_vlan(vlans_list)
# print('sorted vlans:', zd4)
# print("\n---------------------------------------TASK-5---------------------------------------")
# command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
# command2 = 'switchport trunk allowed vlan 1,3,8,9'
# print('Old strings:', command1, '\n' + command2)
# zd5 = zd5_same_vlan(command1, command2)
# print('New string:', zd5)
print("\n---------------------------------------TASK-6---------------------------------------")
zd6_form_vuvod('O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0')
# print("\n---------------------------------------TASK-7---------------------------------------")
# zd7_preobr('AAAA:BBBB:CCCC')
# print("\n---------------------------------------TASK-8---------------------------------------")
# zd8_ip('192.168.3.1')
