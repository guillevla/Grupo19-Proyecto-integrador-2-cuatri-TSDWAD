document.addEventListener('DOMContentLoaded', function () {
    // Obtén el enlace de "Cerrar sesión" por su ID o cualquier otro selector
    var logoutLink = document.querySelector('#logout');

    // Agrega un evento de clic al enlace
    logoutLink.addEventListener('click', function (event) {
        // Evita el comportamiento predeterminado del enlace
        event.preventDefault();

        // Muestra el modal de confirmación
        var confirmLogoutModal = new bootstrap.Modal(document.getElementById('confirmLogoutModal'));
        confirmLogoutModal.show();
    });

    // Obtén el botón de confirmar cierre de sesión del modal
    var confirmLogoutBtn = document.querySelector('#confirmLogoutBtn');

    // Agrega un evento de clic al botón de confirmar
    confirmLogoutBtn.addEventListener('click', function () {
        // Realiza las operaciones de cierre de sesión que necesites

        // Redirige al usuario a la página de inicio de sesión
        window.location.href = 'index.html';
    });
});