from flask import Flask, jsonify
import tensorflow as tf
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
        """Fetch all employee names from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM employees")
        employees = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return employees

    def fetch_past_schedules(self):
        """Fetch past work schedules to train AI."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT employee_name, day, time_slot FROM schedules")
        past_schedules = cursor.fetchall()
        cursor.close()

        # Convert schedule data into numeric format for AI training
        days_map = {day: i for i, day in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}
        slots_map = {
            "08:00 AM - 11:00 AM": 0,
            "11:00 AM - 02:00 PM": 1,
            "02:00 PM - 05:00 PM": 2,
            "05:00 PM - 08:00 PM": 3
        }

        x_train = []
        y_train = []

        for emp, day, slot in past_schedules:
            x_train.append([days_map[day], slots_map[slot]])
            y_train.append(1)  # Label: Employee was assigned

        return np.array(x_train), np.array(y_train)

class Scheduler:
    """Generates AI-based weekly schedules for employees."""

    TIME_SLOTS = [
        "08:00 AM - 11:00 AM",
        "11:00 AM - 02:00 PM",
        "02:00 PM - 05:00 PM",
        "05:00 PM - 08:00 PM"
    ]

    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, db):
        self.db = db
        self.model = self.train_ai_model()

    def train_ai_model(self):
        """Train TensorFlow model based on past work schedules."""
        x_train, y_train = self.db.fetch_past_schedules()

        if len(x_train) == 0:
            print("No past data available! AI will use random scheduling.")
            return None

        model = tf.keras.Sequential([
            tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),
            tf.keras.layers.Dense(5, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=100, verbose=0)

        return model

    def generate_schedule(self):
        """Generate AI-based weekly schedule ensuring each employee has one day off."""
        employees = self.db.fetch_employees()

        if not employees or len(employees) < 6:
            return {"error": "Not enough employees in the database. Minimum 6 required."}

        # Assign a random day off for each employee
        employee_days_off = {emp: random.choice(self.DAYS) for emp in employees}

        schedule = []
        for day in self.DAYS:
            row = {"Day": day}
            available_employees = [e for e in employees if employee_days_off[e] != day]

            for slot in self.TIME_SLOTS:
                if self.model:
                    # AI predicts which employees should work
                    input_data = np.array([[self.DAYS.index(day), self.TIME_SLOTS.index(slot)]])
                    predictions = self.model.predict(input_data)
                    selected_employees = [available_employees[i] for i, p in enumerate(predictions[:len(available_employees)]) if p[0] > 0.5]
                else:
                    selected_employees = random.sample(available_employees, min(6, len(available_employees)))  # Changed from 5 to 6

                row[slot] = ", ".join(selected_employees) if selected_employees else "No Employees"
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


# Start the Flask app
if __name__ == '__main__':
    FlaskApp().run()
