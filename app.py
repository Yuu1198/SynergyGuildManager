from flask import Flask, render_template, jsonify

app = Flask(__name__)

class GuildMember:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

    def __repr__(self):
        return f"GuildMember(name={self.name}, class_name={self.class_name}))"


# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for the API endpoint to get guild members
@app.route('/guildmembers', methods=['GET'])
def get_guild_members_api():
    members = get_guild_members()

    return jsonify([
        {
            'name': member.name,
            'class_name': member.class_name
        }
        for member in members
    ])

def get_guild_members():
    # Sample data for guild members
    members = [
        GuildMember("Calcain", "Warrior"),
        GuildMember("Nortag", "Rogue"),
        GuildMember("Biha", "Druid"),
        GuildMember("Neptune", "Mage"),
        GuildMember("Jocap", "Hunter")
    ]
    return members


if __name__ == '__main__':
    app.run(debug=True)