
var cname = document.getElementById("namee").value 

var email = document.getElementById("eemail").value

var password = document.getElementById("passwordd").value
var cpassword = document.getElementById("cpasswordd").value
var emailRegex = new RegExp("^(.+)@(.+)$")
var passRegex = new RegExp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$");
const form = document.getElementById("form")

form.addEventListener('submit',(e) => {
	if ( cname == "" ) {
		document.getElementById("nameErrorMsg").innerHTML = "Name field cannot be empty"
		e.preventDefault()
	}
	if (email == "") {
		document.getElementById("emailErrorMsg").innerHTML = "Email field cannot be empty"
		e.preventDefault()
	}
	if (password == "") {
		document.getElementById("pwErrorMsg").innerHTML = "Password field cannot be empty"
		e.preventDefault()
	}

	if (cpassword == "") {
		document.getElementById("cpwErrorMsg").innerHTML = "Confirm Password field cannot be empty"
		e.preventDefault()
	}

	if(password != cpassword){
		document.getElementById("cpwErrorMsg").innerHTML = "Password doesn't match"
		e.preventDefault()
	}

	else if (!passRegex.test(password)){
		document.getElementById("pwErrorMsg").innerHTML = "Passwords must be minimum of 8 characters at least 1 alphabet and 1 number"
		e.preventDefault()	
	}
	else if (!emailRegex.test(email)){
		document.getElementById("emailErrorMsg").innerHTML = "Please enter the valid email"
		e.preventDefault()	
	}
	else {
		alert("Successfully signed up");
		location.href = "/" ; 
	}
})


const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
