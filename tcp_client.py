import socket

target_host = "127.0.0.1"
target_port = 8000


#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
client.connect((target_host, target_port))

#send some data
request = (
	"GET / HTPP/1.1\r\n"
	"Host: localhost\r\n"
	"Connection: close\r\n\r\n"

	)

client.sendall(request.encode())

while True:
	response = client.recv(4096)
	if not response:
		break
	print(response.decode(errord="replace"), end="")

client.close()

