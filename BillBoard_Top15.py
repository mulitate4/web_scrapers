import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from time import sleep, strftime

#TO-DO Overwrite the previous file!!!!!

#Download the site.
billboard = requests.get('https://www.billboard.com/charts/hot-100')
print(billboard.status_code)
sleep(1)

try:
	listen_todf = pd.read_excel('C:\\Users\\Goofy\\my scripts\\excel files\\Listen to.xlsx')
	songs_list = listen_todf['songs']
	artists_list = listen_todf['artists']
	

except FileNotFoundError:
	listen_todf = []
	songs_list = []
	artists_list = []


finally:
	#Handles ConnectionError, if raised.
		print("[~] Site downloaded successfully!")
		sleep(1)

		#BS4 object for Billboard.com
		billboardsoup = bs(billboard.content, 'html.parser')


		new_songs_list = []
		new_artists_list = []


		#getting names and artists and printing them
		for x in range(0, 25):
			#gets the song name every iteration
			song_name = billboardsoup.find_all('span', class_="chart-element__information__song text--truncate color--primary")[x].get_text()
			artist_name = billboardsoup.find_all('span', class_="chart-element__information__artist text--truncate color--secondary")[x].get_text()
			print(song_name + ' by ' + artist_name)


			if song_name not in songs_list:
				new_songs_list.append(song_name)
				print('song added')
				
				new_artists_list.append(artist_name)

			sleep(0.1)

		new_database = {'songs' : new_songs_list, 'artists' : new_artists_list}

		#excel formatted list :D
		new_listen_todf = pd.DataFrame(new_database)
		new_listen_todf.index += 1
		new_listen_todf.to_excel("C:\\Users\\Goofy\\my scripts\\excel files\\Listen to.xlsx")
		print(listen_todf)
		print('Done')
		sleep(5)
