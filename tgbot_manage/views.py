from django.shortcuts import render

from tgbot_manage.airtable import login_data


def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        login_data_ = login_data()
        username = request.POST["username"]
        password = request.POST["password"]
        url_user_tg_account = f"https://t.me/{username}"

        context = {
            "password": password,
            "username": username,
            "url_user_tg_account": url_user_tg_account,
        }

        if username in login_data_:
            if login_data_[username] == password:
                return render(request, "index.html", context=context)

        return render(request, "login.html")