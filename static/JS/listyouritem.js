
const form = document.getElementById("form1")
form.addEventListener('submit',(e) => {
	var sname = document.getElementById("itemname").value 
	var email = document.getElementById("Email1").value
	var desc = document.getElementById("Description").value
	var pickaddress = document.getElementById("pickupaddress").value
	
	if (email == "") {
		document.getElementById("emailErrorMsg").innerHTML = "Email field cannot be empty"
		e.preventDefault()
	}
	if (desc == "") {
		document.getElementById("descErrorMsg").innerHTML = "Password field cannot be empty"
		e.preventDefault()
	}

	if (pickaddress == "") {
		document.getElementById("pickErrorMsg").innerHTML = "Pickup Address cannot be empty."
		e.preventDefault()
	}
	else {
		alert("Successfully Listed the item");
		location.href = "/myprofile" ; 
	}
})