/*
Escribe una función que imprima los números pares del 1 al 20
 */

function pares() {
    for (let i = 1; i <= 20; i++) {
        if (i % 2 === 0 ) {
            console.log(i)
        }
    }
}