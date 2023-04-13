ORDERS = [
    {
        "id": 1,
        "product_id": 1,
        "employee_id": 1,
        "timestamp": "20230412"
    },
    {
        "id": 2,
        "product_id": 2,
        "employee_id": 2,
        "timestamp": "20230412"
    }
]


def get_all_orders():
    return ORDERS


def get_single_order(id):
    """gets a single order"""
    requested_order = {}
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order
    return requested_order
