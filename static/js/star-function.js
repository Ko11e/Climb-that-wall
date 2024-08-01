function enableRatingModel(inputBox) {
    // Get all labels and inputs
    const labels = [...inputBox.querySelectorAll('label')];
    const inputs = [...inputBox.querySelectorAll('input')];
    
    // Set click label to active and check the responsive input
    labels.forEach((e, index) => {
        e.addEventListener('click', (event) => {
            labels[index].classList.add('active');
            setTimeout(() => {
                labels[index].classList.remove('active');
            }, 1000);
        });
    });
    
    // Set hovereffect on the labels
    labels.forEach((e, index) => {
        e.addEventListener('mouseover', (e) => {
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

