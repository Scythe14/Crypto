#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int     main(int ac, char **av)
{
    char *s1 = "\1c\01\11\00\1f\01\01\00\06\1a\02\4b\53\53\50\09\18\1c";
    char *s2 = "\68\69\74\20\74\68\65\20\62\75\6c\6c\27\73\20\65\79\65";

    const char* f = s1;
    const char* x = s2;

    while (*s2) {
        printf("%02x", *s1 ^ *s2);
        ++s1;
        ++s2;
    }
    printf("\n");
    return 0;
}
