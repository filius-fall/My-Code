from flask import redirect
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return redirect('http://www.example.com')
if __name__ == "__main__":
    app.run(debug=True)