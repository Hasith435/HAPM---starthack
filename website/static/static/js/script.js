document.addEventListener('DOMContentLoaded', function () {
    // Function to add chemicals
    function addChemicals() {
        const chemical1 = document.getElementById('chemical1').value;
        const chemical2 = document.getElementById('chemical2').value;
        
        fetch('/add-chemical', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ chemical1: chemical1, chemical2: chemical2 })
        })
        .then(response => response.json())
        .then(data => {
            // Display message in reaction results div
            reactionResultsDiv.innerHTML += `<p>${data.message}</p>`;
        })
        .catch(error => {
            console.error('Error adding chemicals:', error);
        });
    }

    // Function to trigger reaction
    function triggerReaction() {
        fetch('/trigger-reaction', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            // Display reaction result in reaction results div
            reactionResultsDiv.innerHTML += `<p>${data.message}</p>`;
        })
        .catch(error => {
            console.error('Error triggering reaction:', error);
        });
    }

    // Simulate reaction on load for demonstration
    // simulateReaction(); // Uncomment this if needed

    const addChemicalButton = document.getElementById('add-chemical');
    const triggerReactionButton = document.getElementById('trigger-reaction');
    const reactionResultsDiv = document.getElementById('reaction-results');

    addChemicalButton.addEventListener('click', function () {
        addChemicals();
    });

    triggerReactionButton.addEventListener('click', function () {
        triggerReaction();
    });
});
