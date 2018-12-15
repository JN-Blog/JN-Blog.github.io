window.onscroll = function() {addShadow()};

function addShadow() {
    if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0) {
        document.getElementsByTagName("header")[0].classList.add("header-shadow");
    } else {
        document.getElementsByTagName("header")[0].classList.remove("header-shadow");
    }
}