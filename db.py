import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='n21902',
    db='karoake_songs')
cursor = mydb.cursor()
i = 0

csv_data = csv.reader(file('C:/Users/Reggie/OneDrive/Code/python/youtube/Master Links_with_Thumbnail.csv'))
for row in csv_data:
    print(i)
    i = i + 1
    cursor.execute('INSERT INTO songs( id,artist,title,genre,date,not_karoake,youtube_ID,link,big_thumb,default_thumb,mqdefault_thumb,maxresdefault_thumb,one_thumb,two_thumb,three_thumb,active,rank,score,vote_total,vote1,vote2,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,info1,info2,info3,info4,info5,info6,info7,info8,info9,info10)' 
          'VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")', row)
#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")