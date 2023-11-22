import datetime

tagadejais_laiks=datetime.datetime.now().hour

if 6 <= tagadejais_laiks < 10:
    print("Labrīt!")
elif 10 <= tagadejais_laiks < 18:
    print("Labdien!")
else:
    print("Labvakar!")