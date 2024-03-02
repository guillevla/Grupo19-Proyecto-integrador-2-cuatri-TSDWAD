// Variable global para almacenar usuarios registrados
var usuarios = [];
console.log('Usuarios almacenados:', usuarios);

// Función de inicio de sesión de usuario
function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('passwordlogin').value;

    // Busca el usuario en el array de usuarios registrados
    var user = usuarios.find(user => user.username === username && user.password === password);

    if (user) {
        document.getElementById('login-message').innerText = '¡Inicio de sesión exitoso!';
        // Puedes hacer más acciones después del inicio de sesión
        window.location.href = 'dashboard.html';
    } else {
        document.getElementById('login-message').innerText = 'Credenciales incorrectas. Inténtalo de nuevo.';
    }
}

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
        
        document.getElementById('success-message').innerText = 'El usuario ' + nombre + ' se registró con éxito';
        setTimeout(function () {
            myModal.hide();
            // Limpia el formulario
            registroForm.reset();
            // Limpia el mensaje después de ocultar el modal
            document.getElementById('success-message').innerText = '';
            window.location.href = 'dashboard.html';
        }, 1000);
        // Cierra el modal
        //myModal.hide();
        //registroForm.reset();
        
    });

});

