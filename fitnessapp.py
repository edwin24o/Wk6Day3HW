from flask import Flask
from connect import db
from flask import request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Fitness API is running!"


@app.route('/members', methods=['GET'])
def get_members():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Members")
    members = cursor.fetchall()
    cursor.close()
    return jsonify(members)

@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    cursor = db.cursor()
    query = "INSERT INTO Members (name, email, membership_type) VALUES (%s, %s, %s)"
    cursor.execute(query, (data['name'], data['email'], data['membership_type']))
    db.commit()  
    cursor.close()
    return jsonify({"message": "Member added successfully!"}), 201

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
    member = cursor.fetchone()
    cursor.close()
    
    if member:
        return jsonify(member)
    else:
        return jsonify({"message": "Member not found"}), 404

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    cursor = db.cursor()
    query = "UPDATE Members SET name = %s, email = %s, membership_type = %s WHERE id = %s"
    cursor.execute(query, (data['name'], data['email'], data['membership_type'], id))
    db.commit()
    cursor.close()
    return jsonify({"message": "Member updated successfully!"})

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    cursor = db.cursor()
    sql = "DELETE FROM Members WHERE id = %s"
    cursor.execute(sql, (id,))
    db.commit()
    cursor.close()
    return jsonify({"message": "Member deleted successfully!"})

@app.route('/workoutsessions', methods=['POST'])
def add_workout_session():
    data = request.json
    cursor = db.cursor()
    query = "INSERT INTO WorkoutSessions (member_id, session_date, workout_type, duration) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (data['member_id'], data['session_date'], data['workout_type'], data['duration']))
    db.commit()
    cursor.close()

    return jsonify({"message": "Workout session added!"}), 201

@app.route('/workoutsessions', methods=['GET'])
def get_workout_sessions():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM WorkoutSessions")
    workout_sessions = cursor.fetchall()
    cursor.close()
    return jsonify(workout_sessions)

@app.route('/workoutsessions/<int:id>', methods=['PUT'])
def update_workout_session(id):
    data = request.json
    cursor = db.cursor()
    query = "UPDATE WorkoutSessions SET session_date = %s, workout_type = %s, duration = %s WHERE id = %s"
    cursor.execute(query, (data['session_date'], data['workout_type'], data['duration'], id))
    db.commit()
    cursor.close()
    return jsonify({"message": "Workout session updated successfully!"})

@app.route('/workoutsessions/<int:id>', methods=['DELETE'])
def delete_workout_session(id):
    cursor = db.cursor()
    sql = "DELETE FROM WorkoutSessions WHERE id = %s"
    cursor.execute(sql, (id,))
    db.commit()
    cursor.close()
    return jsonify({"message": "Workout session deleted successfully!"})


if __name__ == '__main__':
    app.run(debug=True)

