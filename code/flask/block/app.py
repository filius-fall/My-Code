from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    branch = request.form.get("branch")
    if not name or not branch:
        return render_template("failure.html")
    return render_template("success.html", name=name, branch=branch)

if __name__=="__main__":
    app.run(debug=True)
