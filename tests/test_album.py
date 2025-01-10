from lib.album import *
# When I construct an Album
# With the fields title, release_year and artist_id
# They are reflected in the instance properties

def test_constructs_with_fields():
    albumOne = Album(1,'Doolittle', 1989, 1)
    assert albumOne.id == 1
    assert albumOne.title == 'Doolittle'
    assert albumOne.release_year == 1989
    assert albumOne.artist_id == 1

# When I construct two Artists with the same fields
# They are equal

def test_equality():
    album_1 = Album(1,'Doolittle', 1989, 1)
    album_2 = Album(1,'Doolittle', 1989, 1)
    assert album_1 == album_2

"""
when I construct an Album
And I format it to a string
Then it comes out in a friendly format
"""

def test_formatting():
    album = Album(1,'Doolittle', 1989, 1)
    assert str(album) == "Album(1, Doolittle, 1989, 1)"