class SocialButton {
    
    constructor(name) {
        this.name = name;
        this.button = document.getElementById(this.name);
        this.hitType = 'social';
        this.socialAction = "Share";
        this.socialTarget = document.location.href;
        this.trackShareAction(this.button);
    }

    trackShareAction(buttonElt) {
        buttonElt.addEventListener("click", () => {
            ga('send', {
                hitType: 'social',
                socialNetwork: buttonElt.name,
                socialAction: 'Share',
                socialTarget: document.location.href
              });
        })
    }

}

// Initialization

const facebook = new SocialButton("facebook");
const twitter = new SocialButton("twitter");
const linkedin = new SocialButton("linkedin");