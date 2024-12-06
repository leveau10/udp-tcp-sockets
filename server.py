import socket
import threading

tcp_port = 8010
udp_port = 8011

def udp_listen(sock):
    data, addr = sock.recvfrom(1024)  
    print(f"Conexão de: {addr}, UDP")
    
    try:
        with open("pdfUDP_recebido.pdf", "wb") as f:
            while True:
                data, addr = sockUDP.recvfrom(1024)
                if data == b"END":
                    break
                f.write(data)
            print("O pdf foi salvo como 'pdfUDP_recebido.pdf'")
    except Exception as e:
        print(f"Error: {e}")

def tcp_listen(sock):
    while True:
        conn, addr = sock.accept()
        print(f"Conexão de: {addr}, TCP")
        
        try:
            with open("pdfTCP_recebido.pdf", "wb") as f:
                while True:
                    data = conn.recv(1024)  
                    if not data:
                        break  
                    f.write(data)
            print("O pdf foi salvo como 'pdfTCP_recebido.pdf'")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            conn.close()

sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP

server_addressTCP = ('10.24.7.115', tcp_port)
server_addressUDP = ('10.24.7.115', udp_port)

sockTCP.bind(server_addressTCP)
sockUDP.bind(server_addressUDP)

sockTCP.listen(20)

t1 = threading.Thread(target=tcp_listen, args=(sockTCP,))
t2 = threading.Thread(target=udp_listen, args=(sockUDP,))

print("Esperando clients...")

t1.start()
t2.start()

t1.join()
t2.join()