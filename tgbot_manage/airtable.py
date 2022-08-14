import requests

from RegistrationViaTelegram.settings import (AIRTABLE_BASE_ID, AIRTABLE_NAME, AIRTABLE_API_KEY)

endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_NAME}/"


def create_records(data):
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
      "records": [
        {
          "fields": data
        },
      ]
    }
    requests.post(endpoint, json=data, headers=headers)


def retrieve_records():
    headers = {
      'Authorization': f'Bearer {AIRTABLE_API_KEY}',
    }
    response = requests.request("GET", endpoint, headers=headers)
    return response.json()


def data_in_airtable():
    all_data = retrieve_records()
    return {
        data["fields"]['username']:
            data["fields"] for data in all_data["records"]
    }


if __name__ == '__main__':
    print(data_in_airtable())
