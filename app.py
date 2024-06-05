from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('alumni.db')
print("Connected to SQLite database")

# Create tables if they don't exist (replace with your desired tables)
conn.execute('''CREATE TABLE IF NOT EXISTS alumni (
                  name TEXT,
                  graduation_year INTEGER,
                  email TEXT,
                  company TEXT,
                  position TEXT,
                  linkedin_url TEXT
                )''')

# Sample data (replace with functions to add/edit alumni info)
conn.execute("INSERT INTO alumni VALUES ('John Doe', 2020, 'johndoe@email.com', 'ACME Inc.', 'Software Engineer', 'https://www.linkedin.com/in/johndoe')")
conn.execute("INSERT INTO alumni (name, graduation_year, email, company, position) VALUES (?, ?, ?, ?, ?)", ("Jane Doe", 2022, "janedoe@email.com", 'Technovation Ltd.', 'Data Analyst'))
conn.commit()

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    name = request.form["name"]
    graduation_year = request.form["graduation_year"]
    email = request.form["email"]
    company = request.form["company"]
    position = request.form["position"]
    linkedin_url = request.form["linkedin_url"]
    # Add data to database (implement logic)
    conn.execute("INSERT INTO alumni VALUES (?, ?, ?, ?, ?, ?)", (name, graduation_year, email, company, position, linkedin_url))
    conn.commit()
    return render_template("registration_success.html")
  else:
    return render_template("register.html")

@app.route("/alumni_list")
def alumni_list():
  # Fetch alumni data from database
  cursor = conn.execute("SELECT * FROM alumni")
  alumni = cursor.fetchall()
  return render_template("alumni_list.html", alumni=alumni)

if __name__ == "__main__":
  app.run(debug=True)