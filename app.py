from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def index():
    conn = get_db()
    contacts = conn.execute("SELECT * FROM contacts").fetchall()
    conn.close()
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = (
            request.form["first_name"],
            request.form["last_name"],
            request.form["address"],
            request.form["email"],
            request.form["phone"]
        )
        conn = get_db()
        conn.execute("INSERT INTO contacts (first_name, last_name, address, email, phone) VALUES (?, ?, ?, ?, ?)", data)
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM contacts WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()

    if request.method == "POST":
        data = (
            request.form["first_name"],
            request.form["last_name"],
            request.form["address"],
            request.form["email"],
            request.form["phone"],
            id
        )
        conn.execute("UPDATE contacts SET first_name=?, last_name=?, address=?, email=?, phone=? WHERE id=?", data)
        conn.commit()
        conn.close()
        return redirect("/")

    contact = conn.execute("SELECT * FROM contacts WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", contact=contact)

app.run(debug=True)