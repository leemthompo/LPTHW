class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued"
                   "So I'll stop right there"])

print(f"happy_bday is of type {type(happy_bday)}")                               

bulls_on_parade = Song(["They rally around",
                        "So I'll eat right here the sambo"])

fart_song = ["Rats are everywhere",
             "But I don't care", 
             "And I'm running around like a weasel",
             "Plunging forward forever"]

new_fart = Song(fart_song)

new_fart.sing_me_a_song()

s = ""

n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue

    a = ['foo', 'bar', 'baz']
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break
print(s)        