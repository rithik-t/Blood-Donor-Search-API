function searchDonors() {
    const bloodGroup = document.getElementById("bloodGroup").value.trim(); // Ensure trimmed input

    if (!bloodGroup) {
        alert("Please enter a blood group!");
        return;
    }

    console.log("Searching for blood group:", bloodGroup); // Debugging step

    fetch(`http://127.0.0.1:5000/search?bloodGroup=${encodeURIComponent(bloodGroup)}`)
    .then(response => response.json())
    .then(data => {
        let resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";

        if (data.length === 0) {
            resultsDiv.innerHTML = "<p>No donors found.</p>";
        } else {
            data.forEach(donor => {
                resultsDiv.innerHTML += `<p>Name: ${donor.name}, Contact: ${donor.contact}</p>`;
            });
        }
    })
    .catch(error => console.error("Error:", error));
}
