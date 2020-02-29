from cs50 import SQL

db=SQL("sqlite:///new.db")

rows = db.execute("select * from registrants")

for row in rows:
    print(f"{row['name']} registerd")


if __name__ == "__main__":
    app.run(debug=True)