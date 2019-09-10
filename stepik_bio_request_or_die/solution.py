import requests

r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")
while True:
    if r.text[0:1] != "We":
        print("https://stepic.org/media/attachments/course67/3.6.3/" + r.text)
        r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/" + r.text)
    else:
        with open("res.txt", "w") as f:
            f.write(r.text)
        break
