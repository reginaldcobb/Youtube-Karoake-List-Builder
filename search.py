import urllib.request
from bs4 import BeautifulSoup
import csv
import sys
import time
import datetime

# with open('video.csv', mode='r') as csv_file:
with open('artist_inputs_2.csv', mode='r') as csv_file:
# with open('artist_inputs_test.csv', mode='r') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'{", ".join(row)}')
            line_count += 1
        # print(f'\t{row["artist"]} \t{row["title"]}  \t{row["type"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

    line_count = 0
    with open('links.csv', mode='w') as links:
        links_writer = csv.writer(links, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # print("here1")
        csv_file.seek(0)
        for row in csv_reader:
            print(f'\t{row["artist"]} \t{row["artist"]}  \t{row["type"]}.')
            line_count += 1
            print (datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S"))
            print ("sleeping 5 seconds")
            time.sleep(30)
            print ("waking up")

            # if line_count % 100 < 1:
            #     print (datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S"))
            #     print ('taking a  minute break')
            #     time.sleep(3600)
            #     print ("break over")
            #     print (datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S"))

            textToSearchArtist = row["artist"]
            textToSearchSong = row["title"]
            print("processing video #" + str(line_count) + " - " + textToSearchArtist + " " + textToSearchSong )
            sys.stdout.flush()
            textToSearch = textToSearchArtist + ' ' + textToSearchSong + ' ' + row["type"]
            # print(textToSearch)
            query = urllib.parse.quote(textToSearch)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
                    # print(textToSearchArtist + ';' + textToSearchSong + ';' + 'https://www.youtube.com' + vid['href'])
                    youtube_link = 'https://www.youtube.com' + vid['href']
                    links_writer.writerow([textToSearchArtist, textToSearchSong, youtube_link])
        print("finished processing")
        print (datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S"))
        