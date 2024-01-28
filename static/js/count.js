function countAnime() {
    document.addEventListener("DOMContentLoaded", function () {
        // Add an event listener for the page refresh (F5 or browser refresh button)
        window.addEventListener("beforeunload", function () {
            // Store the current count in sessionStorage
            sessionStorage.setItem("initialDivCount", document.querySelectorAll('.valid_count').length);
        });

        // On page load, check if there is a stored count and display it
        window.addEventListener("load", function () {
            let initialDivCount = sessionStorage.getItem("initialDivCount");
            if (initialDivCount !== null) {
                console.log("Number of divs before refresh: " + initialDivCount);
                // Compare the current count with the initial count
                let currentDivCount = document.querySelectorAll('.valid_count').length;

                if (currentDivCount != initialDivCount) {
                    alert("Anime added to your watchlist.");
                }
                else {
                    alert("Anime was already in your watchlist.");
                }
            }
        });
    });
}