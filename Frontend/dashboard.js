async function loadAnalytics() {

    const response = await fetch(
        "http://127.0.0.1:5000/analytics"
    );

    const data = await response.json();

    document.getElementById("totalScans").innerText =
        data.total_scans;

    document.getElementById("scamDetected").innerText =
        data.scam_detected;

    document.getElementById("safeMessages").innerText =
        data.safe_messages;

    document.getElementById("highRisk").innerText =
        data.high_risk;
}

loadAnalytics();

async function loadHistory() {

    const response = await fetch(
        "http://127.0.0.1:5000/history"
    );

    const history = await response.json();

    let historyHTML = "";

    history.reverse().forEach(scan => {

        historyHTML += `
            <div class="history-card">

                <p>
                    <strong>Message:</strong>
                    ${scan.message}
                </p>

                <p>
                    <strong>Prediction:</strong>
                    ${scan.prediction}
                </p>

                <p>
                    <strong>Threat Level:</strong>
                    ${scan.threat_level}
                </p>

                <p>
                    <strong>Risk Score:</strong>
                    ${scan.risk_score}%
                </p>

            </div>
        `;
    });

    document.getElementById(
        "historyContainer"
    ).innerHTML = historyHTML;
}

loadHistory();