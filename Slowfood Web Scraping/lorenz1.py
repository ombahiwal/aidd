

# -*- coding: utf-8 -*-
# Scraping Slowfood Website for Dealer Contacts for Lorenz

import requests
from lxml import html
import csv
import io

print("Initiating Task...\nFetching the URLs of Dealer Contact Pages from main page...")
url = 'https://www.slowfood.de/unterstuetzer/agenturen_verlage'
r = requests.get(url)
print(r)
tree = html.fromstring(r.content)
# print(r.content)
contact_links = tree.xpath('//a[@class="line"]/@href')
print("Contact Links Fetched! \nFetching Contact Details...")
# contact_link = "https://www.slowfood.de/unterstuetzer/haendler/onkel_franz_wenzel_wett_gbr"
export = []
data_list = []
with io.open("sf_germany_agency.csv", "w", newline = "", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Agency or Publisher", "Person(s)", "Phone", "Email", "Website", "Address", "SlowFoodLink"])
    for contact_link in contact_links:
        # for single link
        # Dealer, Phone, Email, Website, address, SlowFoodLink
        data_list = []

        contact_page = requests.get(contact_link)
        # print(contact_page.content)
        page_tree = html.fromstring(contact_page.content)


        # get title
        div_title = page_tree.xpath('//h1[@class="documentFirstHeading"]/text()')
        data_list.extend(div_title)

        # get name and number
        div_name = page_tree.xpath('//div[@class="line-wrapper"]/div[@class="line"]/div[@class="title"]/text()')
        data_list.extend(div_name[0:2])

        # get email and website
        div_links = page_tree.xpath('//div[@class="line-wrapper"]/div[@class="line"]/div[@class="title"]/a/text()')
        data_list.extend(div_links)

        # get address
        div_address = page_tree.xpath('//div[@class="sponsor-address"]/div/text()')
        div_address = ", ".join(div_address)
        data_list.append(div_address)

        # add slow food link to the tuple
        data_list.append(contact_link)

        # make an export master list.
        export.append(data_list)

        # reinitialize to null for the loop
        print("Fetched : ", data_list)

        #write in file

        writer.writerow(data_list)
        print("Written")

        data_list = []

    # Write csv file from export at once.

print("File Generated!\n End of task.")

