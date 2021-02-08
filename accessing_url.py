import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # enables socket in python
mysock.connect(('data.pr4e.org',80)) # connects to the respective webserver and the application in it with the port.
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # command to GET request to the server we connected.
mysock.send(cmd) # sending request

while True:
    data=mysock.recv(512) # gets the details of the page and its response(content). Fetches 512 characters.
    if len(data)<1:
        break
    print(len(data.decode()))
mysock.close()

# encode() and decode() -> used to convert the string(in the 'GET ......') to (bytes)UTF8 and vice-versa.
# encode is under string class-> str.encode(encoding="utf8")
# decode is under bytes class-> bytes.decode(encoding="utf8")