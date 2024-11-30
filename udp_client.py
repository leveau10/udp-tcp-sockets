import socket

target_host = 'localhost'
target_port = 8010

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file_path = 'PPC__Tecnologia_em_Análise_e_Desenvolvimento_de_Sistemas_2012.pdf'
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

