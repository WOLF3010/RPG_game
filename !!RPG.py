import random
import time
class Player:
    def __init__(self, player_name, player_hp, player_damage):
        self.name = player_name
        self.hp = player_hp
        self.damage = player_damage
        self.level = 1
        self.exp = 0
    def lvl_up(self):
        self.level += 1
        self.exp = 0
        self.hp += 5*self.level
        self.damage += 5.5*self.level
        print(f"Поздравляем у вас повышение уровня на {self.level}\n")

    @staticmethod
    def create_weapon():
        weapon_type = ["Сковородка", "меч", "хамон", "клавиатура", "мешок ковычек", "малый пес", "стенд"]
        weapon_rare = {
            1: "обычный",
            2: "редкий",
            3: "легендарный",
            4: "эпический"

        }
        weapon_random = random.choice(weapon_type)
        weapon_rare_random = random.choice(list(weapon_rare.keys()))
        if weapon_random == weapon_type[0]:
            player.damage += 10 * weapon_rare_random
        elif weapon_random == weapon_type[1]:
            player.damage += 25 * weapon_rare_random
        elif weapon_random == weapon_type[2]:
            player.damage += 50 * weapon_rare_random
        elif weapon_random == weapon_type[3]:
            player.damage += 10 * weapon_rare_random
        elif weapon_random == weapon_type[4]:
            player.damage += 5 * weapon_rare_random
        elif weapon_random == weapon_type[5]:
            player.damage += 1000000 * weapon_rare_random
        elif weapon_random == weapon_type[6]:
            player.damage += 99999999999999999999999999999999999999999999999999999999 * weapon_rare_random
        return weapon_random, weapon_rare[weapon_rare_random]

    @staticmethod
    def create_heal():
        heal_type = {
            50: "samogon",
            100: "aktivirovaniy ygol",
            1000000000000000000000000000000000000000000000000000000000000000000: "zvezdochka",
            99: "hamon"
        }
        heal_type_random = random.choice(list(heal_type.keys()))
        player.hp += heal_type_random
        return heal_type[heal_type_random]

    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            random_exp = 5*self.level
            print(f"{victim.name} повержен! +{random_exp} опыта")
            time.sleep(0.7)
            random_number = random.randint(0, 3)
            if random_number == 0:
                weapon = self.create_weapon()
                print(f"Вам выпало оружие \n"
                      f"{weapon[0]} {weapon[1]}\n"
                      f"Ваш урон: {player.damage}")
            elif random_number == 1:
                heal = self.create_heal()
                print(f"вы получили: {heal}\n"
                      f"Ваш здоровье: {player.hp}\n")
            else:
                print("Вам ничего не выпало, повезёт в следующий раз")

            time.sleep(0.7)
            self.exp += random_exp
            max_exp = 20*self.level
            if self.exp >= max_exp:
                self.lvl_up()
                max_exp = 20 * self.level
                time.sleep(0.7)
                print(f"До следущего уровня {max_exp} опыта\n")
                time.sleep(0.7)
            time.sleep(0.7)
            return False
        else:
            print(f"{victim.name}, осталось {victim.hp} здоровья")
            time.sleep(0.7)
            return True

    @staticmethod
    def create_player(player_name, player_race, player_class):
        hp = 0
        damage = 0
        player_name = player_name
        if player_race == races_list[0]:
            hp = 50
            damage = 25
        elif player_race == races_list[1]:
            hp = 100
            damage = 30
        elif player_race == races_list[2]:
            hp = 100
            damage = 30
        elif player_race == races_list[3]:
            hp = 60
            damage = 20
        else:
            print("takoi rassi net")
            quit()
        if player_class == class_list[0]:
            damage += 20
        elif player_class == class_list[1]:
            damage += 37
        else:
            print('takogo classa net')
            quit()
        return Player(player_name, hp, damage)
class Enemy:
    def __init__(self, enemy_name, enemy_hp, enemy_damage):
        self.name = enemy_name
        self.hp = enemy_hp
        self.damage = enemy_damage

    @staticmethod
    def create_enemy():
        enemy_names = ["ogromniy_pyos", "Dio", "ogormniy_cot"]
        enemy_name = random.choice(enemy_names)
        enemy_hp = random.randint(1, 100) + 7*player.level
        enemy_damage = random.randint(1, 100) + 7*player.level
        return Enemy(enemy_name, enemy_hp, enemy_damage)


    def attack(self, victim):
        victim.hp -= self.damage
        print(f"{self.name} нанёс удар: {self.damage}")
        if victim.hp <= 0:
            print(f"{self.name} победил\n"
                  f"Игра окончена")
        else:
            print(f"ваше здоровье: {victim.hp}")
            time.sleep(0.7)



races_list = ["elf","gnom", "hobit", "chelovek"]
class_list = ["lychnik", "ricar"]
print("zdravstvuite, kak vas zovyt?")
name = input()
print("K kakoy rase vi otnosites?")
for race in races_list:
    print(race, end=" ")
print()
race = input().lower()
print("k kakomy clasy vi otnosites?")
for class_player in class_list:
    print(class_player, end=" ")
print()
class_player = input().lower()

player = Player.create_player(name,race,class_player)
print(player.name, player.hp, player.damage, player.level, player.exp)

def fight_choice():
    answer = int(input("Атаковать или сбежать (1,2)?"))
    if answer == 1:
        w = player.attack(enemy)
        if w :
            enemy.attack(player)
            fight_choice()


    elif answer == 2:
        escape_list = [1, 0]
        escape = random.choice(escape_list)

        if escape == 1:
            print("Вы сбежали")
            time.sleep(0.7)
        elif escape == 0:
            print("Побег не удался!")
            time.sleep(0.7)
            enemy.attack(player)
            time.sleep(0.7)
            fight_choice()
        else:
            print("Неизвестная ошибка")
            quit()


while True:
    event = random.randint(0, 1)
    if event == 0:
        print("Вам никто не встретился, идём дальше...")
        time.sleep(0.7)
    elif event == 1:
        enemy = Enemy.create_enemy()
        print(f"Вас заметил {enemy.name}\n"
              f"Здоровье врага: {enemy.hp}\n"
              f"Урон врага: {enemy.damage}\n")

        fight_choice()





