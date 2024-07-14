"""This a library that mean't to access files from github repo without opening it again and again"""

import requests
url = "https://raw.githubusercontent.com/Anupam1707/"
repos = {
    "py" : "Python_Programmes",
    "we" : "weather-app-py",
    "aiu" : "ai",
    "ds" : "DataSense",
    "spy" : "SecuriPy",
    "docs" : "docs",
    "vue" : "vue",
    "LT" : "weather_app_learntricks"
}

def fetch(filename, repo, image = False):
    repo_name = repos.get(repo, repo)
    link = f"{url + repo_name}/main/{filename}"
    page = requests.get(f"{url + repos[repo]}/main/{filename}")
    # print(link)
    if image == False:
        return page.text
    else :
        return page.content

def save(file, name):
    with open(f"{name}", "w", encoding = "utf-8", newline = "") as f:
        f.writelines(file)
