from flask import render_template, Blueprint

default = Blueprint('default', __name__, template_folder='templates')

@default.route("/", methods=["GET"])
def index():
    return render_template("HomePage.html")

@default.route("/menu", methods=["GET"])
def menu():
    return render_template("MenuPage.html")

@default.route("/about", methods=["GET"])
def about():
    return render_template("AboutUsPage.html")

@default.route("/roasted-goose", methods=["GET"])
def roastedGoose():
    return render_template("RoastedGoose.html")

@default.route("/barbecue-pork", methods=["GET"])
def barbecuePork():
    return render_template("BarbecuePorkPage.html")

@default.route("/goose-wing", methods=["GET"])
def gooseWing():
    return render_template("GooseWingPage.html")

@default.route("/goose-feet", methods=["GET"])
def goostFeet():
    return render_template("GooseFeetPage.html")

@default.route("/foie-gras", methods=["GET"])
def foieGras():
    return render_template("FoieGrasPage.html")

@default.route("/goose-gizzards", methods=["GET"])
def GooseGizzards():
    return render_template("GooseGizzardsPage.html")

@default.route("/cart", methods=["GET"])
def cart():
    return render_template("CartPage.html")

@default.route("/login", methods=["GET"])
def login():
    return render_template("LoginPage.html")

@default.route("/SignUp", methods=["GET"])
def signUp():
    return render_template("SignUpPage.html")