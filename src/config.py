class Config:
    max_customers_per_service = 10
    operational_hours = "08:00 - 17:00"
    
    @classmethod
    def update_max_customers(cls, new_max):
        cls.max_customers_per_service = new_max