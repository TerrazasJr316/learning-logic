/* Objetivo: Distancia euclídea.
/* Entrada : Dos puntos cartesianos.
/* Salida : Su distancia euclídea.
/*****************************************************/

#include <stdio.h>
#include <math.h>
void main() {
    double x1, y1, x2, y2;
    puts("\n ***** Distancia de dos puntos *****");
    printf("\n- Punto 1: x1 = ");
    scanf("%f", &x1);

    printf("\n- y1 = ");
    scanf("%f", &y1);

    printf("\n- Punto 2: x2 = ");
    scanf("%f", &x2);

    printf("\n- y2 = ");
    scanf("%f", &y2);

    x1 = x1 - x2;
    y1 = y1 - y2;

    printf("\n* La distancia es: %f\n", sqrtf( (x1*x1)+(y1*y1) ));
    puts("\n ***** FIN *****");
}