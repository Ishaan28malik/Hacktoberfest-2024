/* Created by pycrash */

/* Socket programming in c to implement client server paradigm, this program offers mainly two functionalities -
chatting among server and client using sockets,
and sending files from client to server */

/*
provide three arguments
filename server_ip_address port_no

argv[0] filename
argv[1] server_ip_address
argv[2] port_no

*/

/*Client Model should have following functions
1) Socket
2) Connect
3) Write
4) Read
5) close
*/

	//Contains declarartions for input and output
#include <stdio.h>
	//Defines 4 variable types, several macros and various functions
	//We will use atoi function to convert the string pointed to, by the argument to an integer
#include <stdlib.h>
	//defines one variable type, one macro, and various functions for manipulating arrays of characters
#include <string.h>
	//for read, write and close
#include <unistd.h>
	//conatins definitions of a no. of data types used in system calls
#include <sys/types.h>
	//contains constants and structures needed for internet domain addresses e.g. sockaddr_in
#include <netinet/in.h>
	//definitions of structures needed for sockets e.g. defines sockaddr structure
#include <sys/socket.h>
	//contains definition of Hostent structure
#include <netdb.h>
	//declares several functions that are useful for testing and mapping characters.
#include <ctype.h>
	// defines the structure of the data returned by the function fstat() 
#include <sys/stat.h>
	//defines the following requests and arguments for use by the functions fcntl() and open()
#include <fcntl.h>
	//definitions for internet operations 
#include <arpa/inet.h>

//Error function to exit the program
void error(const char *msg)
{
	/*perror is an inbuilt function that interprets the error no. and outputs the
		output error description by using STDERR */

	perror(msg);
	exit(1);
}

