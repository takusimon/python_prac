import functools

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42),
            ('Just Like That', 5.05),
            ('Song 3', 6.8),
            ('Leave The Door Open', 4.02),
            ('I Can\'t Breath', 4.47),
            ('Bad Guy', 3.14)
            ]

def greater_five(some_songs):
    return some_songs[1]>=5

def minutes_to_seconds(some_songs):
    duration = some_songs[1]
    minutes = int(duration)
    seconds = (duration - minutes) * 100

    total_seconds = minutes * 60 + round(seconds)

    return total_seconds




songs = filter(greater_five,playlist)
print(list(songs))

lets_map = map(minutes_to_seconds,playlist)
print(list(lets_map))


