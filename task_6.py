from itertools import count, cycle

for i in count(3):
    print(i)
    if i >= 10:
        break
song = ['param', 'pam', 'pam']
new_song = []
for i in cycle(song):
    print(i)
    new_song.append(i)
    if len(new_song) > 10:
        break
