function togglePasswordVisibility(page_a_changer) {
    var passwordInputLogin = document.getElementById("passwordLogin");
    var togglePasswordLogin = document.getElementById("togglePasswordLogin");
    var passwordInputInscription = document.getElementById("passwordInscription");
    var togglePasswordInscription = document.getElementById("togglePasswordInscription");
    if (page_a_changer === "login"){
        if (passwordInputLogin.type === "password") {
            passwordInputLogin.type = "text";
            togglePasswordLogin.src = "../static/img/oeilOuvert.png";
        }
        else {
            passwordInputLogin.type = "password";
            togglePasswordLogin.src = "../static/img/oeilFerme.png";
        }
    }
    else{
        if (passwordInputInscription.type === "password") {
            passwordInputInscription.type = "text";
            togglePasswordInscription.src = "../static/img/oeilOuvert.png";
        }
        else {
            passwordInputInscription.type = "password";
            togglePasswordInscription.src = "../static/img/oeilFerme.png";
        }
    }
}
