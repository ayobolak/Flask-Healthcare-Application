from flask import Flask, render_template, request
from pymongo import MongoClient

application = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["income_survey"]
collection = db["responses"]

@application.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = int(request.form.get("age", 0))
        gender = request.form.get("gender")
        total_income = float(request.form.get("total_income", 0))

        # Expense categories
        selected_expenses = request.form.getlist("expense_categories")
        expenses = {}
        for category in ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]:
            if category in selected_expenses:
                expenses[category] = float(request.form.get(category, 0))

        user_data = {
            "age": age,
            "gender": gender,
            "total_income": total_income,
            "expenses": expenses
        }

        collection.insert_one(user_data)
        return "Thank you for submitting your data!"

    return render_template("index.html")

# ✅ Submissions route (MUST come before app.run)
@application.route("/submissions")
def submissions():
    data = list(collection.find())
    return render_template("submissions.html", entries=data)

# ✅ Start the app (only once)
if __name__ == "__main__":
    application.run(debug=True)
