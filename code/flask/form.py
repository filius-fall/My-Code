from flask import Flask, redirect,url_for, request
app = Flask(__name__, template_folder='/home/rams/Desktop/code/HTML')

@app.route('/success')
def user():
    return  