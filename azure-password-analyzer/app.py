from flask import Flask, request, jsonify
import requests, hashlib, os
import pymysql, random, string

app = Flask(__name__)

# Optional: connect to MySQL for stats
db = pymysql.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS"),
    database=os.environ.get("DB_NAME")
)

# Password strength checker
def check_strength(pwd):
    score = 0
    if len(pwd) >= 8: score += 25
    if any(c.islower() for c in pwd): score += 15
    if any(c.isupper() for c in pwd): score += 15
    if any(c.isdigit() for c in pwd): score += 15
    if any(c in string.punctuation for c in pwd): score += 30
    strength = "Weak" if score < 50 else "Medium" if score < 80 else "Strong"
    return score, strength

# Breach checker using HIBP
def check_breach(pwd):
    sha1 = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    res = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    hashes = res.text.splitlines()
    for line in hashes:
        if line.startswith(suffix):
            return "Compromised"
    return "Safe"

@app.route("/")
def home():
    return "Password Analyzer Running"

@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.json
    pwd = data.get("password")
    score, strength = check_strength(pwd)
    breach = check_breach(pwd)

    # Optional: store stats
    cursor = db.cursor()
    cursor.execute("INSERT INTO submissions(strength, breach) VALUES (%s, %s)", (strength, breach))
    db.commit()

    return jsonify(score=score, strength=strength, breach=breach)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
