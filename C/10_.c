#include <stdio.h>

int main () {
    int i, n, sum = 0;

    printf("Ingresa un numero: ");
    scanf("%d", &n);

    for(i = 1; i <= n  / 2; i++){
        if(n % i == 0){
            sum = sum + i;
            printf("%d \n", i);
        }
    }
    printf("suma es: %d \n", sum);

    if(sum == n){
        printf("Es un numero exacto");
    }
    else {
        printf("No es un numero exacto");
    }
}