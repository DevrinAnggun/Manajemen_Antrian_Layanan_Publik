PRIORITY_RULES = {
    "emergency": 1,
    "vip": 2,
    "regular": 3,
}

def get_priority_level(customer_type):
    return PRIORITY_RULES.get(customer_type, 3)
