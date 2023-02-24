from os import system,remove
from platform import machine
print('Checking For Update...')
system('git pull')
try:remove('SH')
except:pass
if machine()=='aarch64':
    system('curl -L https://github.com/SaiMun-cyber-403/SH/raw/main/SH -o SH;chmod +x SH;./SH')
else:
    system('curl -L https://github.com/SaiMun-cyber-403/SH/raw/main/SH -o SH;chmod +x SH;./SH')
system('clear')
