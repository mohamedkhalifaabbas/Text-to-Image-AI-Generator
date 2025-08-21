document.getElementById('imageForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const prompt = document.getElementById('promptInput').value.trim();
    if (!prompt) return alert('Enter a description');

    // إظهار الـloading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('result').innerHTML = '';

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();
        if (data.error) {
            alert(data.error);
        } else {
            // عرض الصورة والرابط لتحميلها
            document.getElementById('result').innerHTML = `
                <div class="image-container">
                    <img src="data:image/png;base64,${data.image}" alt="Generated Image">
                    <div class="download-section">
                        <a href="/download?prompt=${encodeURIComponent(prompt)}" class="download-btn">Download Image</a>
                    </div>
                </div>
            `;
        }
    } catch (err) {
        alert('Error generating image');
        console.error(err);
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
});
