# Networking

# Overview

This program writes the code for a TCP server and client that can connect to the server. This server is able to receive messages from a client and send that message to any other client that is connect to the server.

[Software Demo Video](https://youtu.be/YTgh5Le8m3g)

# Network Communication

The architecture I used is client/server on a TCP server using port number: 4954. 

# Development Environment

In order to write this, I imported two libraries, socket and threading. This made it possible to define the server type I wanted to make. In this case I used socket.SOCK_STREAM to create the TCP server. It also made it possible to determine what IP addresses could connect to the server, in this case I used IPv4.

# Useful Websites


* [Python Documentation](https://docs.python.org/3/library/socket.html)
* [Void Realms TCP Basics Tutorial](https://www.youtube.com/watch?v=4Xe49jl5z5M&list=PLUbFnGajtZlUl0zYr4crGveP21BbcZG_L&index=56)

# Future Work

* Create a distinction between messages received and sent
* Ignore duplicate messages
* Terminate connection in a cleaner way