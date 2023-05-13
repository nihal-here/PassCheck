from flask import Flask, render_template, request
import requests
import hashlib
import sys
import string
from passlib import pwd

app = Flask(__name__)
def req_api_data(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"error fetching:{res.status_code},check the api and try again"
        )
    return res

def get_pass_leak_count(hashes,hash_to_check):
    hashes=(line.split(':')for line in hashes.text.splitlines())        #split hash and count
    for h,count in hashes:
        if h==hash_to_check:                #check if the tail matches any hashes send by api
             return count                   #if matched send count of breaches
    return 0


def pwned_api_check(password):
    sha1pass=(hashlib.sha1(password.encode("utf-8")).hexdigest().upper())       #create sha1 of password
    first5_char,tail=sha1pass[:5],sha1pass[5:]                                  
    response=req_api_data(first5_char)  
    count = int(get_pass_leak_count(response, tail))            #
    return count

def generate_password():
    password = pwd.genword(length=12, charset="ascii_50", entropy=40)
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    count = None
    password = None
    suggestion=None
    if request.method == "POST":
        password = request.form["password"]
        count = pwned_api_check(password)
        if count>0:
            suggestion=generate_password()
    return render_template("index.html", count=count, password=password,suggestion=suggestion)


if __name__ == "__main__":
    app.run(debug=True)
