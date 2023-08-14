import socket
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

UDP_IP = config["UDP_CONFIG"]["ip"] or "127.0.0.1"
UDP_PORT = int(config["UDP_CONFIG"]["port"]) or 5002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Servidor UDP iniciado na porta {} e no ip {}".format(UDP_PORT, UDP_IP))

while True:
    data, addr = sock.recvfrom(1024)
    print("Recebido: ", data, "|", addr)