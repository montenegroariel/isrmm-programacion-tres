// Veamos algunas operaciones útiles en los arreglos,


const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'];

// Si quieres saber cuantos elementos hay un arreglo puedes utilizar la propiedad
console.log(meses.length);

// si tienes un carrito de compras y agregas o quitas elementos del carrito, el arreglo crece de forma dinamica, entonces, como acceder a todos los elementos? con algo llamado un iterador, y en javascript hay varios...

for (let i = 0; i < meses.length; i++) {
    console.log(meses[i]);
}