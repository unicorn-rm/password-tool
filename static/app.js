const input = document.getElementById("password");

input.addEventListener("input", async () => {
    const password = input.value;

    if (!password) {
        resetUI();
        return;
    }

    const res = await fetch("/api/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({password})
    });

    const data = await res.json();

    updateUI(data);
});

function updateUI(data) {
    const bar = document.getElementById("bar");
    const status = document.getElementById("status");
    const feedback = document.getElementById("feedback");

    // progress bar
    bar.style.width = data.score + "%";

    // color + status
    if (data.level === "weak") {
        bar.style.background = "#ff4d4d";
        status.innerText = "Weak password";
        status.style.color = "#ff4d4d";
    } else if (data.level === "medium") {
        bar.style.background = "#ffb84d";
        status.innerText = "Medium strength password";
        status.style.color = "#ffb84d";
    } else {
        bar.style.background = "#4dff88";
        status.innerText = "Strong password";
        status.style.color = "#4dff88";
    }

    // dictionary warning
    if (data.is_common) {
        status.innerText = "CRITICAL: Common password detected!";
        status.style.color = "red";
        bar.style.background = "red";
    }

    // feedback list
    feedback.innerHTML = "";
    data.feedback.forEach(msg => {
        const li = document.createElement("li");
        li.innerText = "⚠ " + msg;
        feedback.appendChild(li);
    });
}

function resetUI() {
    document.getElementById("bar").style.width = "0%";
    document.getElementById("status").innerText = "Waiting for input...";
    document.getElementById("feedback").innerHTML = "";
}

async function generatePassword() {
    const res = await fetch("/api/generate");
    const data = await res.json();
    document.getElementById("generated").value = data.password;
}