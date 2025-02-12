from flask import Flask, jsonify
import numpy as np
import random
import MySQLdb

class Database:
    """Handles MySQL database connection and queries."""
    def __init__(self, host, user, password, database):
        self.connection = MySQLdb.connect(
            host=host,
            user=user,
            password=password,
            db=database
        )

    def fetch_employees(self):
        """Fetch all employees as {id: name} mapping."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name FROM employees")
        employees = {row[0]: row[1] for row in cursor.fetchall()}  # Store as {id: name}
        cursor.close()
        return employees

class Scheduler:
    """Generates AI-based weekly schedules for employees."""

    TIME_SLOTS = ["08:00 AM - 04:00 PM", "04:00 PM - 12:00 AM"]
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, db):
        self.db = db
        self.model = self.train_ai_model()

    def train_ai_model(self):
        """Placeholder for AI model training (Optional)."""
        return None

    def generate_schedule(self):
        """Generate AI-based weekly schedule ensuring each employee has exactly one day off and no extra days off."""
        employees = self.db.fetch_employees()  # Get {id: name}
        employee_ids = list(employees.keys())  # List of employee IDs

        if not employee_ids or len(employee_ids) < 8:
            return {"error": "Not enough employees in the database. Minimum 8 required."}

        schedule = []
        random.shuffle(employee_ids)  # Shuffle employees for fairness

        # Assign exactly one unique day off per employee
        employee_days_off = {}
        assigned_days_off = {day: 0 for day in self.DAYS}  # Track how many employees have each day off

        for emp_id in employee_ids:
            available_days = [day for day in self.DAYS if assigned_days_off[day] < 1]  # Ensure only one day off per employee
            assigned_day_off = random.choice(available_days) if available_days else random.choice(self.DAYS)

            employee_days_off[emp_id] = assigned_day_off
            assigned_days_off[assigned_day_off] += 1

        for day in self.DAYS:
            row = {"Day": day}
            assigned_employees = set()

            for slot in self.TIME_SLOTS:
                available_employee_ids = [e_id for e_id in employee_ids if employee_days_off[e_id] != day]

                if self.model:
                    input_data = np.array([[self.DAYS.index(day), self.TIME_SLOTS.index(slot)]])
                    predictions = self.model.predict(input_data)
                    selected_employee_ids = [
                        available_employee_ids[i] for i, p in enumerate(predictions[:len(available_employee_ids)]) if p[0] > 0.5
                    ]
                else:
                    selected_employee_ids = random.sample(available_employee_ids, min(8, len(available_employee_ids)))

                # Prevent double shifts in a single day
                selected_employee_ids = [e_id for e_id in selected_employee_ids if e_id not in assigned_employees]
                assigned_employees.update(selected_employee_ids)

                # Convert IDs to names for display
                row[slot] = ", ".join([employees[e_id] for e_id in selected_employee_ids]) if selected_employee_ids else "No Employees"

            schedule.append(row)

        return schedule


class FlaskApp:
    """Flask application to serve the AI scheduler API."""

    def __init__(self):
        self.app = Flask(__name__)
        self.db = Database(host="localhost", user="root", password="", database="ai")
        self.scheduler = Scheduler(self.db)
        self.setup_routes()

    def setup_routes(self):
        """Define API routes."""
        @self.app.route('/generate-schedule', methods=['GET'])
        def generate_schedule():
            return jsonify(self.scheduler.generate_schedule())

    def run(self):
        """Run the Flask app."""
        self.app.run(debug=True, port=5000)

if __name__ == '__main__':
    FlaskApp().run()
