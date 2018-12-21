class Header {
    constructor() {
        this.header = document.getElementsByTagName("header")[0];
        this.title = document.getElementsByClassName("heading-brand heading-brand--primary")[0];
        this.headerMenu = document.getElementsByClassName("header__tag-box")[0];
        this.headerTagsLink = document.getElementsByClassName("header__tag-box__link");
        this.addMaterialDesignShadow(this.header);
        this.manageMenuSelection(this.headerTagsLink);      
    }

    addMaterialDesignShadow(headerElt) {
        window.onscroll = function() {addShadow()};

        function addShadow() {
            if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0) {
                headerElt.classList.add("header-shadow");
            } else {
                headerElt.classList.remove("header-shadow");
            }
        } 
    }

    manageMenuSelection(headerTagsLinkElt) {
        const url = new URL(document.location.href);
        const pathRegex = /^\/tag\/.*\/$/
        if (pathRegex.test(url.pathname)) {
            for (let link of headerTagsLinkElt) {
                const linkUrl = new URL(link.href);
                if (linkUrl.pathname === url.pathname) {
                    link.classList.add('active-header');
                } else {
                    link.classList.remove('active-header');
                }
            }
        } 
    }
}

// Initialisation

const header = new Header()