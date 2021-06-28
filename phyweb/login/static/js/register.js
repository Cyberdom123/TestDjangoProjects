function validate() {
	var username = document.forms["RegisterForm"]["username"].value;
	var phone = document.forms["RegisterForm"]["phone"].value;
	var email = document.forms["RegisterForm"]["email"].value;
	var password1 = document.forms["RegisterForm"]["password"].value;
	var password2 = document.forms["RegisterForm"]["confirm_password"].value;

	var errors = document.getElementById("errors");


	if(username == "" || phone == "" || email == "" || password1 == "" || password2 == ""){
	}else{
		alert("ojej!");
	}

	if(password1 != password2){
		errors.innerHTML = "Passowrds don't match";
	}else{
		alert("ok!");
	}

}