function ejecutarEjercicios() {
    var entrada = document.getElementById("inputDatos").value;
    var salidaTexto = "";

    try {
        var datos = JSON.parse(entrada);

        // Ejercicio 1
        if (Array.isArray(datos) && typeof datos[0] === "number") {
            var resultado1 = numerosPares(datos);
            salidaTexto = "Ejercicio 1:\n" + JSON.stringify(resultado1);
        }

        // Ejercicio 3
        else if (Array.isArray(datos) && typeof datos[0] === "object") {
            var resultado3 = carritoCompras(datos);
            salidaTexto = "Ejercicio 3:\n" + JSON.stringify(resultado3);
        }

    } catch (e) {
        // Ejercicio 2
        var resultado2 = contarPalabras(entrada);
        salidaTexto = "Ejercicio 2:\n" + JSON.stringify(resultado2);
    }

    document.getElementById("salida").textContent = salidaTexto;
}


// Ejercicio 1 
function numerosPares(array) {
    var pares = [];

    for (var i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            pares.push(array[i]);
        }
    }

    return pares;
}


//  Ejercicio 2 
function contarPalabras(texto) {
    texto = texto.toLowerCase();
    texto = texto.replace(".", "");
    texto = texto.replace(",", "");
    texto = texto.replace("!", "");
    texto = texto.replace("?", "");

    var palabras = texto.split(" ");
    var contador = {};

    for (var i = 0; i < palabras.length; i++) {
        var palabra = palabras[i];

        if (palabra !== "") {
            if (contador[palabra]) {
                contador[palabra] = contador[palabra] + 1;
            } else {
                contador[palabra] = 1;
            }
        }
    }

    return contador;
}


//Ejercicio 3 
function carritoCompras(productos) {
    var total = 0;
    var productoMasCaro = productos[0];
    var resumen = [];

    for (var i = 0; i < productos.length; i++) {
        var prod = productos[i];

        var subtotal = prod.precio * prod.cantidad;
        total = total + subtotal;

        if (prod.precio > productoMasCaro.precio) {
            productoMasCaro = prod;
        }

        resumen.push({
            nombre: prod.nombre,
            subtotal: subtotal
        });
    }

    return {
        total: total,
        productoMasCaro: productoMasCaro.nombre,
        resumen: resumen
    };
}