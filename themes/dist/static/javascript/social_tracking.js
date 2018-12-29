class SocialButton {
    
    constructor(name) {
        this.name = name;
        this.button = document.getElementById(this.name);
        this.socialTarget = document.location.href;
        this.trackShareAction(this.button, this.name);
    }

    trackShareAction(buttonElt, name) {
        buttonElt.addEventListener("click", () => {
            gtag('event', 'share', {method : name})
        });
    }
}

// Initialization
const url = new URL(document.location.href);
const pathRegex = /^\/articles\/.*\/$/

if (pathRegex.test(url.pathname)) {
    window.onload = () => {
        const facebook = new SocialButton("facebook");
        const twitter = new SocialButton("twitter");
        const linkedin = new SocialButton("linkedin");
    }    
}


