from flask import Flask, render_template, jsonify, request, redirect, url_for
from guild_member_dao import GuildMemberDAO

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    members = GuildMemberDAO.get_all_guild_members()
    return render_template('index.html', members=members)

# Define a route to get guild members
@app.route('/guildmembers', methods=['GET'])
def get_guild_members_api():
    members = GuildMemberDAO.get_all_guild_members()

    return jsonify([
        {
            'name': member.name,
            'class_name': member.class_name
        }
        for member in members
    ])

# Define a route to add a new guild member
@app.route('/guildmembers', methods=['POST'])
def add_guild_member_api():
    # Get the name and class_name from the form / request data
    name = request.form.get('name', '').strip()
    class_name = request.form.get('class_name', '').strip()

    if not name or not class_name:
        return jsonify({'error': 'Name and class name are required'}), 400

    # Add guild member to the database
    success = GuildMemberDAO.add_guild_member(name, class_name)

    if success:
        return jsonify({'message': 'Guild member added successfully'}), 201
    else:
        return jsonify({'error': 'Failed to add guild member'}), 500


if __name__ == '__main__':
    GuildMemberDAO.init_db()  # Initialize the database and add sample data
    app.run(debug=True)