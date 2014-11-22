#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h> 

int main() {
    int result=1;
    int boolean=1;
    result = !boolean;
    if (!result) {
        printf("%s\n", "your theory worked");
    }

    return 1;
}
