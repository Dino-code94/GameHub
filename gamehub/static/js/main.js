// main.js – small interactive UI effects for GameHub
// -------------------------------------------------
// This file contains small JavaScript enhancements to improve UX.
// Nothing here is required for core logic – this is presentation sugar only.

// Wait until the page fully loads
document.addEventListener("DOMContentLoaded", function () {

    // ----------------------------------------------
    // COMMENT BUTTON GLOW EFFECT (on game detail)
    // ----------------------------------------------

    // select comment submit button (only exists on detail page)
    const btn = document.querySelector(".comment-btn");

    // check that button exists
    if (btn) {
        // when button is clicked -> add glow briefly
        btn.addEventListener("click", function () {
            btn.classList.add("glow"); // add glow css class

            // remove glow after 300ms so it's a flash, not permanent
            setTimeout(() => {
                btn.classList.remove("glow");
            }, 300);
        });
    }

    // ----------------------------------------------
    // CARD HOVER SCALE EFFECT (on index page)
    // ----------------------------------------------

    // select all game cards
    const cards = document.querySelectorAll(".game-card");

    // add small pop animation on hover
    cards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.transform = "scale(1.05)"; // scale slightly bigger
            card.style.transition = "transform 0.15s ease-in-out";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "scale(1)"; // reset back to normal
        });
    });

});
