function openme(){
document.getElementById('login1').style.display='block';
document.getElementById('login2').style.display='block';
}
function closeme(){
document.getElementById('login1').style.display='none';
document.getElementById('login2').style.display='none';
}
function openme2(){
document.getElementById('login12').style.display='block';
document.getElementById('login22').style.display='block';
}
function closeme2(){
document.getElementById('login12').style.display='none';
document.getElementById('login22').style.display='none';
}
function logo_in(){
    //alert()
//��֤
//ת��...
//myform.action=""
//myform.submit()
    var username = document.myform.username.value()

    if(document.myform.username.value()=="pipisorry"&&document.myform.passwd.value()=="pipisorry"){
        location.href="header.html"
    }
    else{
        //alert("no such user exit!");
        alert()
        closeme();
    }
}