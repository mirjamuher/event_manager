// TODO: handle "manage existing event" button
// TODO: Make the createBtn Event just an href in html 

function setupPage() {
    const elCreateBtn = document.querySelector("#createBtn");

    elCreateBtn.addEventListener("click", function(event){
        const url = event.currentTarget.getAttribute("data-url");
        location.assign(url);
    });
}

document.addEventListener("DOMContentLoaded", setupPage);
