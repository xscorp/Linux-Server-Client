# Linux Server-Client project in Python3

This program illustrates how to create a server in Python3. It's not the perfect server which can be deployed in real systems, But it gives a general idea of how a program in a computer communicates with another program in different computer through networking. 

<h2>Functions used from socket module</h2>
This project makes use of the socket module of python3. The socket module is imported so that the following necessary functions can be used:

1. <b>socket()</b>: This function is used to create a socket through python. A socket is necessary to communicate with other end. Infact, Communication is not possible without creating a socket.

2. <b>bind()</b>: A socket with no properties is useless. That's why we need to bind the socket to a specific IP address and specific port to listen on. And that is done using this function. 

3. <b>listen()</b>: After binding the socket to specific IP address and port number, It's time to listen for conncetions from different clients. And the connections are listened on the ports using this function.

4. <b>accept()</b>: Once we start getting connections from remote clients, it's time to accept them and interact with them. This is what the accept() does. It accepts connections from clients and stores their necessary information like socket file descriptor, IP address etc.

5. <b>sendall()</b>: sendall() is used to transmit textual messages to the client in the form of raw bytes. But it should be noted that sendall() can only be used in case of a TCP connection. 

6. <b>recv()</b>: recv() is used to receive the textual data received from the client and store it in a variable. After that, the response from the server can be easily printed on the screen using the print() function in python.

7. <b>connect()</b>: connect() is a socket system call used for establishing a connection to remote system. The connect() function accepts a tuple of remote IP address and port number as argument to function. 

<h2>Other functions</h2>

1. <b>sys.exit()</b>: sys.exit() is a function defined in sys module which is used for the termination of the code.

2. <b>printUsage()</b>: printUsage() is a user defined function for displaying the correct usage of the program to the user in case the initial arguments given by user are invalid.

3. <b>errorExit()</b>: errorExit() is another user defined function being used for doing two operations i.e. first, closing the socket and then terminating the program. This is used either when the user tries to terminate the connection or when an internal problem occurs.

<h2>Advantages of the project</h2>

1. This project strongly implements the Exception handling. In case any user interrupts it through keyboard, it is armed with right exit conditions which will not display unnecessary errors to users.

2. The communication is bidirectional. That is why both the client and server can communicate to each other.

3. User don't need to write any specific word as an "exit code". User simply needs to press (CTRL + C) to terminate the connection.

<h2>Limitations of the project</h2>

1. Only IPV4 addresses can be used. Support for IPV6 isn't added yet. 

2. Due to the absence of attractive GUI, it seems unrealistic to a normal user

3. Due to the absence of multithreading, User can't send/receive more than one messages in one go due to the presence of send, receive chain.
  [send] [receive] [send] [receive] [send] [receive]
 
 
