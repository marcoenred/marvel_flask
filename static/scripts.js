document.addEventListener("DOMContentLoaded", function() {

    let back = document.getElementById("back");

    back.addEventListener("click", ()=> {
            window.history.back();
    });

});