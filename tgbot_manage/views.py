from django.shortcuts import render

from tgbot_manage.airtable import data_in_airtable


def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        data_of_users = data_in_airtable()
        username = request.POST["username"]
        password = request.POST["password"]
        url_user_tg_account = f"https://t.me/{username}"

        if username in data_of_users:
            data_of_user = data_of_users[username]
            if data_of_user["password"] == password:
                context = {
                    "password": password,
                    "username": username,
                    "full_name": f"{data_of_user['first_name']} {data_of_user['last_name']}",
                    "id": f"{data_of_user['id']}",
                    "url_user_tg_account": url_user_tg_account,
                }

                return render(request, "index.html", context=context)

        return render(request, "login.html")
