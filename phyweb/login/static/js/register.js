function validate() {
	const username = document.forms["RegisterForm"]["username"].value;
	const email = document.forms["RegisterForm"]["email"].value;
	const password1 = document.forms["RegisterForm"]["password"].value;
	const password2 = document.forms["RegisterForm"]["confirm_password"].value;

	const errors = document.getElementById("errors");

	const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;


	if(username.length < 5){
		errors.innerHTML = "<li>Username is to short</li>";		
	}
	if(username.length > 20){
		errors.innerHTML = "<li>Username is to long</li>";		
	}
	if(password1.length < 8){
		errors.innerHTML = "<li>Password is to short</li>";
	}
	if(password1.length > 128){
		errors.innerHTML = "<li>Password is to long</li>";
	}

	if(password1 != password2){
		errors.innerHTML = "<li>Passwords doesn't match</li>";
	}
	if(!re.test(email)){
		errors.innerHTML = "<li>Email is not valid</li>";
	}
	else{
		RegisterForm.submit()	
	}
}
GASH