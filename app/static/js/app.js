// ===============================
// SIDEBAR MOBILE
// ===============================

function openSidebar() {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");

    if (sidebar && overlay) {
        sidebar.classList.remove("-translate-x-full");
        overlay.classList.remove("hidden");
    }
}

function closeSidebar() {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");

    if (sidebar && overlay) {
        sidebar.classList.add("-translate-x-full");
        overlay.classList.add("hidden");
    }
}


// ===============================
// SIDEBAR DESKTOP MINIMIZABLE
// ===============================

function toggleCollapseSidebar() {
    const sidebar = document.getElementById("sidebar");
    const sidebarTitle = document.getElementById("sidebar-title");
    const navTexts = document.querySelectorAll(".nav-text");
    const footerTexts = document.querySelectorAll(".sidebar-footer-text");

    if (!sidebar) return;

    sidebar.classList.toggle("md:w-72");
    sidebar.classList.toggle("lg:w-80");
    sidebar.classList.toggle("md:w-20");

    if (sidebarTitle) {
        sidebarTitle.classList.toggle("hidden");
    }

    navTexts.forEach(text => {
        text.classList.toggle("hidden");
    });

    footerTexts.forEach(text => {
        text.classList.toggle("hidden");
    });
}


// ===============================
// INPUT PDF - NOMBRE ARCHIVO
// ===============================

function updateFileName(input) {
    const fileName = document.getElementById("fileName");
    const fileButton = document.getElementById("fileButton");
    const fileButtonText = document.getElementById("fileButtonText");

    if (!fileName || !fileButton || !fileButtonText) return;

    if (input.files.length > 0) {
        fileName.textContent = input.files[0].name;
        fileName.classList.remove("text-gray-500");
        fileName.classList.add("text-green-700");

        fileButton.classList.remove("border-gray-300", "text-gray-700", "hover:bg-gray-100");
        fileButton.classList.add("border-green-500", "bg-green-50", "text-green-700", "hover:bg-green-100");

        fileButtonText.textContent = "Factura seleccionada";
    } else {
        fileName.textContent = "Ningún archivo seleccionado";
        fileName.classList.remove("text-green-700");
        fileName.classList.add("text-gray-500");

        fileButton.classList.remove("border-green-500", "bg-green-50", "text-green-700", "hover:bg-green-100");
        fileButton.classList.add("border-gray-300", "text-gray-700", "hover:bg-gray-100");

        fileButtonText.textContent = "Elegir factura PDF";
    }
}



<script src="{{ url_for('static', path='js/app.js') }}"></script>