import requests
from welcome import WelcomePage

welcome = WelcomePage()
CATEGORY = welcome.q_category
NUMBERS = welcome.q_num

parameters = {
    "amount": NUMBERS,
    "type": "boolean",
    "category": CATEGORY
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
