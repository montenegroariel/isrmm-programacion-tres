/**
 * Filtra y retorna solo los números pares de un array
 * @param {number[]} array
 * @returns {number[]}
 */
function numerosPares(array) {
  // Array.prototype.filter:
  // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
  return array.filter(num => num % 2 === 0); // num % 2 === 0 → condición de número par
}

/**
 * Cuenta la cantidad de veces que aparece cada palabra en un texto
 * @param {string} texto
 * @returns {Object} { palabra: cantidad }
 */
function contadorPalabras(texto) {
  const limpio = texto
    .toLowerCase() 
    // String.prototype.toLowerCase:
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase

    .replace(/[.,!?¿?]/g, "");
    // String.prototype.replace:
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/replace
    // Elimina signos de puntuación usando una expresión regular

  const palabras = limpio.split(/\s+/);
  // String.prototype.split:
  // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/split
  // Divide el texto en palabras usando espacios (uno o más)

  const resultado = {}; // Objeto donde se acumulan los conteos

  palabras.forEach(palabra => {
    // Array.prototype.forEach:
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach

    if (palabra) { // Evita strings vacíos
      // Si la palabra ya existe, suma 1; si no, inicializa en 1
      resultado[palabra] = (resultado[palabra] || 0) + 1;
      // Operador OR (||):
      // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/Logical_OR
    }
  });

  return resultado;
}

/**
 * Procesa un carrito de productos y retorna:
 * - total general
 * - producto más caro
 * - resumen con subtotales
 * @param {Array} productos [{nombre, precio, cantidad}]
 * @returns {Object}
 */
function carrito(productos) {
  let total = 0;
  let productoMasCaro = "";
  let maxPrecio = 0;
  const resumen = [];

  productos.forEach(p => {
    // Array.prototype.forEach:
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach

    const subtotal = p.precio * p.cantidad; // cálculo por producto
    total += subtotal; // acumulador total

    // Determina el producto con mayor precio unitario
    if (p.precio > maxPrecio) {
      maxPrecio = p.precio;
      productoMasCaro = p.nombre;
    }

    // Array.prototype.push:
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/push
    resumen.push({
      nombre: p.nombre,
      subtotal: subtotal
    });
  });

  // Retorna un objeto con propiedades resumidas
  return {
    total,
    productoMasCaro,
    resumen
  };
}

/**
 * Función principal que ejecuta el ejercicio seleccionado desde la UI
 */
function runExercise() {
  // document.getElementById:
  // https://developer.mozilla.org/es/docs/Web/API/Document/getElementById
  const input = document.getElementById("inputData").value;
  const exercise = document.getElementById("exercise").value;
  const output = document.getElementById("output");

  try {
    let result;

    if (exercise === "1") {
      // JSON.parse:
      // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse
      const data = JSON.parse(input);
      result = numerosPares(data);

    } else if (exercise === "2") {
      result = contadorPalabras(input);

    } else if (exercise === "3") {
      const data = JSON.parse(input);
      result = carrito(data);
    }

    // JSON.stringify:
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify
    // null, 2 → formatea con indentación de 2 espacios
    output.textContent = JSON.stringify(result, null, 2);

  } catch (error) {
    // Manejo de errores (por ejemplo JSON mal formado)
    output.textContent = "Error en los datos de entrada";
  }
}
