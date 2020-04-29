import pytest
from src.song import Song

def test_exercise():
    song_one = Song("22", "Taylor Swift", 192)
    song_two = Song("22", "Taylor Swift", 192)
    song_three = Song("Blank Space","Taylor Swift",192)

    assert song_one == song_two
    assert not song_two == song_three
