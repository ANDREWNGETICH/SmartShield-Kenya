async function analyzeMessage() {

    const message =
        document.getElementById("messageInput").value;

    try {

        document.getElementById("resultBox").innerHTML = `
    <p style="color:#38bdf8;">
        AI scanning threat...
    </p>
`;

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

    <div class="threat-card ${riskClass}">

       <h2 class="threat-status">

            ${
                data.threat_level === "HIGH"
                ? "⚠ HIGH RISK THREAT"

                : data.threat_level === "MEDIUM"
                ? "⚡ MEDIUM RISK"

                : data.threat_level === "LOW"
                ? "🟡 LOW RISK"

                : "✅ SAFE MESSAGE"
            }

        </h2>

        <div class="threat-badge">
            ${data.threat_level} RISK
        </div>
        <div class="risk-meter">

            <div
                class="risk-fill ${riskClass}"
                style="width:${data.risk_score}%">
            </div>

        </div>

        <p>
            <strong>AI Prediction:</strong>
            ${data.ai_prediction}
        </p>

        <p>
            <strong>AI Confidence:</strong>
            ${data.confidence_score}%
        </p>

        <p>
            <strong>Kenyan Scam Intelligence:</strong>
            ${data.kenyan_detected ? "Detected" : "Not Detected"}
        </p>

        <p>
            <strong>Scam Category:</strong>
            ${data.kenyan_category}
        </p>
        
        <div class="category-badge">
            ${data.kenyan_category}
        </div>

        <p>
            <strong>Risk Score:</strong>
            ${data.risk_score}%
        </p>

        <p>
            <strong>Detected Keywords:</strong>
            ${keywords}
        </p>

    </div>

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