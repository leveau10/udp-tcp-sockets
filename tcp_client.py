import socket

target_host = 'localhost'
target_port = 8010

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

file_path = 'PPC__Tecnologia_em_Análise_e_Desenvolvimento_de_Sistemas_2012.pdf'
try:
    with open(file_path, "rb") as f:
        file_data = f.read()
        client.sendall(file_data)  
    print("PDF enviado via TCP.")
except FileNotFoundError:
    print(f"Arquivo '{file_path}' Não econtrado.")
finally:
    client.close()
