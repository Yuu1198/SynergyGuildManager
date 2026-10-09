from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


class GuildMember:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

    def __repr__(self):
        return f"GuildMember(name={self.name}, class_name={self.class_name}))"