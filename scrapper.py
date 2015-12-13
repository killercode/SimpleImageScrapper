__author__ = "Diogo Alves"
import requests
import bs4

def percentage(part, whole):
  return 100 * float(part)/float(whole)

response = requests.get("http://sic.sapo.pt")
soup = bs4.BeautifulSoup(response.text, "html5lib")

images = soup.select("img[src]")
png = 0
gif = 0
jpg = 0
other = 0
total = 0
for image in images:
    if ".png" in image["src"].lower():
       png += 1
    elif ".gif" in image["src"].lower():
        gif += 1
    elif ".jpg" in image["src"].lower():
        jpg +=1
    else:
        other +=1
        print image["src"]
    total +=1

percpng = (png / total) * 100
percgif = (gif / total) * 100
percjpg = (jpg / total) * 100
percother = (other / total) * 100

print "png: " + str(png) + " " + str(percentage(png, total)) + "%"
print "gif: " + str(gif) + " " + str(percentage(gif, total)) + "%"
print "jpg: " + str(jpg) + " " + str(percentage(jpg, total)) + "%"
print "other: " + str(other) + " " + str(percentage(other, total)) + "%"
print "total: " + str(total)