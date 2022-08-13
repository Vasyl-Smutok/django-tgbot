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


def data_in_airtable(field):
    all_data = retrieve_records()
    data_ = [data["fields"][field] for data in all_data["records"]]
    return data_


def login_data():
    usernames = data_in_airtable("username")
    passwords = data_in_airtable("password")

    return dict(zip(usernames, passwords))


if __name__ == '__main__':
    print(data_in_airtable("username"))
