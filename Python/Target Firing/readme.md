<a href = https://www.codingame.com/ide/puzzle/target-firing target="_blank">Target Firing</a>

«Story»
Your spaceship is under attack by aliens! (It's actually your friend's spaceship, so the situation is even worse) Luckily your spaceship is equipped with an antimatter beam, while the aliens only have cheap (but still dangerous) laser pointers. Can you destroy all alien spaceships safely, or should you flee?

«Prompt»
As the AI within the ship's computer, your goal is to determine the optimal order of alien spaceships to destroy such that you leave the encounter with the maximum strength of your shields. Print the remaining strength of the shields, or FLEE if your spaceship is predicted to take more damage than your shields can handle. Your friend will not forgive you if the ship is damaged.



```Python
import sys
import math

turns = []
d = []
dam = []
arm = []
shp = []
point = []

n = int(input())
for i in range(n):
    inputs = input().split()
    ship = inputs[0]
    hp = int(inputs[1])
    armor = int(inputs[2])
    damage = int(inputs[3])
    if ship == "FIGHTER" :
        for i in range(10000) :
            if armor > 19 :
                armor = 19
            if hp-((20-armor)*i) <= 0 :
                break
        turns.append(i)
        d.append(i*damage)
        dam.append(damage)
        arm.append(armor)
        shp.append(ship)
        point.append(hp)
    else :
        for i in range(10000) :
            if armor > 9 :
                armor = 9
            if hp-((10-armor)*i) <= 0 :
                break
        turns.append(i)        
        d.append(i*damage)
        dam.append(damage)
        arm.append(armor)
        shp.append(ship)
        point.append(hp)
index = []

for i in range(len(turns)) :
    index.append(i)

sum1 = sum(turns)

d1 = []
for i in range(len(d)) :
    d1.append(dam[i] * sum1 / turns[i])

zipi = zip(index, d1)
dic = dict(zipi)
dic2 = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

tot = sorted(turns)
shield = 5000

total = 0
tourstotal = [0]
for i in range(len(d)) :
    tourstotal.append(tourstotal[i] + turns[list(dic2)[i]])

for i in range(len(d)) :
        total += tourstotal[i+1]*dam[list(dic2)[i]]
shield = 5000 - total

if shield < 0 :
    shield = "FLEE"

# print(sum1, ": somme des tours")
# print(turns, ': nbr de tours par vaisseaux')
# print(point, ': PV des vasseaux')
# print(arm, ': armure des vaisseaux')
# print(dam, ': dmg des vaisseaux')
# print(tot, ': nbr de tours ordre croissant')
# print(dic2, ': full blast ordre')
# print(shp, ': type de vaisseau')
# print(list(dic2)[0], "indice dmg le plus vnr")
# print(turns[list(dic2)[0]], "nbr de tour pour kill le vnr")
# print(dam[list(dic2)[0]], "dmg du vnr")
# print(turns[list(dic2)[1]], "turn du 2eme")
# print(tourstotal, "ajout des tours")
# print(shield, ': shield restant')
print(shield)
```
