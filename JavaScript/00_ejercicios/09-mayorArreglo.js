/* Escribe una función que retorne el numero mayor de un arreglo, sin utilizar ningun método. */

function numeroMayor(aarreglo) {
    let numMayor = aarreglo[0];

    for(let i = 0; i < aarreglo.length; i++) {
        if (aarreglo[i] > numeroMayor){
        }
    }
    return numMayor;
}

const numero = [3, 5, 7, 2, 8, 1];
console.log(numeroMayor(numero));
