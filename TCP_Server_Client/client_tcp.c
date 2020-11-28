#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netdb.h> 
#include <netinet/in.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include <string.h>
#define PORT 8080 
#define SA struct sockaddr 


void rs(int sockfd){   //read and send
    
  FILE *dane;
     char buff[10000];
    while(1){
    dane = fopen ("output.json", "r");
    fscanf(dane,"%s", buff);
    sleep(1);
    printf("Hear_Rate: %s\n", buff);
    write(sockfd, buff, sizeof(buff)); 
    bzero(buff, sizeof(buff));
    fclose(dane);
    }


}



 int main(){
     int sockfd, connfd; 
    struct sockaddr_in servaddr, cli; 
  
    // socket create and varification 
    sockfd = socket(AF_INET, SOCK_STREAM, 0); 
    if (sockfd == -1) { 
        printf("socket creation failed...\n"); 
        exit(0); 
    } 
    else
        printf("Socket successfully created..\n"); 
    bzero(&servaddr, sizeof(servaddr)); 
    //Getting an ip address from user
    int i;
    char ip_addr[i];
    printf("IPv4 address of Server: \n");
    scanf("%s", &ip_addr);

    if(i<6 && i>15)
        {
            printf("Wrong IPv4 format:::::::ERROR \n");
            printf("Try again: ");
            scanf("%s",&ip_addr);

        }
        else{
     



    // assign IP, PORT 
    servaddr.sin_family = AF_INET; 
    servaddr.sin_addr.s_addr = inet_addr(&ip_addr); 
    servaddr.sin_port = htons(PORT); 
  
    // connect the client socket to server socket 
    if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) { 
        printf("connection with the server failed...\n"); 
        exit(0); 
    } 
    else
        printf("connected to the server..\n"); 
  
    // function for chat 
    rs(sockfd); 
  
    // close the socket 
    close(sockfd); 
        }

 }
