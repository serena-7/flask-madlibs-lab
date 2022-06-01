"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request, session

from madlib_options import options

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)
app.secret_key = 'super_secret_key'

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

COLORS = [
    'red','orange','yellow','green','blue','purple','pink', 'black', 'brown', 'gray', 'white'
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


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
    response = request.args.get("yesno")
    if response == "no":
        return render_template("goodbye.html")
    else:
        selection = choice(list(options))
        session['madlib_name'] = selection
        name = options[selection]['name']
        types = options[selection]['types']
        return render_template("game.html", name=name, types=types)

@app.route('/madlib')
def show_madlib():
    madlib_name = session['madlib_name']
    name = options[madlib_name]['name']
    res = {}
    for key in options[madlib_name]['types'].keys():
        res[key] = request.args.get(key)
    return render_template('madlib.html', name=name, res=res)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
