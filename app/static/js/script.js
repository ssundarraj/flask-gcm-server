function sendNotifData(){
    var msgString = document.getElementById("notif_msg").value;
    if(msgString != ""){
        if (window.XMLHttpRequest) {
            // code for IE7+, Firefox, Chrome, Opera, Safari
            xmlhttp=new XMLHttpRequest();
        }else {  // code for IE6, IE5
            xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState==4 && xmlhttp.status==200) {
                if(xmlhttp.responseText != "0") {
                    //success
                    document.getElementById("notif_msg").value = "";
                    console.log(xmlhttp.responseText);
                }
                else {
                    //failure
                    console.log(xmlhttp.responseText);
                }
            }
        }
        xmlhttp.open("POST","./",true);
        xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        xmlhttp.send("notif_msg="+msgString);
    }
}