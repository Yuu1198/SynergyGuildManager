const guildmembersButton =
    document.getElementById("guildmembers-button");

guildmembersButton.addEventListener("click", async function() {
    try {
        const response = await fetch("/guildmembers");

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        } 

        const guildmembers = await response.json();

        const guildmembersTable = document.getElementById("guildmembers-table");
        const guildmembersBody = document.getElementById("guildmembers-body");

        // Clear existing table rows
        guildmembersBody.innerHTML = "";

        // Populate the table with guild member data
        guildmembers.forEach(function(member) {
            const row = document.createElement("tr");
            
            const nameCell = document.createElement("td");
            nameCell.textContent = member.name;

            const classCell = document.createElement("td");
            classCell.textContent = member.class_name;

            row.appendChild(nameCell);
            row.appendChild(classCell);

            guildmembersBody.appendChild(row);
        });

        guildmembersTable.hidden = false; // Show the table
    }
        catch (error) {
            console.error("Error fetching guild members:", error);
            return;
    }
});