function signUp(){
	var name = document.getElementById("namee").value 

	var email = document.getElementById("eemail").value
	
	var password = document.getElementById("passwordd").value
	var cpassword = document.getElementById("cpasswordd").value

	var emailRegex = new RegExp("^(.+)@(.+)$")
	var passRegex = new RegExp("^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,}))");
	if ( name == "" ) {
		document.getElementById("nameErrorMsg").innerHTML = "Name field cannot be empty"
		
	}
	if (email == "") {
		document.getElementById("emailErrorMsg").innerHTML = "Email field cannot be empty"
	}
	if (password == "") {
		document.getElementById("pwErrorMsg").innerHTML = "Password field cannot be empty"
	}

	if (cpassword == "") {
		document.getElementById("cpwErrorMsg").innerHTML = "Confirm Password field cannot be empty"
	}

	if(password != cpassword){
		document.getElementById("cpwErrorMsg").innerHTML = "Password doesn't match"
	}

	else if (!passRegex.test(password)){
		document.getElementById("pwErrorMsg").innerHTML = "Passwords must contain 1 capital, 1 small letter and 1 numeric field and total 8 chars"
		
	}
	else if (!emailRegex.test(email)){
		document.getElementById("emailErrorMsg").innerHTML = "Please enter the valid email"
		
	}
	else {
		alert("Successfully signed up");
		location.href = "/" ; 
	}
}


const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
