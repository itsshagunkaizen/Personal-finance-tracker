from flask import Flask, render_template, request, redirect, session
import sqlite3
import csv
import os

app = Flask(__name__)
app.secret_key = "secret123"

DB = "users.db"
DATA = "data.csv"


def get_db():
    return sqlite3.connect(DB)


# ---------- AUTH ----------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        db = get_db()
        cur = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?", (u, p)
        )
        user = cur.fetchone()
        db.close()

        if user:
            session["user"] = u
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        db = get_db()
        db.execute("INSERT INTO users VALUES (?,?)", (u, p))
        db.commit()
        db.close()

        return redirect("/login")

    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ---------- DASHBOARD ----------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        t = request.form["type"]
        amt = request.form["amount"]
        cat = request.form["category"]

        with open(DATA, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([t, amt, cat])

    return render_template("dashboard.html")


# ---------- SUMMARY ----------
@app.route("/summary")
def summary():
    income = 0
    expense = 0

    if os.path.exists(DATA):
        with open(DATA) as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 2:
                    continue
                try:
                    amt = float(row[1])
                except:
                    continue

                if row[0] == "Income":
                    income += amt
                else:
                    expense += amt

    balance = income - expense
    return render_template(
        "summary.html", income=income, expense=expense, balance=balance
    )


@app.route("/clear", methods=["POST"])
def clear():
    open(DATA, "w").close()
    return redirect("/summary")


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
