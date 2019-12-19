"""
Mission 8 : Les classes
Vincent Bauffe, November 2019
"""

class Duree:

    def __init__(self, h, m, s):  #ok
        seconde = h * 3600 + m * 60 + s
        self.h = seconde // 3600
        self.m = (seconde % 3600) // 60
        self.s = ((seconde % 3600) % 60)

    def toSecondes(self):  #ok
        return self.h * 3600 + self.m * 60 + self.s

    def delta(self, d):  #ok
        return self.toSecondes() - d.toSecondes()

    def apres(self, d):  #ok
        if self.delta(d) > 0:
            return True
        return False

    def ajouter(self, d): #ok
        temps = self.toSecondes() + d.toSecondes()
        self.h = temps // 3600
        self.m = (temps % 3600) // 60
        self.s = ((temps % 3600) % 60)
        return self.h, self.m, self.s

    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.h, self.m, self.s)


class Chanson:

    def __init__(self, t, a, d):
        self.t = t
        self.a = a
        self.d = d
        self.length = d.toSecondes()

    def __str__(self):
        return self.t + " - " + self.a + " - " + str(self.d)


class Album:

    def __init__(self, number):
        self.number = number
        self.count = 0
        self.duration = 0
        self.album = []

    def __str__(self):
        return "Album {0} ({1} chansons, {2})\n".format(self.number, self.count, Duree(0, 0, self.duration)) + "\n".join(self.album) + "\n"

    def add(self, chanson):
        self.count += 1
        self.album.append("{:02}: ".format(self.count) + chanson.__str__())
        self.duration += chanson.length

    def state(self):
        if self.count >= 100 or self.duration >= 4500:
            return False
        return True



with open("music-db.txt", "r") as file:
    all_music = file.read().split("\n")
    for i in range(len(all_music)):
        all_music[i] = all_music[i].split(" ")

count = 0
music_count = 0
while True:
    count += 1
    album = Album(count)
    while True:
        if music_count == len(all_music):
            break
        title = " ".join(all_music[music_count][0].split("_"))
        artist = " ".join(all_music[music_count][1].split("_"))
        try:
            length = Duree(0, int(all_music[music_count][-2]), int(all_music[music_count][-1]))
            chanson = Chanson(title, artist, length)
        except:
            continue
        if album.duration + length.toSecondes() < 4500:
            album.add(chanson)
            music_count += 1
        else:
            break
    print(album)
    if music_count == len(all_music):
        break