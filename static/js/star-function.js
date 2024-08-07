document.addEventListener("DOMContentLoaded", function() {
    if (document.querySelector('.rating-box')) {
        // Get all labels and inputs
        const inputBox = document.querySelector('.rating-box');
        const labels = [...inputBox.querySelectorAll('label')];
        const inputs = [...inputBox.querySelectorAll('input')];
        
        // Initialize to -1 to indicate no input is checked
        let checkedInput = -1; 
        
        // Finds the checked value if it exist.
        inputs.forEach((input, index) => {
            if (input.checked) {
                checkedInput = index;
            }
        });

        if (checkedInput === -1) {
            // No input is checked, reset all labels to default color
            labels.forEach(lbl => lbl.style.color = '#888');
        } else {
            // Set the color based on the checked input
            labels.forEach((lbl, i) => {
                lbl.style.color = (i <= checkedInput) ? 'var(--yellow)' : '#888';
                console.log(lbl.style.color);
            });
        }
    }
});

function enableRatingModel(inputBox) {
    // Get all labels and inputs
    const labels = [...inputBox.querySelectorAll('label')];
    const inputs = [...inputBox.querySelectorAll('input')];

    // Set click label to active and check the responsive input
    labels.forEach((e, index) => {
        e.addEventListener('click', () => {
            labels[index].classList.add('active');
            setTimeout(() => {
                labels[index].classList.remove('active');
            }, 1000);
        });
    });
    
    // Set hovereffect on the labels
    labels.forEach((e, index) => {
        e.addEventListener('mouseover', () => {
            for (let i = 0; i < labels.length; i++) {
                labels[i].style.color = (i <= index) ? 'var(--yellow)' : '#888';
            }
        });
    });

    labels.forEach((label, index) => {
        label.addEventListener('mouseleave', () => {
            const checkIndex = inputs.findIndex(input => input.checked);
            if (checkIndex === -1) {
                // No input is checked, reset all labels to default color
                labels.forEach(lbl => lbl.style.color = '#888');
            } else {
                // Set the color based on the checked input
                labels.forEach((lbl, i) => {
                    lbl.style.color = (i <= checkIndex) ? 'var(--yellow)' : '#888';
                });
            }
        });
    });

}


// Enable rating model
if (document.querySelector('.rating-box'))
    enableRatingModel(document.querySelector('.rating-box'));

