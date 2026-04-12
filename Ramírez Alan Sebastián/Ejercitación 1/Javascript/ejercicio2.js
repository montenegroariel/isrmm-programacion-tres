function contarPalabras(texto) {
    let textoLimpio = texto.toLowerCase();
    //Antes era textoLimpio 'textoLimpio = textoLimpio.replace(/[.,!¿?¡!]/g, "");'
    //...pero dejaba pasar cadenas de símbolos como "'', --, .., __" etc.

    textoLimpio = textoLimpio.replace(/[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]/g, "");

    let palabras = textoLimpio.split(/\s+/);

    let contador = {};

    for (let palabra of palabras) {
        if (palabra === "") continue;

        if (contador[palabra]) {
            contador[palabra]++;
        } else {
            contador[palabra] = 1;
        }
    }
    return contador;
}