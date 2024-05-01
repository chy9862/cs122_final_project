from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    make_response,
    jsonify,
)
from app import (
    db,
)  # check this later if it is an issue, nmight need to rename mdels.py to __init__.py
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.models import User
import requests
from app.config import Config

routes = Blueprint("routes", __name__)


@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))


@routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # check if user used the field prompts properly -- cannot be empty.
        if len(email) < 1:
            flash("Email cannot be empty, please try again", category="error")
        if len(password) < 1:
            flash("Password cannot be empty, try again.", category="error")
        else:
            # checks if user exist through email. Then use check_password_hash() to check if password matches with password from request
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Loggin in successfully.", category="success")
                    login_user(user, remember=True)
                    return redirect("authorizedHomepage")  # change this later
                else:
                    flash("Password does not match. Try Again.", category="error")
            else:
                flash("Email does not exist.", category="error")

    return render_template("LoginPage.html", user=current_user)


@routes.route("/sign-up", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        elif len(email) < 4:
            flash("Email must be larger than 3 characters", category="error")
        elif len(first_name) < 2:
            flash("First name must be larger than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords must match!", category="error")
        elif len(password1) < 7:
            flash(
                "Password is too short. It should be larger than 7 characters",
                category="error",
            )
        else:
            # generates a password hash with sha-256 algorithm as a security feature.
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="pbkdf2:sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created successfully!", category="success")
            # return redirect(url_for('routes.authorizedHomepage'), user=current_user)
            return render_template("AuthorizedHomepage.html", user=current_user)

    return render_template("SignUpPage.html", user=current_user)


@routes.route("/authorizedHomepage", methods=["POST", "GET"])
@login_required
def authorizedHomepage():
    if request.method == "POST":
        keyword = request.form.get("search")
        if not keyword:
            return flash("keyword cannot be empty.", category="error")
        # redirect(url_for('routes.get_event', keyword = keyword))
        event_list = []

        for i in range(
            2
        ):  # you can change the number in range(num) for how many pages you want

            # get the json data
            event_data = fetch_event_details(Config.api_key, i, keyword)

            # Check if the response is an error message
            if isinstance(event_data, str):
                return make_response(jsonify({"error": event_data}), 403)

            # get the events list in json file
            events = event_data.get("_embedded", {}).get("events", [])

            # create the dictionary for each event by traversing all the events
            for event in events:

                # create the new dictionary
                event_info = {}

                # get the event name, data, url
                event_info["event_name"] = event.get("name")
                event_info["event_date"] = (
                    event.get("dates", {})
                    .get("start", {})
                    .get("localDate", "Date not available")
                )
                event_info["event_url"] = event.get("url", "URL not available")

                # get the "venues" list for event
                venues = event.get("_embedded", {}).get("venues", [])

                # get the "city" information in the list
                for venue in venues:

                    # get the city name for the event and check the city is matched
                    city = venue.get("city", {}).get("name", "")
                    event_info["venue"] = venue.get("name", "Venue not available")
                    event_info["city"] = city

                    # get the image url
                    images = event.get("images", [])
                    if images and len(images) > 3:
                        event_info["image_url"] = images[8].get(
                            "url", "No image available"
                        )

                    # if the city is mateched, the dictionary is added to the list 'event_list'
                    if event_info.get("event_name") and event_info.get("venue"):
                        event_list.append(event_info)
        if len(event_list) == 0:
            flash(
                "There are no events happening in that area. Try again",
                category="error",
            )
        else:
            return render_template(
                "SearchEventPage.html", events=event_list, user=current_user
            )
    return render_template("AuthorizedHomepage.html", user=current_user)


# get the api key and page number
def fetch_event_details(api_key, page, keyword):

    # url for events
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&locale=*&page={page}&keyword={keyword}"

    # request
    response = requests.get(url)

    # return the json if the data is successfully retrieved.
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to retrieve events."
