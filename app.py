from flask import Flask, render_template, jsonify
from guild_member_dao import GuildMemberDAO

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

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

if __name__ == '__main__':
    GuildMemberDAO.init_db()  # Initialize the database and add sample data
    app.run(debug=True)