EMPLOYEES = [
    {
        "id": 1,
        "name": "Herman Merman",
        "email": "hermer@gmail.com",
        "hourly_rate": 15
    },
    {
        "id": 2,
        "name": "Sheryll Teryll",
        "email": "sherter@gmail.com",
        "hourly_rate": 15
    }
]


def get_all_employees():
    """doc"""
    return EMPLOYEES


def get_single_employee(id):
    """gets a single employee"""
    requested_employee = {}
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee
