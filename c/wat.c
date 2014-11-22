#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
    char **strings = (char**)malloc(5*sizeof(char*));
    int i = 0;
    for (i = 0; i < 5; i++) {
        printf("%d\n", i);
        strings[i] = (char*)malloc(50*sizeof(char));
    }
    strings[0] = "bird goes tweet";
    strings[1] = "mouste goes squeak";
    strings[2] = "cow goes moo";
    strings[3] = "frog goes croak";
    strings[4] = "what does the fox say?";

    for (i = 0; i < 5; i++) {
        printf("Line #%d(length: %lu): %s\n", i, strlen(strings[i]), strings[i]);
    }

    for (i = 0; i < 5; i++) {
        free(strings[i]);
    }

    free(strings);
    return 0;
}
