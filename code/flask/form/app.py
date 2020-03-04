from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    hostel = request.form.get("hostel")
    if not name or not hostel:
        return "Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    return render_template("success.html", name=name, hostel=hostel)

if __name__=="__main__":
    app.run(debug=True)
