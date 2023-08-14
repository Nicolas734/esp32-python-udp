import socket
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

UDP_IP = config["UDP_CONFIG"]["ip"] or "127.0.0.1"
UDP_PORT = int(config["UDP_CONFIG"]["port"]) or 5002


print("Conexão com o servidor UDP na porta {} e no ip {}".format(UDP_PORT, UDP_IP))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MESSAGE = input("Digite uma mensagem: ").encode()

while MESSAGE != '\x18':
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    MESSAGE = input("Digite uma mensagem: ").encode()
