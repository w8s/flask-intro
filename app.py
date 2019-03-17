from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

names = ["Todd"]


@app.route("/")
def hello():
    return render_template("home.html", message="Hello World!", names=names)


@app.route("/new-name/", methods=["POST"])
def new_name():
    name = request.form.get("name")
    names.append(name)

    return redirect(url_for("hello"))


if __name__ == "__main__":
    app.run()
