jQuery.validator.addMethod("correoValido", function(value, element) {
    return this.optional(element) || /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|cl)$/i.test(value);
}, "Ingrese un correo electrónico válido");

$("#frmInicioSesion").validate({
    debug: true,
    errorClass: "errorMessage",
    rules:{
        correo: {
            required: true,
            email: true,
            correoValido: true
        },
        contrasena: {
            required: true
        }
    },
    messages: {
        correo: {
            required: "El campo correo electrónico no puede estar vacío.",
            email: "Ingrese un correo electrónico válido.",
            correoValido: "Ingrese un correo electrónico válido que termine en .com o .cl."
        },
        contrasena: {
            required: "El campo contraseña no puede estar vacío."
        }
    }
});
