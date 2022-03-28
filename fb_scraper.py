import csv

from bs4 import BeautifulSoup

rows = []
foldername = "facebook-html"

with open("%s/ads_information/advertisers_using_your_activity_or_information.html" % foldername) as page:
    soup = BeautifulSoup(page,  "html.parser")
    contents = soup.find("div", class_="_a706")
    ad_list = contents.find_all( "tr" , class_="_1isx")

    for item in ad_list:
        for second in item.find_all("td"):
            advert = item.find("strong").get_text()
        metadata = item.find("td", style="text-align:center").get_text()
        metadata2 = item.find("td", style="text-align:center").get_text()
        row = { "advert": advert,
                    "metadata": metadata,
                    "metadata2": metadata2
              }
        rows.append(row)

with open("%s-all-advertisers.csv" % foldername, "w+") as csvfile:
    fieldnames = ["advert", "metadata", "metadata2"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        writer.writerow(row)