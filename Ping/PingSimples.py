import os

print('#' * 60)

ip_ou_host = input('digite ip ou host a ser verificado: ')
print('-' * 60)
os.system('ping -n 6 {}'.format(ip_ou_host))
print('-' * 60)