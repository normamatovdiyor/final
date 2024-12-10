from flask import Flask, render_template, request
import pg8000

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the level from the form
        level = request.form["level"]
        return render_template("timetable.html", level=level, data=[], message="Loading timetable...")

    return render_template("index.html")

@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get('level')  # Get level from the query parameters
    if not level:
        return "Level not provided", 400

    try:
        # Connect to the PostgreSQL database
        conn = pg8000.connect(
<<<<<<< HEAD
            user="postgres",
            password="postgres",
            host="database-1.cr8cicwiwx39.eu-north-1.rds.amazonaws.com",
            port=5432,
            database="postgres"
=======
            user="postgres", 
            password="postgres", 
            host="database-1.cr8cicwiwx39.eu-north-1.rds.amazonaws.com", 
            port=5432, 
            database="database-1"
>>>>>>> 0472d038c33f7bf44bca7f079bf30924e91696d7
        )

        cur = conn.cursor()
        query = "SELECT * FROM timetable WHERE level = %s;"   # Query with placeholder
        cur.execute(query, (level,))
        rows = cur.fetchall()

        # Pass data to the template
        if rows:
            return render_template("timetable.html", level=level, data=rows, message="")
        else:
            return render_template("timetable.html", level=level, data=[], message="No data found for this level.")
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
