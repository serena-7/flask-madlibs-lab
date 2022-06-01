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

colors = [
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
        return render_template("game.html", colors=colors)

@app.route('/madlib')
def show_madlib():
    person = request.args.get('person')
    colors = request.args.getlist('colors')
    color = ''
    if len(colors) > 2:
        for i in range(len(colors)):
            if i != len(colors) - 1:
                color += colors[i] + ', '
            else:
                color += 'and ' + colors[i]
    elif len(colors) ==2:
        color = colors[0] + ' and ' + colors[1] 
    elif len(colors) == 1:
        color = colors[0]
    else:
        color = 'clear'
    noun = request.args.get('noun')
    adjective = request.args.get('adjective')
    print(colors)
    return render_template('madlib.html', person=person, color=color, noun=noun, adjective=adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
