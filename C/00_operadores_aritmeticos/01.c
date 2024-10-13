/**************************************************************/
/* Objetivo: Prueba y manejo de operadores aritméticos en C. */
/* Entrada : Dos valores enteros. */
/* Salida : Suma, Resta, Producto, División y Resto. */
/**************************************************************/
#include <stdio.h>
void main() {
    int x, y;

    puts("\n ***** Operaciones *****");
    printf("\n Dame un número entero: ");
    scanf("%i”,&x");

    printf("\nDame otro entero: ");
    scanf("%i",&y);

    printf("\nSuma : %i + %i = %i", x, y, x+y );

    printf("\nResta : %i - %i = %i", x, y, x-y );
    printf("\n %i - %i = %i", y, x, y-x );
    printf("\nProducto: %i * %i = %i", x, y, x*y );

    printf("\nDivisión: %i / %i = %f", x, y, x/(float)y );
    printf("\n %i / %i = %f", y, x, y/(float)x );
    
    printf("\nMódulo : %i %% %i = %i", x, y, x%y );
    printf("\n %i %% %i = %i", y, x, y%x );

    puts("\n ***** FIN *****");
}