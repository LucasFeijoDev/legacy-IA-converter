document.getElementById('converter-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const legacy_code = document.getElementById('legacy_code').value;
    const language = document.getElementById('language').value;

    const response = await fetch('/convert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ legacy_code, language })
    });

    const data = await response.json();
    document.getElementById('result').innerText = data.converted_code;
});