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