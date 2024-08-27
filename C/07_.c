#include <stdio.h>

void printable();

int main() {
    int n;

    print("Ingresa un numero: ");
    scanf("%d", &n);
    printable(n);

    return 0;
}

void printable() {
    for (int i = 1; i <= 10; i++) {
        printf("%d \n", i * n);
    }
}