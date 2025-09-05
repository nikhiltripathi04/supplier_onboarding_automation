// frontend/script.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('supplier-form');
    const responseDiv = document.getElementById('response-message');
    const submitButton = form.querySelector('button');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent the default form submission

        const supplierName = document.getElementById('supplierName').value;
        const gstin = document.getElementById('gstin').value;
        
        // The API endpoint URL provided by Vercel
        const apiUrl = '/api/onboard';

        // Provide user feedback
        submitButton.textContent = 'Processing...';
        submitButton.disabled = true;
        responseDiv.textContent = '';
        responseDiv.className = '';

        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ supplierName, gstin }),
            });

            const result = await response.json();

            if (response.ok) { // Check if the HTTP status is 2xx (e.g., 200 OK)
                responseDiv.textContent = result.message;
                responseDiv.className = 'success';
                form.reset(); // Clear the form on success
            } else {
                // The API returned an error (e.g., 400 for bad validation)
                responseDiv.textContent = `Error: ${result.message}`;
                responseDiv.className = 'error';
            }
        } catch (error) {
            // A network error occurred
            responseDiv.textContent = 'A network error occurred. Please try again.';
            responseDiv.className = 'error';
            console.error('Submission Error:', error);
        } finally {
            // Re-enable the button
            submitButton.textContent = 'Onboard Supplier';
            submitButton.disabled = false;
        }
    });
});
