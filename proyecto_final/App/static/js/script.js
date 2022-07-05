// INPUT de validacion por e-mail
// FRONTEND form
function validateEmail(email){
    regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validateForm() {
    const nombre = document.getElementById("nombre").value;
    const edad = document.getElementById("edad").value;
    const telefono = document.getElementById("telefono").value;
    const email = document.getElementById("email").value;
    const Personal = document.getElementById("Personal").value;
    const Experiencia = document.getElementById("Experiencia").value;
    const archivo = document.getElementById("archivo ").value;

    if (nombre == "") {
        swal("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (nombre.split(" ").lenght < 2) {
        swal("Se requiere tu nombre completo","ERROR");
        return false;
    }
    
    else if (telefono == "") {
        swal("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (email == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (Personal == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (Experiencia == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (archivo == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else {
        return true;
    }
}


// INPUT de validacion BACKEND form
function validateEmail2(email){
    regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email2);
}

function validateForm2() {
    const nombre = document.getElementById("nombre2").value;
    const edad = document.getElementById("edad2").value;
    const telefono = document.getElementById("telefono2").value;
    const email = document.getElementById("email2").value;
    const Personal = document.getElementById("Personal2").value;
    const Experiencia = document.getElementById("Experiencia2").value;
    const archivo = document.getElementById("archivo2").value;

    if (nombre2 == "") {
        swal("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (nombre2.split(" ").lenght < 2) {
        swal("Se requiere tu nombre completo","ERROR");
        return false;
    }
    
    else if (telefono2 == "") {
        swal("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (email2 == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (Personal2 == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (Experiencia2 == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (archivo2 == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else {
        return true;
    }
}

// INPUT de validacion CIBERSGURIDAD form
function validateEmail3(email){
    regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email3);
}

function validateForm3() {
    const nombre = document.getElementById("nombre3").value;
    const edad = document.getElementById("edad3").value;
    const telefono = document.getElementById("telefono3").value;
    const email = document.getElementById("email3").value;
    const Personal = document.getElementById("Personal3").value;
    const Experiencia = document.getElementById("Experiencia3").value;
    const archivo = document.getElementById("archivo3").value;

    if (nombre3 == "") {
        swal("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (nombre3.split(" ").lenght < 2) {
        swal("Se requiere tu nombre completo","ERROR");
        return false;
    }
    
    else if (telefono3 == "") {
        swal("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (email3 == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (Personal3 == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (Experiencia3 == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else if (archivo3 == "") {
        swal ("Este campo no puede quedar vacío","ERROR");
        return false;
    }

    else {
        return true;
    }
}