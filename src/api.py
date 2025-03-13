from asyncio import Queue
from flask import Flask, jsonify # type: ignore

app = Flask(__name__)
queue_system = Queue()

@app.route("/queue/add/<customer_id>", methods=["POST"])
def add_to_queue(customer_id):
    queue_system.add_to_queue(customer_id)
    return jsonify({"message": "Nomor antrian diberikan", "customer_id": customer_id})

@app.route("/queue/call", methods=["GET"])
def call_next():
    next_customer = queue_system.call_next()
    if next_customer:
        return jsonify({"message": "Pelanggan berikutnya dipanggil", "customer_id": next_customer})
    return jsonify({"message": "Tidak ada antrian"})

if __name__ == "__main__":
    app.run(debug=True)
