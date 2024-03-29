PRODUCTS = [
    {
        "id": 1,
        "name": "black coffee",
        "price": 5
    },
    {
        "id": 2,
        "name": "espresso",
        "price": 6
    },
    {
        "id": 3,
        "name": "cookie",
        "price": 3
    }
]


def get_all_products():
    return PRODUCTS


def get_single_product(id):
    """gets a single product"""
    requested_product = {}
    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product
    return requested_product
