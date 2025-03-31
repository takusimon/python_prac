def write_liked_songs_to_file(liked_songs,file_name):
    with open(file_name,'w')as f:
        f.write("Liked Songs:\n")
        for title, artist in liked_songs.items():
            f.write(f'{title} by {artist}\n')
        



songs = {'hello':'adele',
               'best part of life':'st jhn'}

write_liked_songs_to_file(songs,"liked_songs.txt")