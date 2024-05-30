from flask import render_template, Blueprint, session

default = Blueprint('default', __name__, template_folder='templates')

@default.route("/", methods=["GET"])
def index():
    logged_in = session.get("logged_in", False)
    return render_template("HomePage.html", logged_in=logged_in)

@default.route("/menu", methods=["GET"])
def menu():
    logged_in = session.get("logged_in", False)
    return render_template("MenuPage.html", logged_in=logged_in)

@default.route("/about", methods=["GET"])
def about():
    logged_in = session.get("logged_in", False)
    return render_template("AboutUsPage.html", logged_in=logged_in)

@default.route("/roasted-goose", methods=["GET"])
def roastedGoose():
    logged_in = session.get("logged_in", False)
    return render_template("RoastedGoose.html", logged_in=logged_in)

@default.route("/barbecue-pork", methods=["GET"])
def barbecuePork():
    logged_in = session.get("logged_in", False)
    return render_template("BarbecuePorkPage.html", logged_in=logged_in)

@default.route("/goose-wing", methods=["GET"])
def gooseWing():
    logged_in = session.get("logged_in", False)
    return render_template("GooseWingPage.html", logged_in=logged_in)

@default.route("/goose-feet", methods=["GET"])
def goostFeet():
    logged_in = session.get("logged_in", False)
    return render_template("GooseFeetPage.html", logged_in=logged_in)

@default.route("/foie-gras", methods=["GET"])
def foieGras():
    logged_in = session.get("logged_in", False)
    return render_template("FoieGrasPage.html", logged_in=logged_in)

@default.route("/goose-gizzards", methods=["GET"])
def GooseGizzards():
    logged_in = session.get("logged_in", False)
    return render_template("GooseGizzardsPage.html", logged_in=logged_in)

@default.route("/cart", methods=["GET"])
def cart():
    logged_in = session.get("logged_in", False)
    return render_template("CartPage.html", logged_in=logged_in)

@default.route("/login", methods=["GET"])
def login():
    logged_in = session.get("logged_in", False)
    return render_template("LoginPage.html", logged_in=logged_in)

@default.route("/SignUp", methods=["GET"])
def signUp():
    logged_in = session.get("logged_in", False)
    return render_template("SignUpPage.html", logged_in=logged_in)