# import socket module
import sys
from socket import *
 # In order to terminate the program

# ip_port = ('127.0.0.1',9999)
# ip_port=('128.238.251.26',45,62)
ip_port=('192.168.199.246',32323)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ip_port)
serverSocket.listen(5)
# Prepare a sever socket
# Fill in start

# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    # Fill in start              #Fill in end
    try:
        message=connectionSocket.recv(1000)
        print("message is:"+message)

        # print(message)
        # Fill in start          #Fill in end
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read()
        # Fill in start
        connectionSocket.send("HTTP/1.1 200  OK\r\n\r\n")
        #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        print(outputdata)
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print("message replied")
        connectionSocket.close()
        print("close succ")
    except IOError:
# Send response message for file not found
        print("message replied")
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.close()
        # connectionSocket.close()

# Fill in start
# Fill in end
# Close client socket
# Fill in start
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
