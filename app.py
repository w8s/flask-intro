from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "This is a terrible key"


@app.route("/")
def hello():
    if "names" not in session:
        session["names"] = ["Todd"]
    names = session["names"]
    return render_template("home.html", message="Hello World!", names=names)


@app.route("/new-name/", methods=["POST"])
def new_name():
    names = session["names"]
    name = request.form.get("name")
    names.append(name)
    session["names"] = names

    return redirect(url_for("hello"))


@app.cli.command("add_names")
def cli_names():
    """Adds five names to the names list"""
    print("Adding names...")
    names = session["names"] # THIS IS NOT GOING TO WORK!
    names.append("Kazoo")
    names.append("Nathario")
    names.append("Lizzymag")
    names.append("Peppa")
    names.append("Wesley")
    session["names"] = names
    print("Done adding names.")


if __name__ == "__main__":
    app.run()
