import requests

url = input("Which website do you want to check the status of?\n")
page = requests.get(url)
print (page.status_code) 