from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Inisialisasi database SQLite
def init_db():
    with sqlite3.connect("queue.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS queue (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                queue_number TEXT,
                priority TEXT
            )
        """)
        conn.commit()

init_db()

PRIORITY_RULES = {
    "EMERGENCY": 1,
    "VIP": 2,
    "REGULAR": 3,
}

class QueueSystem:
    def __init__(self):
        self.counter = {"EMERGENCY": 1, "VIP": 1, "REGULAR": 1}
    
    def take_queue(self, priority):
        priority = priority.upper()
        if priority not in self.counter:
            priority = "REGULAR"
        
        queue_number = f"{priority[:1]}{self.counter[priority]}"
        self.counter[priority] += 1

        with sqlite3.connect("queue.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO queue (queue_number, priority) VALUES (?, ?)", (queue_number, priority))
            conn.commit()
        
        return queue_number

    def get_queues(self):
        with sqlite3.connect("queue.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT queue_number, priority FROM queue ORDER BY id ASC")
            queues = cursor.fetchall()

        result = {"EMERGENCY": [], "VIP": [], "REGULAR": []}
        for queue_number, priority in queues:
            result[priority].append(queue_number)
        
        return result
    
    def call_next(self):
        with sqlite3.connect("queue.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, queue_number, priority FROM queue
                ORDER BY
                    CASE priority 
                        WHEN 'EMERGENCY' THEN 1 
                        WHEN 'VIP' THEN 2 
                        ELSE 3 
                    END, id ASC
                LIMIT 1
            """)
            next_queue = cursor.fetchone()

            if next_queue:
                queue_id, queue_number, _ = next_queue
                cursor.execute("DELETE FROM queue WHERE id = ?", (queue_id,))
                conn.commit()
                return queue_number
        
        return None

queue_system = QueueSystem()

@app.route("/queue/take", methods=["POST"])
def take_queue():
    data = request.get_json()
    priority = data.get("priority", "REGULAR").upper()
    queue_number = queue_system.take_queue(priority)
    return jsonify({"message": "Nomor antrian berhasil diambil", "queue_number": queue_number})

@app.route("/queue", methods=["GET"])
def get_queue():
    return jsonify(queue_system.get_queues())

@app.route("/queue/call", methods=["POST"])
def call_queue():
    next_queue = queue_system.call_next()
    if next_queue:
        return jsonify({"message": "Memanggil nomor antrian", "queue_number": next_queue})
    return jsonify({"message": "Tidak ada antrian"})

@app.route("/queue/reset", methods=["POST"])
def reset_queue():
    with sqlite3.connect("queue.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM queue")  # Hapus semua data antrian
        conn.commit()
    
    queue_system.counter = {"EMERGENCY": 1, "VIP": 1, "REGULAR": 1}  # Reset nomor antrian

    return jsonify({"message": "Antrian telah direset"})

if __name__ == "__main__":
    app.run(debug=True)
