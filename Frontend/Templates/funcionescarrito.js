
// Obtener el carrito del almacenamiento local
let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

// Función para agregar un producto al carrito
function agregarAlCarrito(nombre, cantidad, precio) {
    const producto = {
        nombre: nombre,
        cantidad: cantidad,
        precio: precio
    };

    carrito.push(producto);
    mostrarMensaje('El producto seleccionado se ha agregado al carrito');

    // Puedes mostrar el contenido del carrito o realizar otras acciones aquí
    console.log(carrito);

    // Actualizar el carrito en el almacenamiento local
    actualizarCarrito();
}

function mostrarMensaje(mensaje) {
    // Crear un elemento para el mensaje
    const mensajeElemento = document.createElement('div');
    mensajeElemento.className = 'mensaje';
    mensajeElemento.textContent = mensaje;

    // Agregar el mensaje al DOM 
    document.body.appendChild(mensajeElemento);

    // Desaparecer el mensaje después de un tiempo
    setTimeout(() => {
        document.body.removeChild(mensajeElemento);
    }, 3000); // 3000 milisegundos = 3 segundos
}


// Función para mostrar el contenido del carrito
function mostrarCarrito() {
    const carritoContainer = document.getElementById('carrito-container');
    carritoContainer.innerHTML = '';

    if (carrito.length === 0) {
        carritoContainer.innerHTML = '<p>El carrito está vacío.</p>';
    } else {
        carrito.forEach(producto => {
            const productoHTML = `
                <div class="card mb-2">
                    <div class="card-body">
                        <h5 class="card-title">${producto.nombre}</h5>
                        <p class="card-text">Cantidad: ${producto.cantidad}</p>
                        <p class="card-text">Precio: $${producto.precio.toFixed(2)}</p>
                        <button class="btn btn-danger" onclick="eliminarDelCarrito('${producto.nombre}')">Eliminar</button>
                    </div>
                </div>
            `;
            carritoContainer.innerHTML += productoHTML;
        });
    }
}

// Función para eliminar un producto del carrito
function eliminarDelCarrito(nombre) {
    carrito = carrito.filter(producto => producto.nombre !== nombre);
    actualizarCarrito();
}

// Función para actualizar el carrito en el almacenamiento local
function actualizarCarrito() {
    localStorage.setItem('carrito', JSON.stringify(carrito));
    mostrarCarrito();
}

// Mostrar el carrito al cargar la página
mostrarCarrito();

 // Obtener el año actual
//document.getElementById('currentYear').textContent = new Date().getFullYear();

