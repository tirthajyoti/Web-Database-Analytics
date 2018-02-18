import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
txt=''
flag=False

while True:
	data=mysock.recv(64)
	if len(data)<1:
		break
	if data.decode().find('Content-Type: text/plain')!=-1:
		flag=True
	if flag:
		txt += data.decode()
	#print(data.decode())
	#print("Next line...")
stpos = txt.find('text/plain')

print("Now printing all the relevant text received\n"+"-"*50)
print(txt[stpos+13:])
mysock.close()

