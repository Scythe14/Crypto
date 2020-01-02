#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char        *rev_str(char *str)
{
    char    *begin;
    char    *end;
    char    tmp;

    begin = str;
    end = str + strlen(str) - 1;
    while (end > begin)
    {
        tmp = *end;
        *end-- = *begin;
        *begin++ = tmp;
    }
    return str;
}

int         find(char c, char *str)
{
    int       i;

    i = 0;
    while (str[i])
    {
        if (str[i] == c)
            return i;
        i++;
    }
    return i;
}

int         my_getnbr_base(char *str, char *base)
{
    int       res;
    int       l_base;
    int       l_str;
    int       fact;

    res = 1;
    fact = 1;
    l_base = strlen(base);
    l_str = strlen(str) - 1;
    while (l_str >= 0)
    {
        res = res + find(str[l_str], base) * fact;
        fact = l_base * fact;
        l_str = l_str - 1;
    }
    res -= 1;
    return res;
}

char            *convert_base(char *nbr, char *ib, char *ob)
{
    int           i;
    int           nb;
    char          *res;

    i = 0;
    if ((res = malloc(strlen(nbr) + (strlen(ib) * strlen(ob)))) == NULL)
        return (NULL);
    nb = my_getnbr_base(nbr, ib);
    while (nb > 0)
    {
        res[i] = ob[nb % strlen(ob)];
        nb = nb / strlen(ob);
        i += 1;
    }
    res[i] = '\0';
    res = rev_str(res);
    return res;
}
