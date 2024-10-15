#include <stdio.h>

int main() {

    int i, n, c=0;

    printf("Ingresa un número: ");
    scanf("%d", &n);

    for(i = 1; i <= n; i++){
        if(n % i == 0){
            c++
        }
    }
    if(c == 2){
        printf("Es numero primo");
    }
    else{
        printf("No es numero primo");
    }
}