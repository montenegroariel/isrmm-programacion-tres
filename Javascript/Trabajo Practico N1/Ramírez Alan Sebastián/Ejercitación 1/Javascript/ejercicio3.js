function procesarProductos(listaDeObjetos) {
    let totalPagar = 0;
    let productoMasCaro = "";
    let precioMaximo = -1;
    let resumen = [];

    for (let prod of listaDeObjetos) {
        let subtotal = prod.precio * prod.cantidad;
        totalPagar += subtotal;

        if (prod.precio > precioMaximo) {
            precioMaximo = prod.precio;
            productoMasCaro = prod.nombre;
        }

        resumen.push({
            nombre: prod.nombre,
            subtotal: subtotal
        });
    }

    return {
        total: totalPagar,
        productoMasCaro: productoMasCaro,
        resumen: resumen
    };
}