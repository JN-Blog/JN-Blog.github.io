class SocialButton {
    
    constructor(name) {
        this.name = name;
        this.buttons = document.getElementsByClassName(this.name); // all share buttons linked to a specific social network
        this.trackShareAction(this.buttons, this.name);
    }

    trackShareAction(buttonElts, name) {
        // For each buttons from a social network
        for (let buttonElt of buttonElts) {
            buttonElt.addEventListener("click", () => {
                gtag('event', 'share', {method : name})
            });
        }
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
        const twitterDisqus = new SocialButton("share-twitter");
        const facebookDisqus = new SocialButton("share-facebook");
    }    
}


