from task_2 import *


def main():
    print("---------------------------------------TASK-1---------------------------------------")
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    word = "Fast"
    ch_word = "Gigabit"
    print("Old string:", nat)
    ch_line = zd1_nat(nat, word, ch_word)
    print("New string:", ch_line)
    print("\n---------------------------------------TASK-2---------------------------------------")
    mac = 'AAAA:BBBB:CCCC'
    sb = ':'
    ch_sb = '.'
    print('Old string:', mac)
    ch_mac = zd2_mac(mac, sb, ch_sb)
    print('New string:', ch_mac)
    print("\n---------------------------------------TASK-3---------------------------------------")
    config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
    print('Old string:', config)
    format_vlan = zd3_vlan(config)
    print('New string:', format_vlan)
    print("\n---------------------------------------TASK-4---------------------------------------")
    vlans_list = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    print('vlans:', vlans_list)
    vlans_rise = zd4_sort_vlan(vlans_list)
    print('sorted vlans:', vlans_rise)
    print("\n---------------------------------------TASK-5---------------------------------------")
    command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
    command2 = 'switchport trunk allowed vlan 1,3,8,9'
    print('Old strings:', command1, '\n' + command2)
    same_vlan = zd5_same_vlan(command1, command2)
    print('New string:', same_vlan)
    print("\n---------------------------------------TASK-6---------------------------------------")
    name = ('Protocol:\t\t\t', 'Prefix:\t\t\t\t', 'AD/Metric:\t\t\t', 'Next-Hop:\t\t\t', 'Last update:\t\t',
            'Outbound Interface:\t')
    ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
    print("Inserted string: ", ospf_route)
    form_str = zd6_form_vuvod(ospf_route)
    print("Changed strings: ")
    ind = 0
    for i in name:
        print(i, form_str[ind])
        ind += 1
    print("\n---------------------------------------TASK-7---------------------------------------")
    mac_address = 'AAAA:BBBB:CCCC'
    print("Inserted string: ", mac_address)
    mac_in_binary = zd7_preobr(mac_address)
    print("New string: ", mac_in_binary)
    print("\n---------------------------------------TASK-8---------------------------------------")
    ip = '192.168.3.1'
    print("Inserted ip: ", ip)
    ip, bip = zd8_ip(ip)
    print(ip, "\n" + bip)


main()
