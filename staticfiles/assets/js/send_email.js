document.getElementById("e-btn").addEventListener("click" , function (e){
    e.preventDefault()
    const name = document.getElementById("e-name").value
    const email = document.getElementById("e-mail").value
    const subject = document.getElementById("e-subject").value
    const message = document.getElementById("e-message").value
    const data = {
        "name" : name,
        "email" : email,
        "subject":subject,
        "message":message
    }
    console.log(data);
    $.ajax({
        url:"send_email/",
        data:data,
        data_type:'json',
        success:function(res){
            console.log("send !");
        },
    })
})