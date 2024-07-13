/*
Escribe una función para verificar si un numero es positivo, negativo o cero
*/


function verificarNumero(numero){
    if (numero > 0) {
        return "El numero es positivo"
    } else if (numero < 0){
        return "El numero es negativo"
    } else {
        return "El  numero es cer"
    }
}

console.log(verificarNumero(5))
console.log(verificarNumero(-3))
console.log(verificarNumero(0))