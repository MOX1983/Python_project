from random import randint
class Monster:
    name = ''
    ammo = 10 #боеприпасы
    health = 100

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Monster: " + str(self.name) + " " + str(self.health)

    def attack(self, other):
        self.ammo -= 1
        other.health -= 10


class Screaming_mold(Monster):
    sound = 10

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "Screaming: " + str(self.name) + " " + str(self.health)

    def scream(self):
        return "AAAAAAA"
    def attack(self, other):
        self.ammo -= 1
        other.health -= 20

class Hero:
    name = ''
    shield = 20 #щит
    health = 100
    sword = 50 #меч

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name) + " " + str(self.health)

    def protect(self):
        self.health += randint(1, self.shield)

    def attack(self, other):
        self.sword -= 1
        other.health -= 20


print("Введите имя героя!")
hero = Hero(str(input()))

lst_Monsters = []
print("Скольно монстров вы хотите создать ?")
for i in range(0, int(input())):
    print("Хотите создать обычного монстра --(1) или Орущую плесень --(2)?")
    if int(input()) == 1:
        print("Введите имя монстра!")
        monster = Monster(str(input()))
        lst_Monsters.append(monster)
    else:
        print("Введите имя Орущему монстру!")
        scream = Screaming_mold(str(input()))
        lst_Monsters.append(scream)


print(f"В густом лесу, где деревья возвышаются над землёй, словно стражи,\n"
          f" живёт молодой охотник по имени {hero.name}.\n"
          f" Однажды, когда {hero.name} отправился на охоту,\n"
          f" он услышал странные звуки, доносящиеся из глубины леса.\n"
          f" Решив выяснить, что происходит, он углубился в чащу и обнаружил, что попал в ловушку.\n"
          f" Вокруг него были монстры, которые хотели его убить.\n")

bl = True
for i in range(hero.sword):
    if hero.health > 0  and bl:
        print(hero.__str__())
        for x in lst_Monsters:
            print(x.__str__(), end=' ')

        print("\nкого хотите ударить ?")
        x = str(input())
        for mob in lst_Monsters:
            if x == mob.name:
                print(f"{hero.name} атакует! -20 {mob.name}")
                hero.attack(mob)
                print(mob.__str__())
            if not isinstance(mob, Screaming_mold):
                if mob.ammo != 0 and mob.health != 0:
                    print(f"{mob.name} вас атакует Монстр ! -10 {hero.name}")
                    mob.attack(hero)
                elif mob.health == 0:
                    print(f"{mob.name} Умер!")
                    lst_Monsters.remove(mob)
            else:
                if mob.ammo != 0 and mob.health != 0:
                    print(mob.scream())
                    print(f"{mob.name} вас атакует Орущая плесень! -20 {hero.name}")
                    mob.attack(hero)
                elif mob.health == 0:
                    print(f"{mob.name} Умер!")
                    lst_Monsters.remove(mob)

            if hero.health <= 50:
                hero.protect()
                print("вы использовали хилл!", hero.__str__())

            if len(lst_Monsters) == 0:
                print(f"{hero.name} Выйграл!!! УРАААААААА!!!!")
                bl = False
    elif hero.health <= 0 and bl:
        print(f"{hero.name} Умер :((( попробуй ещё раз ")
        bl = False

if hero.sword == 0:
    print(f"{hero.name} Проиграл у тебя сломался меч:((( попробуй ещё раз ")