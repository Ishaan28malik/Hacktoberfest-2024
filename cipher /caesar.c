#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void encrypt(char *a, int key)
{
    int i;
    for (i = 0; i < strlen(a); i++)
    {
        a[i] = (a[i] - 65 + key) % 26;
    }
    for (i = 0; i < strlen(a); i++)
    {
        a[i] = a[i] + 65;
    }
    for (i = 0; i < strlen(a); i++)
        printf("%c", a[i]);
    printf("\n");
}

void decrypt(char *a, int key)
{

    int i;
    for (i = 0; i < strlen(a); i++)
    {
        a[i] = (a[i] - key - 65) % 26;
    }
    for (i = 0; i < strlen(a); i++)
    {
        a[i] = a[i] + 65;
    }
    for (i = 0; i < strlen(a); i++)
        printf("%c", a[i]);

    printf("\n");
}

void main()
{
    char a[100];
    int key;
    printf("enter the text");
    scanf("%s", a);
    printf("enter the key");
    scanf("%d", &key);
    encrypt(a, key);
    decrypt(a, key);
}
