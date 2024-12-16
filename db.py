import sqlite3


conn = sqlite3.connect('favorites.db', check_same_thread=False)
cursor = conn.cursor()






def get_shows_array_from_rating(rating):
    shows = cursor.execute("""SELECT Title FROM favorites WHERE IMDbRating >= ?""", (rating,))
    show_titles = [row[0] for row in shows.fetchall()]  # Fetch all results at once
    print(show_titles)
    return show_titles