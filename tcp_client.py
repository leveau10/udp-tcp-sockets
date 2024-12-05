import socket
import time 




print("Bem-vindo ao envio de pdf.")
print("Escolha um método de envio:")

print("Digite 1 para TCP e 2 para UDP:")

resposta = int(input())

target_host = 'localhost'
file_path = 'PPC__Tecnologia_em_Análise_e_Desenvolvimento_de_Sistemas_2012.pdf'

if resposta==1: #TCP
    target_port = 8010
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            client.sendall(file_data)  
        print("PDF enviado via TCP.")
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' Não econtrado.")
    finally:
        client.close()
elif resposta==2: #UDP
    target_port = 8011
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                client.sendto(chunk, (target_host, target_port))      
            client.sendto(b"END", (target_host, target_port))
            print("PDF enviado via UDP.")
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
    finally:
        client.close()
else:
    print("Desculpe, não entendi.")