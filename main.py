def timeConversion(s):
    hour = (s[:2])
    if (s.count('PM') > 0) and (int(hour) != 12):
        hour = str(int(hour) + 12)
    elif (s.count('AM') > 0) and int(hour) == 12:
        hour = str('00')

    return hour + s[2:8]

s = '12:07:38PM' # -> 17:07:38

print(timeConversion(s))
