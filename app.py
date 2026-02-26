from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database (Python list)
classrooms = []
# Expected structure:
# {
#     "roomId": "STR",
#     "capacity": INT,
#     "floorNo": INT,
#     "nearWashroom": BOOL
# }

def allocate_rooms(total_students):
    # Sort classrooms by floorNo ascending (prefer lower floors), then capacity descending (min rooms)
    sorted_rooms = sorted(classrooms, key=lambda r: (r['floorNo'], -r['capacity']))
    
    allocated = []
    current_capacity = 0

    for room in sorted_rooms:
        if current_capacity >= total_students:
            break
        allocated.append(room)
        current_capacity += room['capacity']

    if current_capacity < total_students:
        return None

    return allocated

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-room", methods=["GET", "POST"])
def add_room():
    error = None
    if request.method == "POST":
        room_id = request.form.get("roomId", "").strip()
        capacity = request.form.get("capacity", "")
        floor_no = request.form.get("floorNo", "")
        near_washroom = request.form.get("nearWashroom") == "on"

        if not room_id or not capacity or not floor_no:
            error = "Missing required fields"
        else:
            # Check for duplicate roomId
            if any(r["roomId"] == room_id for r in classrooms):
                error = f"Room ID '{room_id}' already exists"
            else:
                try:
                    capacity = int(capacity)
                    floor_no = int(floor_no)
                    
                    if capacity <= 0:
                        error = "Capacity must be greater than 0"
                    elif floor_no < 0:
                        error = "Floor number cannot be negative"
                    else:
                        classrooms.append({
                            "roomId": room_id,
                            "capacity": capacity,
                            "floorNo": floor_no,
                            "nearWashroom": near_washroom
                        })
                        return redirect(url_for('rooms'))
                except ValueError:
                    error = "Capacity and Floor No must be valid numbers"

    return render_template("add_room.html", error=error)

@app.route("/rooms")
def rooms():
    return render_template("rooms.html", classrooms=classrooms)

@app.route("/allocate", methods=["GET", "POST"])
def allocate():
    allocated_rooms = None
    error = None
    total_students = ""

    if request.method == "POST":
        total_students = request.form.get("totalStudents", "").strip()
        
        if not total_students:
            error = "Please enter a number of students"
        else:
            try:
                num_students = int(total_students)
                if num_students <= 0:
                    error = "Number of students must be greater than 0"
                else:
                    allocated_rooms = allocate_rooms(num_students)
                    if allocated_rooms is None:
                        error = "Not enough seats available"
            except ValueError:
                error = "Invalid number format"

    return render_template("allocate.html", allocated_rooms=allocated_rooms, error=error, total_students=total_students)

if __name__ == "__main__":
    app.run(debug=True)
