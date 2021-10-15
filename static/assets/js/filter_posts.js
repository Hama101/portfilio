let buttons = document.getElementsByName("post_box")
let post_holder = document.getElementById("post-holder")

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function(e) {
        e.preventDefault()
        let value = this.dataset.filter
        post_holder.innerHTML = ""
        $.ajax({
            url: "http://0.0.0.0:8000/filter_blogs/",
            data: { "type": value },
            data_type: 'json',
            success: function(res) {
                post_holder.innerHTML = res.data
            },
        })
        console.log(value);
    })
}