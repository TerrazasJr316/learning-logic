#include <stdio.h>

int main() {

    int i, n;
    printf("Ingresa un número: ");
    scanf("%d", &n);

    i = 1;

    while(i <= n){
        printf("%d \n", i);
        i++;
    }
}