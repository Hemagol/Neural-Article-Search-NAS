// Function to perform the search when the user clicks the search button or presses "Enter"
function performSearch() {
    const query = document.getElementById('searchQuery').value;
    const resultsDiv = document.getElementById('results');
    
    // Clear previous results
    resultsDiv.innerHTML = '';

    // If the query is empty, display an error message
    if (!query.trim()) {
        resultsDiv.innerHTML = '<p>Please enter a search query.</p>';
        return;
    }

    // Send the search query to the backend using fetch
    fetch(`/search?query=${encodeURIComponent(query)}`)
        .then(response => {
            if (!response.ok) {
                if (response.status === 404) {
                    return { message: "No articles found for the predicted category." };
                }
                throw new Error("Server error");
            }
            return response.json();
        })
        .then(data => {
            // Check if the response contains an error or no results
            if (data.error) {
                resultsDiv.innerHTML = `<p>${data.error}</p>`;
            } else if (data.message) {
                resultsDiv.innerHTML = `<p>${data.message}</p>`;
            } else {
                // Display the results
                data.forEach(result => {
                    const resultItem = document.createElement('div');
                    resultItem.classList.add('result-item');
                    resultItem.innerHTML = `
                        <h3>${result.article_title}</h3> <!-- Title -->
                        <p><a href="${result.article_link}" target="_blank">${result.article_link}</a></p> <!-- URL -->
                    `;
                    resultsDiv.appendChild(resultItem);
                });
            }
            // Show results container only if there are results
            resultsDiv.style.display = data.length ? 'block' : 'none';
        })
        .catch(error => {
            console.error('Error fetching search results:', error);
            resultsDiv.innerHTML = '<p>An error occurred while searching. Please try again.</p>';
        });
}

// Function to trigger search when "Enter" is pressed
function checkEnter(event) {
    if (event.key === 'Enter') {
        performSearch();
    }
}
