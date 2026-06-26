function obtenerPares(array) {
  return array.filter(num => num % 2 === 0);
}


function contarPalabras(texto) {
  const resultado = {};
  const limpio = texto
    .toLowerCase()
    .replace(/[.,!¿?]/g, "");

  const palabras = limpio.split(" ");

  palabras.forEach(palabra => {
    if (palabra) {
      resultado[palabra] = (resultado[palabra] || 0) + 1;
    }
  });

  return resultado;
}

function procesarCarrito(productos) {
  let total = 0;
  let productoMasCaro = productos[0];
  const resumen = [];

  productos.forEach(prod => {
    const subtotal = prod.precio * prod.cantidad;

    total += subtotal;

    if (prod.precio > productoMasCaro.precio) {
      productoMasCaro = prod;
    }

    resumen.push({
      nombre: prod.nombre,
      subtotal: subtotal
    });
  });

  return {
    total: total,
    productoMasCaro: productoMasCaro.nombre,
    resumen: resumen
  };
}



function ejecutar() {
  let ejercicio = document.getElementById("ejercicio").value;
  let entrada = document.getElementById("entrada").value;
  let salida = document.getElementById("salida");

  try {
    let resultado;

    if (ejercicio == "1") {
      let datos = JSON.parse(entrada);
      resultado = obtenerPares(datos);
    }

    if (ejercicio == "2") {
      resultado = contarPalabras(entrada);
    }

    if (ejercicio == "3") {
      let datos = JSON.parse(entrada);
      resultado = procesarCarrito(datos);
    }

    salida.textContent = JSON.stringify(resultado, null, 2);
  } catch (error) {
    salida.textContent = "Error en los datos ingresados";
  }
}
