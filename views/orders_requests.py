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

def create_order(order):
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

def delete_order(id):
    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index
            
    if order_index >= 0:
        ORDERS.pop(order_index)

