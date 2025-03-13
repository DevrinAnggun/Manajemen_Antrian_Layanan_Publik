class Queue:
    def __init__(self):
        self.queue = []
        self.status = {}
    
    def add_to_queue(self, customer_id):
        self.queue.append(customer_id)
        self.status[customer_id] = "Menunggu"
    
    def call_next(self):
        if self.queue:
            next_customer = self.queue.pop(0)
            self.status[next_customer] = "Dilayani"
            return next_customer
        return None
    
    def finish_service(self, customer_id):
        if customer_id in self.status:
            self.status[customer_id] = "Selesai"