// Variable global para almacenar usuarios registrados
var usuarios = [];
console.log('Usuarios almacenados:', usuarios);
// Función de registro de nuevo usuario
    document.addEventListener('DOMContentLoaded', function () {
        var myModal = new bootstrap.Modal(document.getElementById('registroModal'), {
            keyboard: false
        });

        document.getElementById('registroForm').addEventListener('submit', function (event) {
            event.preventDefault();
            var nombre = document.getElementById('nombre').value;
            var email = document.getElementById('email').value;
            var password = document.getElementById('passwordregistro').value;

            // Almacena los datos en el array global de usuarios
            usuarios.push({ username: nombre, email: email, password: password });
            
            // Puedes hacer más cosas aquí, como limpiar el formulario o mostrar un mensaje de éxito

            // Cierra el modal
            myModal.hide();
        });

        // Activa el modal cuando la página está completamente cargada
        myModal.show();
    });


// Función de inicio de sesión de usuario
function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('passwordlogin').value;

    // Busca el usuario en el array de usuarios registrados
    var user = usuarios.find(user => user.username === username && user.password === password);

    if (user) {
        document.getElementById('error-message').innerText = '¡Inicio de sesión exitoso!';
        // Puedes hacer más acciones después del inicio de sesión
        window.location.href = 'dashboard.html';
    } else {
        document.getElementById('error-message').innerText = 'Credenciales incorrectas. Inténtalo de nuevo.';
    }
}


