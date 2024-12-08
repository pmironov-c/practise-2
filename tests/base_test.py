import os
import pytest
from datetime import datetime


class BaseTest:
    url = os.environ.get("BASE_URL")
    user_login = os.environ.get("USER_LOGIN")
    user_password = os.environ.get("USER_PASSWORD")

    lead_info = {
        "first_name": "John",
        "last_name": f"Doe 42 {str(datetime.now())}",
        "phone_number": "8 800 555 35 35",
    }
    lead_info["lead_name"] = f"{lead_info["first_name"]} {lead_info["last_name"]}"

    account_info = {
        "name": f"Bob 666 {str(datetime.now())}",
        "phone_number": "9 900 666 56 56",
    }
