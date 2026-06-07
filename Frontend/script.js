    async function analyzeMessage() {

    const message =
        document.getElementById("messageInput").value;

    const response = await fetch(
        "http://127.0.0.1:5000/detect",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        }
    );

    const data = await response.json();

 document.getElementById("resultBox").innerHTML = `
    <h3>Status: ${data.status}</h3>

    <p>
        <strong>AI Prediction:</strong>
        ${data.ai_prediction}
    </p>

    <p>
        <strong>Detected Keywords:</strong>
        ${data.keywords.join(", ")}
    </p>
`;
}