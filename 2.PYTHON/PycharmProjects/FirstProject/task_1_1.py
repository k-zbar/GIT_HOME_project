import random

sm = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
bg = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
nm = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
sp = ('-', '+', '=', '%', '@', '""', '?', '!', '&', '.', ',')
# kmb = ['s', '1', 'd', '2', 'A', '3', 'a', '4']
kmb = []

print("Pattern: [a-z] - a; [A-Z] - A; [0-9] - d; [symbols] - s;  a3d2s2A4")
print("Enter the desired character by pattern and number of characters:")
for i in range(4):
    ''' LETTER CHECK '''
    while True:
        ch_tmp = input("Input character [" + str(i + 1 + i) + "]: ")
        if (ch_tmp != 'a') and (ch_tmp != 'A') and (ch_tmp != 'd') and (ch_tmp != 's'):
            print("Error!!! Inappropriate letter. Try another one: ")
        else:
            kmb.append(ch_tmp)
            break
    ''' NUMBER OF CHARACTERS CHECK '''
    while True:
        ch_tmp = input("Input number of characters [" + str(i + 2 + i) + "]: ")
        try:
            int(ch_tmp) >= 6
        except ValueError:
            print("Error!!! Inappropriate number of characters. Try another one: ")
        else:
            if int(ch_tmp) >= 6:
                print("Error!!! Inappropriate number of characters. Try another one: ")
            else:
                kmb.append(ch_tmp)
                break
print("Your pattern: ", end='')
for i in kmb:
    print(i, end='')
print("\n\nGenerated password: ", end='')

''' GENERATED PASSWORD '''
for i in range(0, len(kmb)):
    if kmb[i] == 'a':
        print(''.join(random.sample(sm, int(kmb[i + 1]))), end='')
    elif kmb[i] == 'd':
        print(''.join(random.sample(nm, int(kmb[i + 1]))), end='')
    elif kmb[i] == 's':
        print(''.join(random.sample(sp, int(kmb[i + 1]))), end='')
    elif kmb[i] == 'A':
        print(''.join(random.sample(bg, int(kmb[i + 1]))), end='')


