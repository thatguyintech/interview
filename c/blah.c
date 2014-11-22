#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h> 
 
#include <sys/socket.h>
#include <netinet/in.h>
#include <fcntl.h>
#include <unistd.h>
#include <signal.h>
#include <dirent.h>

const char dir_listing_head[] = 
"<html>"
"<head>"
"<title>index of %s </title>"
"</head>"
"<body>"
"<h1> Index of %s</h1>"
"<table>"
"<tr> <th style='width:300px'> Name </th> <th style='width:300px'> Type </tr>"; 
    
int main() {
    char info_to_display[9999];
    sprintf(info_to_display,dir_listing_head, "hello", "bye");
    printf("%s\n", info_to_display);
    return 1;
}
