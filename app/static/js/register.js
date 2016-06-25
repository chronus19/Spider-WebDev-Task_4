

function validate() {

    var pwd = document.getElementById('passwd').value;
    var repwd = document.getElementById('repasswd').value;
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var username = document.getElementById('username').value;

    if ( username.length < 4 || name.length  <=2 || email.length <=8 || email.length >128 ||pwd.length < 8 ) {
    	alert('Fill the required fields properly.');
    	return;
    }
      
    if ( pwd != repwd) {
    	alert("Please enter your password correctly.")
    	return;
    }
    
    document.myform.submit();

}