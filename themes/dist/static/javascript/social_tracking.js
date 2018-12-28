class SocialButton {
    
    constructor(name) {
        this.name = name;
        this.button = document.getElementById(this.name);
        this.socialTarget = document.location.href;
        this.trackShareAction(this.name);
    }

    trackShareAction(name) {
        buttonElt.addEventListener("click", () => {
            gtag('event', 'share', {
                engagement : 'engagement_' + name, 
                method : document.location.href})
        });
    }
}

// Initialization
window.onload = () => {
    const facebook = new SocialButton("facebook");
    const twitter = new SocialButton("twitter");
    const linkedin = new SocialButton("linkedin");
}
