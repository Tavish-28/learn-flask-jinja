from flask import Flask ,render_template, request, redirect, url_for

app = Flask(__name__)
REG1={}
SPORTS = ["soccer", "basketball", "cricket"]

@app.route('/')
def index():
    return render_template('index.html',sports=SPORTS)
@app.route('/register', methods=['POST'])
def register():
    # Name is optional.
    name = request.form.get('name')
    if not name:
        return render_template("error.html",error_message="Name is required")

    #invalid sport
    sport = request.form.get('sport')
    #agar sport naahi bhara
    if not sport:
        return render_template("error.html",error_message="select any sport")
#if hacked
    elif sport not in SPORTS:
        return render_template("error.html",error_message="select from the given list of sports")
# if both not filled
    if not name and not sport:
        return render_template("error.html",error_message="Name and sport are required")

    #remember student
    #successful registration
    REG1[name] = sport
    return render_template("success.html")
    @app.route('/reg1')
    def reg1():
        # if name is in REG1:
        return render_template("reg1.html",reg1=REG1)