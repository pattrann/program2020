import os
print('enter router ip')
default = input()
os.system('tcpdump host ' + str(default) + ' > dump.txt && cat dump.txt')

