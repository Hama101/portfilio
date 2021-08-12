
let buttons = document.getElementsByName("app_box")
let app_holder = document.getElementById("app-holder")

for (let i = 0 ; buttons.length ; i++){
    buttons[i].addEventListener('click' , function (e){
        e.preventDefault()
        let value = this.dataset.filter
        app_holder.innerHTML = ""
        $.ajax({
            url:"filter_projects/",
            data:{"type":value},
            data_type:'json',
            success:function(res){
                app_holder.innerHTML = res.data
            },
        })
        console.log(value);
    })
}
