
document.addEventListener('DOMContentLoaded', function () {
    // Variable para indicar el estado de autenticación (puedes ajustarlo según tu lógica)
    var usuarioAutenticado = false;

    // Función para cargar dinámicamente el menú según la autenticación
    function cargarMenu() {
        // Obtén el contenedor del menú
        var menuContainer = document.getElementById('navbarNav');

        // Crear una lista de elementos de menú basada en el estado de autenticación
        var menuItems = [
            { text: 'Inicio', url: 'index.html' },
            { text: 'Nosotros', url: 'nosotros.html' },
            { text: 'Contacto', url: 'contacto.html' }
            
        ];

        // Si el usuario está autenticado, agrega elementos adicionales al menú
        if (usuarioAutenticado) {
            menuItems.push(
                { text: 'Tienda', url: 'tienda.html' },
                { text: 'Carrito', url: 'carrito.html' },
                { text: 'Registro', url: 'registro.html' },
                // Agrega otros elementos según sea necesario
            );
        }

        // Construye el HTML del menú
        var menuHTML = '<ul class="navbar-nav ml-auto">';
        menuItems.forEach(function (item) {
            menuHTML += `<li class="nav-item"><a class="nav-link" href="${item.url}">${item.text}</a></li>`;
        });
        menuHTML += '</ul>';

        // Inserta el HTML del menú en el contenedor
        menuContainer.innerHTML = menuHTML;
    }

    // Llama a la función al cargar la página
    cargarMenu();

    // Puedes cambiar el estado de autenticación y llamar a la función según sea necesario
    // Por ejemplo, si el usuario inicia sesión correctamente
    // usuarioAutenticado = true;
    // cargarMenu();
});
