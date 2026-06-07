async function analyzeMessage() {

    const message =
        document.getElementById("messageInput").value;

    try {

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

        let keywords = "None";

        if (data.keywords && data.keywords.length > 0) {
            keywords = data.keywords.join(", ");
        }

        let riskClass = "safe-risk";

        if (data.threat_level === "HIGH") {
            riskClass = "high-risk";
        }
        else if (data.threat_level === "MEDIUM") {
            riskClass = "medium-risk";
        }
        else if (data.threat_level === "LOW") {
            riskClass = "low-risk";
        }

        document.getElementById("resultBox").innerHTML = `
            <h3>Status: ${data.status}</h3>

            <p>
                <strong>AI Prediction:</strong>
                ${data.ai_prediction}
            </p>

            <p>
                <strong>Kenyan Scam Intelligence:</strong>
                ${data.kenyan_detected ? "Detected" : "Not Detected"}
            </p>

            <p>
                <strong>Scam Category:</strong>
                ${data.kenyan_category}
            </p>

            <p>
                <strong>Threat Level:</strong>

                <span class="${riskClass}">
                    ${data.threat_level}
                </span>
            </p>

            <p>
                <strong>Risk Score:</strong>
                ${data.risk_score}%
            </p>

            <p>
                <strong>Detected Keywords:</strong>
                ${keywords}
            </p>
        `;

    } catch (error) {

        console.error(error);

        document.getElementById("resultBox").innerHTML = `
            <p style="color:red;">
                Error connecting to SmartShield backend.
            </p>
        `;
    }
}