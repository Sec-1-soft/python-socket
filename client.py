import socket
import sys

sock = socket.socket()
sock.connect(('localhost',4242))
print('Sunucuya bağlanıldı...')

while True:
    
    try:
        fl = sock.recv(4096).decode('utf-8')
        print('Sunucu sana dosya gönderdi...')
        
        f = input('Dosya ismini giriniz#>')
        f = f + ".txt"
        
        with open(f,'w') as file:
            file.write(fl)
            
        print(f'{f} belgesi {sys.path[0]} yolunda kayıt edildi.')
        break
              
    except: 
        print('Dosya oluşturulamadı')
        sys.exit()