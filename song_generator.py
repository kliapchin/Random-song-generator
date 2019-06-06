# This function will enable the user to pick a genre out of suggested categories
def pick_genre():
    genre = ''
    categories = ['50s','60s','70s','80s','90s','2000s','top hits','hip hop','house']
    # The user is asked to select a category until a valid genre from the list has been chosen
    while genre == '':
        print('\nPlease choose one of the following categories:')
        print(f'         {categories[0]}         |         {categories[1]}         |         {categories[2]}         ')
        print('_____________________|_____________________|_____________________')
        print(f'         {categories[3]}         |         {categories[4]}         |        {categories[5]}         ')
        print('_____________________|_____________________|_____________________')
        print(f'       {categories[6]}      |       {categories[7]}       |        {categories[8]}      ')
        print('_____________________|_____________________|_____________________')
        genre = input('Which category would you like to choose? Please enter names exactly as listed above. ')
        while genre not in categories:
            genre = input('Please choose a valid category: ')
        else:
            break
    return(genre)

# Gives the user the option to select another song
def repick():
    choose_another_song = input('\nDo you want me to choose another song? ')
    return choose_another_song[0].lower() == 'y'
    
        
    
if __name__ == '__main__':
	import requests
	from bs4 import BeautifulSoup
	import random
	from IPython.display import clear_output
	import emoji


	print("\nHey there! Welcome to your daily song picker. Let's get started", emoji.emojize(':notes:', use_aliases=True), '\n')

	choosing = True
	while choosing:
	    chosen_genre = pick_genre()
	    clear_output()
	    if chosen_genre == '50s':
	        song_list = []
	        page = requests.get('http://www.discjockey.org/top-100-songs-of-the-1950s/')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'musicTable'})
	        table_body = table.find('tbody')
	        rows = table_body.find_all('tr')
	        for row in rows:
	            columns = row.find_all('td')[1:3]
	            columns = [ele.text.strip() for ele in columns]
	            song_list.append([ele for ele in columns if ele])   
	        song = random.choice(song_list)
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print( ", ".join(repr(e) for e in song))
	    elif chosen_genre == '60s':
	        song_list = []
	        page = requests.get('http://www.discjockey.org/top-100-songs-of-the-1960s/')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'musicTable'})
	        table_body = table.find('tbody')
	        rows = table_body.find_all('tr')
	        for row in rows:
	            columns = row.find_all('td')[1:3]
	            columns = [ele.text.strip() for ele in columns]
	            song_list.append([ele for ele in columns if ele])   
	        song = random.choice(song_list)
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print( ", ".join(repr(e) for e in song))
	    elif chosen_genre == '70s':
	        song_list = []
	        page = requests.get('http://www.discjockey.org/top-100-songs-of-the-1970s/')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'musicTable'})
	        table_body = table.find('tbody')
	        rows = table_body.find_all('tr')
	        for row in rows:
	            columns = row.find_all('td')[1:3]
	            columns = [ele.text.strip() for ele in columns]
	            song_list.append([ele for ele in columns if ele])   
	        song = random.choice(song_list)
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print( ", ".join(repr(e) for e in song))
	    elif chosen_genre == '80s':
	        song_list = []
	        page = requests.get('http://www.discjockey.org/top-100-songs-of-the-1980s/')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'musicTable'})
	        table_body = table.find('tbody')
	        rows = table_body.find_all('tr')
	        for row in rows:
	            columns = row.find_all('td')[1:3]
	            columns = [ele.text.strip() for ele in columns]
	            song_list.append([ele for ele in columns if ele])   
	        song = random.choice(song_list)
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print( ", ".join(repr(e) for e in song))
	    elif chosen_genre == '90s':
	        song_list = []
	        page = requests.get('http://www.discjockey.org/top-100-songs-of-the-1990s/')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'musicTable'})
	        table_body = table.find('tbody')
	        rows = table_body.find_all('tr')
	        for row in rows:
	            columns = row.find_all('td')[1:3]
	            columns = [ele.text.strip() for ele in columns]
	            song_list.append([ele for ele in columns if ele])   
	        song = random.choice(song_list)
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print( ", ".join(repr(e) for e in song))
	    elif chosen_genre == '2000s':
	        song_list = []
	        page = requests.get('http://www.discjockey.org/top-100-songs-of-the-2000s/')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'musicTable'})
	        table_body = table.find('tbody')
	        rows = table_body.find_all('tr')
	        for row in rows:
	            columns = row.find_all('td')[1:3]
	            columns = [ele.text.strip() for ele in columns]
	            song_list.append([ele for ele in columns if ele])   
	        song = random.choice(song_list)
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print( ", ".join(repr(e) for e in song))
	    elif chosen_genre.lower() == 'top hits':
	        song_list = []
	        page = requests.get('https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_top-ten_singles_in_2018')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'wikitable sortable'})
	        table_body = table.find('tbody')
	        rows = table_body.find_all('tr')
	        rowspan = []

	        for row_num, row in enumerate(rows):
	            for col_no, data in enumerate(row.find_all('td')):
	                if data.has_attr("rowspan"):
	                    rowspan.append((row_num, col_no, int(data["rowspan"]), data.get_text()))
	                    rowspan = [list(elem) for elem in rowspan]
	        for row in rows: 
	            columns = row.find_all('td')[:3]
	            columns = [ele.text.strip() for ele in columns]
	            song_list.append([ele for ele in columns if ele])          

	        if rowspan:
	            for i in rowspan:
	                for j in range(1,i[2]):
	                    song_list[i[0]+j].insert(i[1],i[3])

	        updated_song_list = [x for x in song_list if x != []]
	        updated_song_list = [song[1:3] for song in updated_song_list]
	        updated_song_list
	        song = random.choice(updated_song_list)
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print( ", ".join(repr(e) for e in song))
	    elif chosen_genre.lower() == 'hip hop':
	        song_list = []
	        page = requests.get('https://en.wikipedia.org/wiki/List_of_Billboard_number-one_rap_singles_of_the_2000s')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'plainrowheaders'})
	        table_body = table.find('tbody')
	        rows = table_body.find_all('tr')[1::]
	        for row in rows: 
	            columns = row.find_all(['th','td'])[0:2]
	            columns = [ele.text.strip() for ele in columns]
	            song_list.append([ele for ele in columns if ele])
	        song = random.choice(song_list)
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print( ", ".join(repr(e) for e in song))
	    elif chosen_genre.lower() == 'house':
	        song_list = []
	        page = requests.get('https://digitaldreamdoor.com/pages/best_electronic_dance_songs_2000s.html')
	        soup = BeautifulSoup(page.text, 'html.parser')
	        table = soup.find('table', attrs={'class':'t7'})
	        table_body = table.find('tbody')
	        rows = table.find_all('tr')[1:2]

	        for row in rows: 
	            columns = row.find_all('td')
	            columns = [ele.text.split('\n') for ele in columns][0:1]
	            song_list.append([ele for ele in columns if ele])
	        updated_song_list = [x for x in song_list[0][0] if x != '']
	        updated_song_list = ([x.replace('\xa0', '') for x in updated_song_list])


	        song = random.choice(updated_song_list)
	        song = song[3::]
	        print('Your song is...', emoji.emojize(':drum:', use_aliases=True), ': ')
	        print(song)
	    else:
	        print('Another genre has been chosen')

	    
	    if not repick():
	        clear_output()
	        print('\nThanks for stopping by! Good night', emoji.emojize(':sleeping:', use_aliases=True))
	        break


