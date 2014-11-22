#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    fp = fopen("test_dir", "r");
    if (!fp) {
        perror("Error: ");
        return(-1);
    } else {
        printf("%s", "directory opened!");
    }
    fclose(fp);
    return(0);
}
