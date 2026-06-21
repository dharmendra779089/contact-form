/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/

// Add an event listener to run code after the HTML document's initial DOM structure is fully parsed and loaded.
window.addEventListener('DOMContentLoaded', () => {
    
    // Initialize a variable to track the previous vertical scroll position, starting at 0.
    let scrollPos = 0;
    
    // Select and store the main navigation element with ID 'mainNav' to dynamically manipulate its CSS classes later.
    const mainNav = document.getElementById('mainNav');
    
    // Get the inner height of the navigation bar in pixels, including padding but excluding borders and margins.
    const headerHeight = mainNav.clientHeight;
    
    // Register a scroll event listener on the window object to run code every time the user scrolls the page.
    window.addEventListener('scroll', function() {
        
        // Calculate the current distance from the top of the viewport to the top of the body element,
        // multiplying by -1 to get a positive scroll coordinate representing how far down the page the user has scrolled.
        const currentTop = document.body.getBoundingClientRect().top * -1;
        
        // Compare the current scroll position with the previous scroll position to determine direction.
        // If currentTop is smaller than scrollPos, the user is scrolling UP.
        if ( currentTop < scrollPos) {
            
            // If the user has scrolled past the top (currentTop > 0) and the nav has 'is-fixed' styling,
            // add the 'is-visible' class to slide the navigation bar down into view.
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                // Log a debugging value to the console (left in from original template code).
                console.log(123);
                // If scrolling up near the very top of the page, completely hide/unfix the navigation bar.
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Otherwise, the user is scrolling DOWN.
            
            // Remove the 'is-visible' class so the navbar slides up out of view while scrolling down.
            mainNav.classList.remove(['is-visible']);
            
            // If the user has scrolled beyond the height of the navigation header itself and the navbar
            // is not already fixed, add the 'is-fixed' class to position it at the top of the viewport.
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        
        // Update scrollPos with the current scroll position for comparison in the next scroll event cycle.
        scrollPos = currentTop;
    });
})
