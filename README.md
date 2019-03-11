# Linux-Server-in-Python3

This program illustrates how to create a server in Python3. It's not the perfect server which can be deployed in real systems, But it gives a general idea of how a program in a computer communicates with another program in different computer through networking. 

<h2>Functions used</h2>
This project makes use of the socket module of python3. The socket module is imported so that the following necessary functions can be used:

1. <b>socket()</b>: This function is used to create a socket through python. A socket is necessary to communicate with other end. Infact, Communication is not possible without creating a socket.

2. <b>bind()</b>: A socket with no properties is useless. That's why we need to bind the socket to a specific IP address and specific port to listen on. And that is done using this function. 

3. <b>listen()</b>: After binding the socket to specific IP address and port number, It's time to listen for conncetions from different clients. And the connections are listened on the ports using this function.

4. <b>accept()</b>: Once we start getting connections from remote clients, it's time to accept them and interact with them. This is what the accept() does. It accepts connections from clients and stores their necessary information like socket file descriptor, IP address etc.

5. <b>sendall()</b>: sendall() is used to transmit textual messages to the client in the form of raw bytes. But it should be noted that sendall() can only be used in case of a TCP connection. 

6. <b>recv()</b>: recv() is used to receive the textual data received from the client and store it in a variable. After that, the response from the server can be easily printed on the screen using the print() function in python.