int main(int argc, char *argv[])
{
	/*The user need to provide 3 arguments, first one the file name,
	second one -the ip address of server and lastly the port no. */

	//socketfd is file descriptor
	int socketfd, portno, n;

	//sockaddr_in gives internet address
	struct sockaddr_in serv_address;

	//hostent structure is used to store info about the host such as host name, an IPv4 address etc.
	struct hostent * server;
	int sourse_fd;

	//buffer will be transferred in a data stream
	char buffer[1024];

	//variables for operation - send file, chat etc.
	int operation, sub_operation;

	//file name variable
	char str[20];
	int file_name_len, read_len;

	//checking if user provided 3 arguments or not	
	if (argc < 3)
	{
		//Terminating the program as user didnt provide 3 arguments
		fprintf(stderr, "usage %s hostname port\n", argv[0]);
		exit(0);
	}

	//converting the string argument into an int
	portno = atoi(argv[2]);

	//socket function returns a file descriptor, if its less than 0 then there is an error opening socket
	/*socket function has 3 arguments, first one is domain, here we will use AF_INET which is an IPv4 protocol,
	second argument is type, we will use SOCK_STREAM as it for TCP protocol, If we were to use UDP protocl, we would have provide SOCK_DGRAM as second argument,
	third argument is protocol, which is 0 for TCP */
	socketfd = socket(AF_INET, SOCK_STREAM, 0);

	if (socketfd < 0)
	{
		//File descrpitor is less than 0, error opening socket
		error("Error opening socket");
	}

	//getting info about host
	server = gethostbyname(argv[1]);
	if (server == NULL)
	{
		//server is null, no host exists
		fprintf(stderr, "No such host exists");
	}

	//bzero clears data or anything in whatever it is refrenced to
	//clearing serv_address so as to do operations on it 
	bzero((char*) &serv_address, sizeof(serv_address));

	/*getting info such as port, using htons - host to network short,
	converts port no. in host byte order to port no. in network byte order */
	serv_address.sin_family = AF_INET;
	bcopy((char*) server->h_addr, (char*) &serv_address.sin_addr.s_addr, server->h_length);
	serv_address.sin_port = htons(portno);

	//conneting to host, if file descriptor is less than 0, then the operation failed
	if (connect(socketfd, (struct sockaddr *) &serv_address, sizeof(serv_address)) < 0)
		error("connection Failed");

	//clearing everything in the output buffer of a stream
	fflush(stdout);

	//Asking user what he wants to do
	printf("What do you want me to do ?\n 1) Send File\n 2) Chat with server \nPress other key to terminate\n ");
	//getting user input
	scanf("%d", &operation);

	//we will send this operation no. to server, so that server can execute operations accordingly
	int number_to_send;
	fflush(stdout);
	number_to_send = operation;
	int converted_number = htonl(number_to_send);

	// Telling the server about the operation using write, there is a corresponding read in the server
	write(socketfd, &converted_number, sizeof(converted_number));

	//performing the operation according to user
	switch (operation)
	{
		case 1:
			//user selected send file
			{
			 	//asking user which type of file he/she wants to send
				bzero(str, 20);
				printf("Which type of file you want to send? \n1) Text file \n2) Image \n3) Audio \n4) Video \nPress any other key to terminate the program\n");

				//we will send this sub - operation no. to server, so that server can execute sub-operations accordingly
				scanf("%d", &sub_operation);
				int sub_number_to_send;

				//Telling the server about the sub - operation
				fflush(stdout);
				sub_number_to_send = sub_operation;
				int sub_converted_number = htonl(sub_number_to_send);

				// Telling the server about the sub-operation
				write(socketfd, &sub_converted_number, sizeof(sub_converted_number));

				switch (sub_operation)
				{
				 		//performing the sub operation according to user
					case 1:
						{
						 	//User selected txt file
							//asking the user, the name of the file he wants to send
							//Note : The file should be in the same directory as this client.c file
							printf("Type the name of your file that you want to send with the extension. Make sure that the file is in same directory as this file\n");

							//clearing everything in str, so as to save the file name in str
							//we will send this file name to server
							bzero(str, 20);
							scanf("%s", str);
							n = write(socketfd, str, strlen(str));

							//Starting the operation to send the txt file
							FILE * f;

							int words = 0;
							char c;
							f = fopen(str, "r");
							while ((c = getc(f)) != EOF)
							//Counting No of words in the file
							{
								fscanf(f, "%s", buffer);
								if (isspace(c) || c == '\t')
									words++;
							}
							//For printing the no. of words
							//printf("Words = %d \n", words);	

							write(socketfd, &words, sizeof(int));
							rewind(f);

							// tells size of the file. Not required for the functionality in code.      
							/*
							fseek(f, 0L, SEEK_END);    	
							int sz = ftell(f);				
							printf("Size is %d \n", sz);
         						rewind(f);  
							*/

							char ch;
							/*
							On getting EOF (or error) from standard input, the client Stdin process, before it exits, needs to tell
							the server that the client is done and there is nothing more coming down
							the socket.  The client has to signal "EOF" to the server.
							*/
							//So we will keep sending the file through buffer until EOF is encountered
							while (ch != EOF)
							{

								fscanf(f, "%s", buffer);
								//For printing every word in the file
								//printf("%s\n", buffer);	
								write(socketfd, buffer, 512);
								ch = fgetc(f);
							}
							//The operation executed successfully
							//The file was sent successfully
							printf("The file was sent successfully\n");
							break;
						}
					case 2:

						{

							/*memset copies the character 0 (an unsigned char) to the first 1024 characters of the string pointed to, by the argument buffer*/
							memset(buffer, 0x00, 1024);

							//User selected img file
							//asking the user, the name of the file he wants to send
							//Note : The file should be in the same directory as this client.c file
							printf("Type the name of your image that you want to send with the extension. Make sure that the file is in same directory as this file\n");
							scanf("%s", buffer);
							printf("Sending your Image\n");
							file_name_len = strlen(buffer);

							//sending file name to server
							send(socketfd, buffer, file_name_len, 0);

							//opening the file in the buffer for reading
							sourse_fd = open(buffer, O_RDONLY);
							if (!sourse_fd)
							{
							 					//error opening the file
								perror("Error reading file");
								return 1;
							}

							while (1)
							{

								//reading the file and then sending it through buffer, if read_len is 0 then there is nothing to send and the loop gets terminated
								memset(buffer, 0x00, 1024);
								read_len = read(sourse_fd, buffer, 1024);
								send(socketfd, buffer, read_len, 0);
								if (read_len == 0)
								{
									break;
								}
							}
							//Image was sent successfully
							printf("Image sent\n");
							break;
						}
					case 3:
						{
						 	/* memset copies the character 0 (an unsigned char) to the first 1024 characters of the string pointed to, by the argument buffer*/
							memset(buffer, 0x00, 1024);

							//User selected audio file
							//asking the user, the name of the file he wants to send
							//Note : The file should be in the same directory as this client.c file
							printf("Type the name of your file that you want to send with the extension. Make sure that the file is in same directory as this file\n");
							scanf("%s", buffer);
							printf("Sending your audio file\n");
							file_name_len = strlen(buffer);

							//sending file name to server
							send(socketfd, buffer, file_name_len, 0);

							//opening the file in the buffer for reading
							sourse_fd = open(buffer, O_RDONLY);
							if (!sourse_fd)
							{
							 	//error opening the file
								perror("Error : ");
								return 1;
							}

							while (1)
							{
							 	//reading the file and then sending it through buffer, if read_len is 0 then there is nothing to send and the loop gets terminated
								memset(buffer, 0x00, 1024);
								read_len = read(sourse_fd, buffer, 1024);
								send(socketfd, buffer, read_len, 0);
								if (read_len == 0)
								{
									break;
								}
							}
							//Audio file was sent successfully
							printf("Audio sent\n");
							break;
						}
					case 4:
						{
						 	/* memset copies the character 0 (an unsigned char) to the first 1024 characters of the string pointed to, by the argument buffer */
							memset(buffer, 0x00, 1024);

							//User selected video file
							//asking the user, the name of the file he wants to send
							//Note : The file should be in the same directory as this client.c file
							printf("Type the name of your file that you want to send with the extension. Make sure that the file is in same directory as this file\n");
							scanf("%s", buffer);

							printf("Sending your video file\n");
							file_name_len = strlen(buffer);

							//sending file name to server
							send(socketfd, buffer, file_name_len, 0);

							//opening the file in the buffer for reading
							sourse_fd = open(buffer, O_RDONLY);
							if (!sourse_fd)
							{
							 	//error opening the file
								perror("Error : ");
								return 1;
							}

							while (1)
							{
							 	//reading the file and then sending it through buffer, if read_len is 0 then there is nothing to send and the loop gets terminated
								memset(buffer, 0x00, 1024);
								read_len = read(sourse_fd, buffer, 1024);
								send(socketfd, buffer, read_len, 0);
								if (read_len == 0)
								{
									break;
								}
							}
							//Video file was sent successfully
							printf("Video sent\n");
							break;
						}
					default:
						exit(0);
				}
				break;
			}
		case 2:
			//user selected chat with server
			//lets have a chat then
			while (1)
			{

				//clearing buffer as will stream data through buffer only
				fflush(stdout);
				bzero(buffer, 1024);

				//fgets reads a line from the specified stream and stores it into the string pointed to by buffer.
				fgets(buffer, 1024, stdin);

				//sending whatever is in buffer to sever
				n = write(socketfd, buffer, strlen(buffer));

				if (n < 0)
					//file descriptor returns -1 which means write failed
					error("Error Writing");

				//again clearing buffer for reading data from server
				bzero(buffer, 512);
				//reading data from server
				n = read(socketfd, buffer, 1024);
				if (n < 0)
				{
				 		//file descriptor returns -1 which means read failed
					error("Error reading");
				}
				printf("Server: %s\n", buffer);

				//Server or client can anytime close the chat with keyword "Bye"
				int i = strncmp("Bye", buffer, 3);
				if (i == 0)
					break;
			}
			break;

		default:
			//user entered other keyword, so we have to terminate the program 
			printf("Other key entered, terminating");
			exit(0);
	}

	//closing the socket

	close(socketfd);
	return 0;
}
