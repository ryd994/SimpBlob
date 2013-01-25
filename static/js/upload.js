function upload(action)
 {
 var xmlhttp;
 if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
 xmlhttp.open("POST",action,true);
 xmlhttp.setRequestHeader("enctype","multipart/form-data") 
 alert(action)
 filename=document.getElementById("imputform").elements[0].value
 filename="file="+filename
 xmlhttp.send(filename)
 xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }
}