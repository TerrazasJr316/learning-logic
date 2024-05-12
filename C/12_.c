#include <stdio.h>

int noDigitos(int n1);

int main () {

    int n1, ctr;

    printf("\n\n contar los digitos que se obtienen: \n");
    printf("-----------------------------------------\n");

    printf("Ingresa un numero: ");
    scanf("%d", &n1);

    ctr = noDigitos(n1);
}