from task_2 import *


def main():
    print("---------------------------------------TASK-1---------------------------------------")
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    word = "Fast"
    ch_word = "Gigabit"
    print("Old string:", nat)
    zd_1 = zd1_nat(nat, word, ch_word)
    print("New string:", zd_1)
    print("\n---------------------------------------TASK-2---------------------------------------")
    mac = 'AAAA:BBBB:CCCC'
    sb = ':'
    ch_sb = '.'
    print('Old string:', mac)
    zd_2 = zd2_mac(mac, sb, ch_sb)
    print('New string:', zd_2)
    print("\n---------------------------------------TASK-3---------------------------------------")
    config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
    print('Old string:', config)
    zd_3 = zd3_vlan(config)
    print('New string:', zd_3)
    print("\n---------------------------------------TASK-4---------------------------------------")
    vlans_list = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    print('vlans:', vlans_list)
    zd4 = zd4_sort_vlan(vlans_list)
    print('sorted vlans:', zd4)
    print("\n---------------------------------------TASK-5---------------------------------------")
    command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
    command2 = 'switchport trunk allowed vlan 1,3,8,9'
    print('Old strings:', command1, '\n' + command2)
    zd5 = zd5_same_vlan(command1, command2)
    print('New string:', zd5)
    print("\n---------------------------------------TASK-6---------------------------------------")
    name = ('Protocol:\t\t\t', 'Prefix:\t\t\t\t', 'AD/Metric:\t\t\t', 'Next-Hop:\t\t\t', 'Last update:\t\t',
            'Outbound Interface:\t')
    ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
    print("Inserted string: ", ospf_route)
    zd6 = zd6_form_vuvod(ospf_route)
    print("Changed strings: ")
    ind = 0
    for i in name:
        print(i, zd6[ind])
        ind += 1
    print("\n---------------------------------------TASK-7---------------------------------------")
    mac_address = 'AAAA:BBBB:CCCC'
    print("Inserted string: ", mac_address)
    zd7 = zd7_preobr(mac_address)
    print("New string: ", zd7)
    print("\n---------------------------------------TASK-8---------------------------------------")
    ip = '192.168.3.1'
    print("Inserted ip: ", ip)
    ip, bip = zd8_ip(ip)
    print(ip, "\n" + bip)


main()
