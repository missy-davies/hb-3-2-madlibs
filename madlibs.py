"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return """
    <!doctype html>
    <html>
      <head>
        <link rel = "stylesheet" href ="/static/madlibs.css">
        <title>Start Here</title>
      </head>
      <body>
        <h1>Click <a href="/hello">HERE</a> to get started!</h1>
       
      </body>
    </html>

    """


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():

    answer = request.args.get("yes_or_no")

    if answer == 'no':
        return render_template("goodbye.html")
    else: 
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    noun = request.args.get("noun")
    person = request.args.get("person")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    noun_1 = request.args.get("noun_1")
    color = request.args.get("color")
    
    return render_template("madlib.html", noun = noun, verb = verb, 
                            adjective = adjective, person = person , 
                            noun_1 = noun_1, color = color)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
