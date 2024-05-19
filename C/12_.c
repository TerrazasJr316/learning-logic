#include <stdio.h>

int noDigitos(int n1);

int main () {

    int n1, ctr;

    printf("\n\n contar los digitos que se obtienen: \n");
    printf("-----------------------------------------\n");

    printf("Ingresa un numero: ");
    scanf("%d", &n1);

    ctr = noDigitos(n1);

    printf("El numero de digitos es: %d \n\n", ctr);

    return 0;
}

int noDigitos(int n1){

    static int ctr = 0;

    if(n1 != 0){
        
    }
}