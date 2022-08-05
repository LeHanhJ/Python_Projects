import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
rosterValues = (('Jean-Baptiste Zorg','Human',122),('Korben Dallas', 'Meat Popsicle', 100), ("Ak'not","Mangalore", -5))
c.executemany("INSERT INTO Roster VALUES(?,?,?)",rosterValues)


c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?", ("Human", "Korben Dallas", 100))

c.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
for row in c.fetchall():
    print(row)
