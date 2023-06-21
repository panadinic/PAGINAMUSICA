
jQuery.validator.addMethod("nacimiento", function(value, element) {
    var fechaNacimiento = new Date(value);
    var fechaActual = new Date();
    return fechaNacimiento < fechaActual;
}, "La fecha de nacimiento debe ser menor que la fecha actual");

$("#frmRegistro").validate({
    debug: true,
    errorClass: "errorMessage",
    rules:{
        nombre:{
            required: true,
            minlength: 10
        },
        telefono: {
            required: true,
            minlength: 12
        },
        correo: {
            required: true,
            email: true
        },
        fechaNacimiento: {
            required: true,
            date: true,
            nacimiento: true
        },
        contrasena: {
            required: true
        },
        recontrasena: {
            equalTo: "#contrasena"
        }

    },
    messages: {
        nombre: {
            required: "El campo nombre no puede estar vacio.",
            minlength: jQuery.validator.format("El campo nombre debe tener como minimo {0} caracteres.")
        },
        telefono: {
            required: "El campo teléfono no puede estar vacio.",
            minlength: jQuery.validator.format("El campo teléfono debe tener un minimo de {0} caracteres."),
        },
        fechaNacimiento: {
            required: "El campo fecha de nacimiento es obligatorio.",
            date: "Ingrese una fecha válida.",
            nacimiento: "La fecha de nacimiento debe ser menor que la fecha actual."
        }
        
    }
});