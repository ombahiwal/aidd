

# -*- coding: utf-8 -*-
# Scraping Slowfood Website -  Contacts for Lorenz
# 31st Jul
import requests
from lxml import html
import csv
import io
import numpy as np

print("Initiating Task...\nFetching the URLs of Dealer Contact Pages from main page...")
page = 0
data = []
with io.open("sf_presidia_global_2.csv", "w", newline = "", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Slowfood Link', 'Category', 'Country', 'Presidium', 'Coordinator(s) Contact', 'Email | Website'])
    for page in range(57, 60):
        info = []
        numpy_array = 0
        transpose = 0
        url = 'https://www.fondazioneslowfood.com/en/slow-food-presidia/?fwp_paged='+str(page)
        r = requests.get(url)
        print(r)
        tree = html.fromstring(r.content)
        # print(r.content)

        # info list master in loop

        # info links
        info_links = tree.xpath('//span[@class="info-btn"]/a/@href')
        print("Contact Links Fetched for Page : "+str(page))
        # info_link = "https://www.fondazioneslowfood.com/en/slow-food-presidia/herat-abjosh-raisin/"
        info.append(info_links)

        categories = tree.xpath('//span[@class="entry-term settore entry-term-last"]/a/text()')
        info.append(categories)

        info_countries = tree.xpath('//span[@class="entry-term nazione entry-term-first"]/a/text()')
        info.append(info_countries)

        info_region = tree.xpath('//span[@class="entry-term regione"]/a/text()')
        # info.append(info_region)

        # print(info)

        transpose = list(map(list, zip(*info)))
        info = transpose[:]

        # print(info)
        contacts = []
        for k in range(0, len(info_links)):
            # Contact Info URL
            # first URL of the list. - info_link

            r2 = requests.get(info_links[k])
            # print(r2)
            tree_info = html.fromstring(r2.content)
            # print("Contact Fetched for Page : ", page)
            # info_link = "https://www.fondazioneslowfood.com/en/slow-food-presidia/herat-abjosh-raisin/"

            # fetch contact info
            info_contact = []

            info_title = tree_info.xpath('//h1[@class="entry-title"]/text()')

            info_contact.extend(info_title)
            info_contact_name = tree_info.xpath('//div[@id="info"]/text()')
            info_contact_name = [x for x in info_contact_name if x != ' ']
            info_contact_name = [", ".join(info_contact_name)]

            info_contact.extend(info_contact_name)
            info_contact_email_web = tree_info.xpath('//div[@id="info"]/a/text()')
            info_contact_email_web = [" | ".join(info_contact_email_web)]
            info_contact.extend(info_contact_email_web)

            # print(info_contact)
            print("Info contact : ", info_contact)
            contacts.append(info_contact)

        for k in range(0, len(info)):
            info[k] = info[k] + contacts[k]
            for y in range(len(info[k])):
                if isinstance(type(u"t"), type(info[k][y])):
                    print(info[k][y])
                    info[k][y].decode('utf-8', 'ignore')
            writer.writerow(info[k])

        # print("info : ", info)

        data.append(info)
        # print(data)


    data = data[0]




print('Task Done')
"""

export = []
data_list = []
with io.open("sf_presidia_global.csv", "w", newline = "", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Supporter", "Person(s)", "Phone", "Email", "Website", "Address", "SlowFoodLink"])
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

"""