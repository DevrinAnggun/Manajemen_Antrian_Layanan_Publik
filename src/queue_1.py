class QueueSystem:
    def __init__(self):
        self.queues = {"VIP": [], "REGULAR": []}
        self.counter = {"VIP": 1, "REGULAR": 1}

    def take_queue(self, priority):
        if priority not in self.queues:
            priority = "REGULAR"  # Jika input salah, default ke REGULAR
        
        queue_number = f"{priority[:1]}{self.counter[priority]}"
        self.queues[priority].append(queue_number)
        self.counter[priority] += 1
        return queue_number

    def get_queues(self):
        return self.queues

def reset_queue(self):
    conn = sqlite3.connect("queue.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM queue")  # Menghapus semua data antrian
    conn.commit()
    conn.close()
    self.counter = {"EMERGENCY": 1, "VIP": 1, "REGULAR": 1}  # Reset counter
