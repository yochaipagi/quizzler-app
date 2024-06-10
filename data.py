import requests
import json

def get_question_data():
    parameters = {
        "amount": 10,
        "type": "boolean",
    }

    question_data = requests.get(url="https://opentdb.com/api.php" , params=parameters)
    question_data.raise_for_status()
    question_data = question_data.json()
    question_data = question_data["results"]
    return question_data

