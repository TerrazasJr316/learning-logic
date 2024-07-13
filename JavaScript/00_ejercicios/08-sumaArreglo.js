/*
Escribe una función que retorne la suma de todos los elementos de un arreglo
*/

function sumaArreglo(arr) {
    let suma = 0
    for (let i = 0; i < arr.length; i++) {
        suma += arr[i]
    }
    return suma
}

const arreglo = [1,2,3,4,5]
console.log(sumaArreglo(arreglo))