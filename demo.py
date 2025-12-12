import sqlite3
con = sqlite3.connect("part2.db")
cur = con.cursor()

#izveidot tabulu
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

#apskatīt, kādas tabulas eksistē
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())

#ievietot vērtības tabulā
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
#Apstiprināt ievadi
con.commit()

#Izgūt datus:
res = cur.execute("SELECT title,score FROM movie")

movies=res.fetchall()
for movie in movies:
  print(movie)