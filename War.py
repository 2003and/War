class Soldier:
    def __init__(self, name, hp=10, ammo=5):
        self.name = name
        self.ammo = ammo
        self.hp = hp
        self.alive = True

    def hit(self):
        self.hp -= 5
        print(self.name, 'is hit!')
        if self.hp <= 0:
            self.alive = False
            print(self.name, 'is dead!')

    def fire_at(self, enemy):
        if self.alive:
            if self.ammo >= 1:
                print(self.name, 'is firing at', enemy.name)
                self.ammo -= 1
                enemy.hit()
            else:
                print(self.name, 'is out of ammo!')
        else:
            print(self.name, 'is dead... Rest in peace,', self.name, '!')

    def __str__(self):
        if self.alive:
            return self.name+' - hp:'+str(self.hp)+' ammo:'+str(self.ammo)
        else:
            return self.name+' - DEAD'

    def get_ammo(self):
        self.ammo += 5
        print(self.name, 'took some more ammo')

    def heal(self):
        self.hp += 5
        print(self.name, 'used his medkit to heal his wounds')

    def skip_turn(self):
        print(self.name, 'skipped turn')

seps = ['@'*20, 'w'*20]

army = [Soldier('Andrew'),
        Soldier('Bob'),
        Soldier('Cole'),
        Soldier('Daniel'),
        Soldier('Edmond')]
IDs = {'Andrew': 1,
       'Bob': 2,
       'Cole': 3,
       'Daniel': 4,
       'Edmond': 5}

while len(army) > 1:
    attacker = 0
    for i in range(len(army)):
        print(seps[0])
        for j in range(len(army)):
            print(army[j])
        print(seps[0])
        print("It's", army[attacker].name, "'s turn")
        action = input('Your action?(heal, shoot, ammo)')
        if action == 'heal':
            print(seps[1])
            army[attacker].heal()
            print(seps[1])
        elif action == 'shoot':
            defender = input("Who's the target?")
            print(seps[1])
            army[attacker].fire_at(army[IDs[defender]-1])
            print(seps[1])
        elif action == 'ammo':
            print(seps[1])
            army[attacker].get_ammo()
            print(seps[1])
        else:
            print(seps[1])
            army[attacker].skip_turn()
            print(seps[1])

        if not army[IDs[defender]-1].alive:
            army.pop(IDs[defender]-1)
        attacker += 1
print(army[0].name, 'is the winner! Congratulations,', army[0].name+'!')
