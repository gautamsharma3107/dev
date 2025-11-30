"""
Day 6 Mini Project 1: Playlist Manager
======================================
Build a music playlist manager using linked list.

Features:
- Add songs to playlist
- Remove songs
- Play next/previous
- Shuffle playlist
- Display playlist
"""

import random

class Song:
    """Represents a song in the playlist."""
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # in seconds
        self.next = None
        self.prev = None
    
    def __repr__(self):
        mins = self.duration // 60
        secs = self.duration % 60
        return f"'{self.title}' by {self.artist} ({mins}:{secs:02d})"


class Playlist:
    """Doubly linked list based playlist manager."""
    
    def __init__(self, name):
        self.name = name
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
    
    def add_song(self, title, artist, duration):
        """Add song to end of playlist."""
        new_song = Song(title, artist, duration)
        
        if not self.head:
            self.head = new_song
            self.tail = new_song
            self.current = new_song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song
        
        self.size += 1
        print(f"✅ Added: {new_song}")
    
    def remove_song(self, title):
        """Remove song by title."""
        current = self.head
        
        while current:
            if current.title == title:
                # Update links
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                # Update current if needed
                if self.current == current:
                    self.current = current.next or current.prev
                
                self.size -= 1
                print(f"🗑️  Removed: {current}")
                return True
            
            current = current.next
        
        print(f"❌ Song '{title}' not found")
        return False
    
    def play_current(self):
        """Display currently playing song."""
        if self.current:
            print(f"🎵 Now Playing: {self.current}")
        else:
            print("❌ Playlist is empty")
    
    def play_next(self):
        """Move to next song."""
        if not self.current:
            print("❌ Playlist is empty")
            return
        
        if self.current.next:
            self.current = self.current.next
            print(f"⏭️  Next: {self.current}")
        else:
            print("📍 End of playlist, wrapping to start")
            self.current = self.head
            print(f"🎵 Now Playing: {self.current}")
    
    def play_previous(self):
        """Move to previous song."""
        if not self.current:
            print("❌ Playlist is empty")
            return
        
        if self.current.prev:
            self.current = self.current.prev
            print(f"⏮️  Previous: {self.current}")
        else:
            print("📍 Start of playlist, wrapping to end")
            self.current = self.tail
            print(f"🎵 Now Playing: {self.current}")
    
    def shuffle(self):
        """Shuffle playlist using Fisher-Yates algorithm."""
        if self.size <= 1:
            print("❌ Not enough songs to shuffle")
            return
        
        # Convert to list
        songs = []
        current = self.head
        while current:
            songs.append((current.title, current.artist, current.duration))
            current = current.next
        
        # Shuffle
        random.shuffle(songs)
        
        # Rebuild playlist
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
        
        for title, artist, duration in songs:
            self.add_song(title, artist, duration)
        
        print("🔀 Playlist shuffled!")
    
    def display(self):
        """Display all songs in playlist."""
        if not self.head:
            print(f"📋 {self.name}: Empty playlist")
            return
        
        print(f"\n📋 {self.name} ({self.size} songs):")
        print("-" * 50)
        
        current = self.head
        position = 1
        total_duration = 0
        
        while current:
            marker = "▶️ " if current == self.current else "   "
            print(f"{marker}{position}. {current}")
            total_duration += current.duration
            current = current.next
            position += 1
        
        print("-" * 50)
        mins = total_duration // 60
        secs = total_duration % 60
        print(f"Total duration: {mins}:{secs:02d}")
    
    def search(self, query):
        """Search for songs by title or artist."""
        results = []
        current = self.head
        
        while current:
            if query.lower() in current.title.lower() or \
               query.lower() in current.artist.lower():
                results.append(current)
            current = current.next
        
        if results:
            print(f"\n🔍 Search results for '{query}':")
            for i, song in enumerate(results, 1):
                print(f"   {i}. {song}")
        else:
            print(f"❌ No songs found matching '{query}'")
        
        return results
    
    def get_total_duration(self):
        """Calculate total playlist duration."""
        total = 0
        current = self.head
        while current:
            total += current.duration
            current = current.next
        return total


def main():
    """Demo the playlist manager."""
    print("=" * 50)
    print("🎧 PLAYLIST MANAGER")
    print("=" * 50)
    
    # Create playlist
    playlist = Playlist("My Favorites")
    
    # Add songs
    print("\nAdding songs:")
    playlist.add_song("Bohemian Rhapsody", "Queen", 355)
    playlist.add_song("Stairway to Heaven", "Led Zeppelin", 482)
    playlist.add_song("Hotel California", "Eagles", 391)
    playlist.add_song("Sweet Child O Mine", "Guns N' Roses", 356)
    playlist.add_song("Smells Like Teen Spirit", "Nirvana", 279)
    
    # Display playlist
    playlist.display()
    
    # Play songs
    print("\n" + "=" * 50)
    print("🎵 PLAYBACK CONTROLS")
    print("=" * 50)
    
    playlist.play_current()
    playlist.play_next()
    playlist.play_next()
    playlist.play_previous()
    
    # Search
    print("\n" + "=" * 50)
    print("🔍 SEARCH")
    print("=" * 50)
    
    playlist.search("Queen")
    playlist.search("Heaven")
    playlist.search("rock")
    
    # Remove song
    print("\n" + "=" * 50)
    print("🗑️  REMOVE SONG")
    print("=" * 50)
    
    playlist.remove_song("Hotel California")
    playlist.display()
    
    # Shuffle
    print("\n" + "=" * 50)
    print("🔀 SHUFFLE")
    print("=" * 50)
    
    playlist.shuffle()
    playlist.display()
    
    print("\n" + "=" * 50)
    print("✅ Playlist Manager Demo Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
