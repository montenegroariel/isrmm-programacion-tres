const textarea = document.getElementById('entrada-datos');
const salida = document.getElementById('salida-datos');
const selector = document.getElementById('selector-ejercicio');

selector.addEventListener('change', () => {
    textarea.value = "";
    salida.innerText = "Esperando ejecución...";
    salida.style.color = "black";

    if (selector.value === "1") {
        textarea.placeholder = "Ejercicio 1: Escribe números, uno por línea...";
    } else if (selector.value === "2") {
        textarea.placeholder = "Ejercicio 2: Escribe una frase o texto libre...";
    } else if (selector.value === "3") {
        textarea.placeholder = "Ejercicio 3: Escribe -> Nombre, Precio, Cantidad (ej: Camisa, 20, 2)";
    }
});

document.getElementById('btn-ejecutar').addEventListener('click', () => {
    const ejercicioSeleccionado = selector.value;
    const valorRaw = textarea.value.trim();

    if (valorRaw === "") {
        salida.innerText = "Error: El campo está vacío.";
        salida.style.color = "red";
        return;
    }

    if (ejercicioSeleccionado === "1") {
        let lineas = valorRaw.split('\n');
        let numerosValidos = [];
        let error = false;

        for (let l of lineas) {
            let item = l.trim();
            if (item === "") continue;
            let num = Number(item);
            if (isNaN(num)) { error = true; break; }
            numerosValidos.push(num);
        }

        if (error) {
            salida.innerText = "Error: Solo números (uno por línea).";
            salida.style.color = "red";
        } else {
            salida.style.color = "black";
            ejecutarLogica("1", numerosValidos);
        }
    } 
    else if (ejercicioSeleccionado === "2") {
        salida.style.color = "black";
        ejecutarLogica("2", valorRaw);
    }
    else if (ejercicioSeleccionado === "3") {
        let lineas = valorRaw.split('\n');
        let productos = [];
        let error = false;

        for (let l of lineas) {
            let partes = l.split(',');
            if (partes.length !== 3) { error = true; break; }

            let nombre = partes[0].trim();
            let precio = Number(partes[1].trim());
            let cantidad = Number(partes[2].trim());

            if (isNaN(precio) || isNaN(cantidad)) { error = true; break; }
            productos.push({ nombre, precio, cantidad });
        }

        if (error) {
            salida.innerText = "Error: Formato incorrecto. Usa: nombre, precio, cantidad";
            salida.style.color = "red";
        } else {
            salida.style.color = "black";
            ejecutarLogica("3", productos);
        }
    }
});

function ejecutarLogica(opcion, datos) {
    let resultado;
    let titulo = "<strong>Resultado:</strong><br><br>";

    if (opcion === "1") {
        resultado = filtrarPares(datos);
        salida.innerHTML = titulo + resultado.join('\n');
    } 
    else if (opcion === "2") {
        resultado = contarPalabras(datos);
        let formatoVertical = titulo;
        for (let palabra in resultado) {
            formatoVertical += palabra + ": " + resultado[palabra] + "\n";
        }
        salida.innerHTML = formatoVertical;
    }
    else if (opcion === "3") {
        resultado = procesarProductos(datos);
        let textoFinal = titulo;
        textoFinal += `TOTAL A PAGAR: $${resultado.total}\n`;
        textoFinal += `PRODUCTO MÁS CARO: ${resultado.productoMasCaro}\n\n`;
        textoFinal += `RESUMEN:\n`;
        resultado.resumen.forEach(item => {
            textoFinal += `- ${item.nombre}: $${item.subtotal}\n`;
        });
        salida.innerHTML = textoFinal;
    }
}