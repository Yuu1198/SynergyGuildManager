const addMemberForm = document.getElementById('add-member-form');
const addMemberButton = document.getElementById('add-member-button');

const formMessage = document.getElementById('form-message');

// Add new guild member
addMemberButton.addEventListener('click', function() {
    addMemberForm.hidden = !addMemberForm.hidden;
});

addMemberForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    // Get data from form
    const formData = new FormData(addMemberForm);

    // Send request to POST data
    try {
        const response = await fetch('/guildmembers', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        // Error Handeling
        if (!response.ok) {
            formMessage.textContent = result.error;
            formMessage.style.color = 'red';
            return;
        }

        formMessage.textContent = result.message;
        formMessage.style.color = 'green';

        addMemberForm.reset();

        // Refresh the guild members table
        await loadGuildMembers();

    } catch (error) {
        formMessage.textContent = 'A guild member with this name already exists.';
        formMessage.style.color = 'red';
    }
});

// Reload guild member table
async function loadGuildMembers() {
    const response = await fetch('/guildmembers'); // Request to GET all guild members

    if (!response.ok) {
        throw new Error('Failed to load guild members');
    }

    const guildMembers = await response.json();
    const tableBody = document.getElementById('guildmembers-table').getElementsByTagName('tbody')[0];

    tableBody.innerHTML = '';

    // Populate the table
    guildMembers.forEach(function(guildMember) {
        const row = document.createElement('tr');
        
        // Create and append cells for each property
        const nameCell = document.createElement('td');
        nameCell.textContent = guildMember.name;
        row.appendChild(nameCell);

        const classCell = document.createElement('td');
        classCell.textContent = guildMember.class_name;
        // Apply color based on class_name
        classCell.classList.add(guildMember.class_name.trim().toLowerCase());
        row.appendChild(classCell);

        tableBody.appendChild(row);
    });
}

document.addEventListener("DOMContentLoaded", loadGuildMembers);
