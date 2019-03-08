class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singMeASong(self):
        for line in self.lyrics:
            print(line)

happyB = Song(["Happy birthday to you",
               "Happy birthday to you",
               "Happy birthday dear someone",
               "Happy birthday to you"])

bullsOnParade = Song(["They really around the family",
                      "With pockets full of shells"])

beautifulSong = ["When the days are colder", "The cards all folded", 
"The saints we see", "Are all made of gold."]

demons = Song(beautifulSong)

happyB.singMeASong()
bullsOnParade.singMeASong()

demons.singMeASong()