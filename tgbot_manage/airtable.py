import requests

AIRTABLE_BASE_ID = "app3vcxFEDlEdStCB"
AIRTABLE_NAME = "django-tgbot"
AIRTABLE_API_KEY = "keyCYj6sE0mNnqoJw"

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


def usernames_in_airtable():
    all_data = retrieve_records()
    username = [data["fields"]["username"] for data in all_data["records"]]
    return username