function obtenerNumerosPares(arreglo) {
  return arreglo.filter(function (numero) {
    return numero % 2 === 0;
  });
}

function contarPalabras(texto) {
  var textoLimpio = texto
    .toLowerCase()
    .replace(/[.,!¿?¡;:()"]/g, " ");

  var palabras = textoLimpio.split(/\s+/).filter(function (palabra) {
    return palabra.length > 0;
  });

  var resultado = {};

  palabras.forEach(function (palabra) {
    if (!resultado[palabra]) {
      resultado[palabra] = 0;
    }
    resultado[palabra] += 1;
  });

  return resultado;
}

function resolverCarrito(productos) {
  var total = 0;
  var productoMasCaro = null;
  var resumen = [];

  productos.forEach(function (producto) {
    var subtotal = producto.precio * producto.cantidad;
    total += subtotal;

    if (productoMasCaro === null || producto.precio > productoMasCaro.precio) {
      productoMasCaro = producto;
    }

    resumen.push({
      nombre: producto.nombre,
      subtotal: subtotal
    });
  });

  return {
    total: total,
    productoMasCaro: productoMasCaro ? productoMasCaro.nombre : null,
    resumen: resumen
  };
}

var selectEjercicio = document.getElementById("ejercicio");
var campoEntrada = document.getElementById("entrada");
var campoSalida = document.getElementById("salida");
var botonEjecutar = document.getElementById("btn-ejecutar");

var ejemplos = {
  1: "[1, 2, 3, 4, 5, 6]",
  2: "hola mundo hola",
  3: '[{"nombre":"camisa","precio":20,"cantidad":2},{"nombre":"pantalon","precio":40,"cantidad":1},{"nombre":"gorra","precio":10,"cantidad":3}]'
};

function actualizarPlaceholder() {
  var ejercicio = selectEjercicio.value;
  campoEntrada.placeholder = "Ejemplo: " + ejemplos[ejercicio];
  campoEntrada.value = "";
  campoSalida.textContent = "Esperando datos...";
}

function ejecutarEjercicio() {
  var ejercicio = selectEjercicio.value;
  var textoEntrada = campoEntrada.value.trim();

  if (!textoEntrada) {
    campoSalida.textContent = "Error: ingresá datos en la entrada.";
    return;
  }

  try {
    if (ejercicio === "1") {
      var arreglo = JSON.parse(textoEntrada);
      if (!Array.isArray(arreglo)) {
        throw new Error("La entrada debe ser un array.");
      }
      arreglo.forEach(function (item) {
        if (typeof item !== "number") {
          throw new Error("Todos los elementos del array deben ser números.");
        }
      });

      var salidaPares = obtenerNumerosPares(arreglo);
      campoSalida.textContent = JSON.stringify(salidaPares, null, 2);
    }

    if (ejercicio === "2") {
      var salidaConteo = contarPalabras(textoEntrada);
      campoSalida.textContent = JSON.stringify(salidaConteo, null, 2);
    }

    if (ejercicio === "3") {
      var productos = JSON.parse(textoEntrada);
      if (!Array.isArray(productos)) {
        throw new Error("La entrada debe ser un array de productos.");
      }

      productos.forEach(function (producto) {
        if (
          typeof producto.nombre !== "string" ||
          typeof producto.precio !== "number" ||
          typeof producto.cantidad !== "number"
        ) {
          throw new Error("Cada producto debe tener nombre (string), precio (number) y cantidad (number).");
        }
      });

      var salidaCarrito = resolverCarrito(productos);
      campoSalida.textContent = JSON.stringify(salidaCarrito, null, 2);
    }
  } catch (error) {
    campoSalida.textContent = "Error: " + error.message;
  }
}

selectEjercicio.addEventListener("change", actualizarPlaceholder);
botonEjecutar.addEventListener("click", ejecutarEjercicio);

actualizarPlaceholder();
