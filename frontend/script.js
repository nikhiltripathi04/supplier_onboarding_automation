// frontend/script.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('supplier-form');
    const responseDiv = document.getElementById('response-message');
    const submitButton = form.querySelector('button');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const supplierName = document.getElementById('supplierName').value;
        const gstin = document.getElementById('gstin').value;
        
        const apiUrl = '/api/onboard';

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

            // --- DEBUGGING LINES ADDED ---
            console.log('Received response from API:', response);
            console.log('Response OK?:', response.ok);
            console.log('Response Status:', response.status);
            // --- END DEBUGGING LINES ---

            const result = await response.json();

            // --- MORE DEBUGGING ---
            console.log('Parsed JSON result:', result);
            // --- END DEBUGGING ---

            if (response.ok) {
                // --- SUCCESS ALERT ADDED ---
                alert(`Success: ${result.message}`);
                responseDiv.textContent = result.message;
                responseDiv.className = 'success';
                form.reset();
            } else {
                // --- FAILURE ALERT ADDED ---
                alert(`Error: ${result.message}`);
                responseDiv.textContent = `Error: ${result.message}`;
                responseDiv.className = 'error';
            }
        } catch (error) {
            // --- NETWORK ERROR ALERT ADDED ---
            const errorMessage = 'A network error occurred. Please check the console.';
            alert(errorMessage);
            responseDiv.textContent = errorMessage;
            responseDiv.className = 'error';
            // --- MORE DEBUGGING ---
            console.error('Submission Error:', error);
            // --- END DEBUGGING ---
        } finally {
            submitButton.textContent = 'Onboard Supplier';
            submitButton.disabled = false;
        }
    });
});

