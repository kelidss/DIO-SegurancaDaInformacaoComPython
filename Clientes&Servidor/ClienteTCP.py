import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input ("Digite o Host ou Ip  aser conctado: ")
    PortaAlvo = input("Digite a porta a ser conctada: ")

    try:
        s.connect((HostAlvo, int (PortaAlvo)))
        print('Cliente TCP conectado com suceso no HOST' + HostAlvo + " e na porta:  " + PortaAlvo)
        s.shutdown(2)


    except socket.error as e:
        print('Não foi póssivel conectar no HOST' + HostAlvo + " e na porta:  " + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()