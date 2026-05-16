"""
Author:Adrian Terriquez
Filename: playlist.py
Description: Implementation of a playlist as an array with duplicates
"""

from song import Song

class Playlist():
    # The constructor is run every time a new Playlist object is created
    # max_num_songs is the maximum number of songs you can have in the playlist
    def __init__(self, initial_songs):
        # Manually count the initial songs to find the size
        count = 0
        for song in initial_songs:
            count += 1
            
        # Set attributes based on the initial list size
        self.max_num_songs = count
        self.num_songs = count
        
        # Initialize the fixed-size array
        self.songs = [None] * self.max_num_songs
        
        # Manually copy the songs over into our playlist array
        for i in range(count):
            self.songs[i] = initial_songs[i]

    ###########
    # Methods #
    ###########

    # Return the number of songs in the playlist
    def get_num_songs(self):
        return self.num_songs 
    
    # Return the current songs list
    def get_songs(self):
        return self.songs 
    
    # Return the song at index idx or
    # Return None if idx is outside of bounds
    def get_song_at_idx(self, idx):
        if 0 <= idx and idx < self.num_songs:
            return self.songs[idx]
    
    # Set index idx to the given song
    # Do not change anything if idx is outside of bounds
    def set_song_at_idx(self, idx, song):
        if 0 <= idx and idx < self.num_songs:
            self.songs[idx] = song 

    # Insert a song to the end of the playlist
    def insert_song(self, song):
        # If the array is full, dynamically resize it (double the size)
        if self.num_songs == self.max_num_songs:
            # Handle edge case where max_num_songs might start at 0
            self.max_num_songs = self.max_num_songs * 2 if self.max_num_songs > 0 else 1
            
            # Create a new, larger array
            new_songs = [None] * self.max_num_songs
            
            # Manually copy elements over (no built-in list methods allowed!)
            for i in range(self.num_songs):
                new_songs[i] = self.songs[i]
                
            # Replace the old array with the new one
            self.songs = new_songs

        # Insert the song at the end and update length
        self.songs[self.num_songs] = song
        self.num_songs += 1

    # Return the index of the given song title in the playlist,
    # or return -1 if the song is not in the playlist
    def search_by_title(self, song_title):
        # Only search the indices with songs
        for i in range(self.num_songs):
            # Check the value at the current index 
            if self.songs[i].title == song_title:
                # Return the index
                return i 
            
        # If we got here, we did not find the song so return -1
        return -1
    
    # Delete the first occurrence of the song title in the playlist
    # Returns True if the song was deleted, or False if not
    def delete_by_title(self, song_title):
        delete_count = 0
        idx = self.search_by_title(song_title)
        
        # Keep looping as long as the song title is found in the playlist
        while idx != -1:
            delete_count += 1
            self.num_songs -= 1
            
            # Shift all remaining songs to the left
            for j in range(idx, self.num_songs):
                self.songs[j] = self.songs[j+1]
                
            # Clear out the trailing leftover duplicate reference at the end
            self.songs[self.num_songs] = None 
            
            # Search again to see if there's another duplicate
            idx = self.search_by_title(song_title)
            
        return delete_count
    
    # Print all songs in the playlist
    def traverse(self):
        for song in self.songs:
            print(song)

if __name__ == '__main__':
    # You can test your code here
    songs = [Song("Golden", "HUNTR/X"),
             Song("Ordinary", "Alex Warren"),
             Song("What I Want", "Morgan Wallen ft. Tate McRae"),
             Song("Your Idol", "Saja Boys"),
             Song("Soda Pop", "Saja Boys")]
    
    p = Playlist(3)