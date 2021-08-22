# Billboard-top-100-playlist

Link to Spotipy docs: https://spotipy.readthedocs.io/en/2.19.0/

This project uses Web scraping and spotipy API to do the following:

-asks the user for a year which he would like to get a playlist for

-the script will scrape https://www.billboard.com/charts/hot-100/ for the title of each song from that year

-then with the spotipy API will search for every title in the Spotify library and make a playlist for the user

-the script will ignore a title if it is not on spotify
