/*
Escribe una función que retorne la suma de los numeros del 1 al 10.
*/

function sumarNumeros() {
    let suma = 0
    for (let i = 1; i <= 10; i++) {
        suma += i
    }
    return suma
}

console.log(sumarNumeros())