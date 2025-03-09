document.addEventListener("DOMContentLoaded", loadTransactions);

function loadTransactions() {
    fetch("/expenses/load")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("transaction-list");
            list.innerHTML = data.data.map(tx => `
                <tr>
                    <td>${tx.description}</td>
                    <td class="${tx.amount >= 0 ? 'positive' : 'negative'}">$${tx.amount.toFixed(2)}</td>
                    <td>${new Date(tx.timestamp).toLocaleDateString()}</td>
                </tr>
            `).join("");
        })
        .catch(error => console.error("Error loading transactions:", error));
}

function addTransaction() {
    const description = document.getElementById("description").value;
    let amount = parseFloat(document.getElementById("amount").value);
    const type = document.getElementById("transaction-type").value;

    if (!description || isNaN(amount)) return alert("Enter valid details.");
    if (type === "expense") amount = -Math.abs(amount); // Convert to negative for expenses

    fetch("/expenses/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description, amount })
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "expense_added") {
            document.getElementById("description").value = "";
            document.getElementById("amount").value = "";
            document.getElementById("transaction-type").value = "income"; // Reset dropdown
            loadTransactions(); // Auto-refresh the table
        }
    })
    .catch(error => console.error("Error adding transaction:", error));
}

function logout() {
    fetch("/logout").then(() => window.location.href = "/login");
}