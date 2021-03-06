function validate(){
  var name=document.cForm.name.value;
  var email=document.cForm.email.value;
  var password=document.cForm.password.value;
  var con_password=document.cForm.con_password.value;
  if(name==""){
    document.getElementById("name").style.borderBottom="2px solid red";
    document.getElementById("name_error").innerHTML="This is required field";
    document.getElementById("name").style.marginBottom="5px";
  }
  if(email==""){
    document.getElementById("email").style.borderBottom="2px solid red";
    document.getElementById("email_error").innerHTML="This is required field";
    document.getElementById("email").style.marginBottom="5px";
    return false;
  }
  if(password=="" ){
    document.getElementById("password").style.borderBottom="2px solid red";
    document.getElementById("password_error").innerHTML="This is required field";
    document.getElementById("password").style.marginBottom="5px";
    return false;
  }
  if(con_password==""){
    document.getElementById("con_password").style.borderBottom="2px solid red";
    document.getElementById("conpassword_error").innerHTML="This is required field";
    document.getElementById("con_password").style.marginBottom="5px";
    return false;
  }
  if (con_password!=password) {
    document.getElementById("con_password").style.borderBottom="2px solid red";
    document.getElementById("conpassword_error").innerHTML="Enter same password as above";
    document.getElementById("con_password").style.marginBottom="5px";
    return false;
  }
}
function validate1(){
  var email=document.cForm.email.value;
  var password=document.cForm.password.value;
  if(email==""){
    document.getElementById("email").style.borderBottom="2px solid red";
    document.getElementById("email_error").innerHTML="This is required field";
    document.getElementById("email").style.marginBottom="5px";
    return false;
  }
  if(password=="" ){
    document.getElementById("password").style.borderBottom="2px solid red";
    document.getElementById("password_error").innerHTML="This is required field";
    document.getElementById("password").style.marginBottom="5px";
    return false;
  }
}
function validateBlog(){
  var blogname=document.cForm.blogname.value;
  var title=document.cForm.title.value;
  if(blogname==""){
    document.getElementById("blogname").style.borderBottom="2px solid red";
    document.getElementById("Name_error").innerHTML="This is required field";
    document.getElementById("blogname").style.marginBottom="5px";
    return false;
  }
  if(title=="" ){
    document.getElementById("title").style.borderBottom="2px solid red";
    document.getElementById("title_error").innerHTML="This is required field";
    document.getElementById("title").style.marginBottom="5px";
    return false;
  }

}