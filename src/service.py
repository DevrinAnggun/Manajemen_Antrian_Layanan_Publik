class Service:
    def __init__(self, service_type, service_name):
        self.service_type = service_type
        self.service_name = service_name
    
    def get_info(self):
        return f"{self.service_name} ({self.service_type})"
