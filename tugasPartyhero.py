class Hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        self.name = name
        self.job = job
        self.hp = hp
        self.max_hp = hp
        self.type = hero_type
        self.rage = False

        print(self.name, "siap bertarung")

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def attack(self, enemy, damage):
        if self.is_alive() == False:
            print(self.name, "tidak bisa menyerang")
            return

        if damage <= 0:
            print("damage salah")
            return

        if self.type == "boss":
            if self.hp <= self.max_hp / 2:
                self.rage = True
                print("Boss rage")

        if self.rage == True:
            damage = damage * 2

        print(self.name, "attack", enemy.name, damage)
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0

        print(self.name, "HP", self.hp)

        if self.hp == 0:
            print(self.name, "mati")

    def heal(self):
        if self.is_alive() == False:
            print(self.name, "tidak bisa heal")
            return

        if self.job == "Healer":
            heal = 25
        else:
            heal = 10

        self.hp = self.hp + heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(self.name, "heal", heal)

# CERITA

hero1 = Hero("Zilong", "Warrior", 120)
hero2 = Hero("Eudora", "Mage", 80)
hero3 = Hero("Rafaela", "Healer", 90)

goblin = Hero("Goblin", "Monster", 60, "normal")

print("Lawan Goblin")
hero1.attack(goblin, 20)
hero2.attack(goblin, 30)
goblin.attack(hero1, 15)
hero2.attack(goblin, 20)

print("Boss Datang")
boss = Hero("Raja Iblis", "Boss", 200, "boss")

hero1.attack(boss, 25)
hero2.attack(boss, 40)
boss.attack(hero1, 30)

hero3.heal()

hero2.attack(boss, 60)   
boss.attack(hero2, 30)   
boss.attack(hero2, 50)   
