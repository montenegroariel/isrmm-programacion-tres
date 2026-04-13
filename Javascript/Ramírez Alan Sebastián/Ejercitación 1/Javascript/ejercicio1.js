function filtrarPares(listaNumeros) {
    let pares = [];
    for (let i = 0; i < listaNumeros.length; i++) {
        let numeroActual = listaNumeros[i];
        if (numeroActual % 2 === 0) {
            pares.push(numeroActual);
        }
    }
    return pares;
}