import socket
import sys

# Gerekli bağlantı bilgilerini girin
HOST = 'localhost'
PORT = 4242
clients = []
clients_ = []

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bağlantıyı aç
        sock.bind((HOST, PORT))

        # Bağlantı noktası sayısını belirt.
        listen = input('Client sayısı#>')
        sock.listen(int(listen))
        
        conn, addr = sock.accept()
        clients.append(f'{addr[0]}:{addr[1]} istemcisi bağlandı...')
        
        i = 0
        for client in clients:
            print('No:', i, ':', client)
            i = i+1

        # Client dinle
        try:
            fname = input('Dosya ismini giriniz#>')
            file = open(fname, 'r')
            content = file.read()
            
            conn.sendall(content)
            sock.close()
            clients.remove(client)
            if not clients :
                sys.exit()
            
        except IOError:
            print('Dosya ismini yanlış girdiniz !')
        
    except Exception as e:
        print('Bağlantı sağlanamadı:', str(e))
        sys.exit()
