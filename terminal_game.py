import random

name = input("Enter your name: ")
print(f'Welcome, {name}, to this mysterious adventure!')

class Wizard():
    def __init__(self, name):
        self.name = name
        self.health = 60
        self.power = 80

class Warrior():
    def __init__(self, name):
        self.name = name
        self.health = 80
        self.power = 70

class Archer():
    def __init__(self, name):
        self.name = name
        self.health = 90
        self.power = 60

hero = input(f'Choose your character, {name}. Wizard, Warrior, or Archer: ')

if hero.lower() == 'wizard':
    player = Wizard(name)
elif hero.lower() == 'warrior':
    player = Warrior(name)
elif hero.lower() == 'archer':
    player = Archer(name)
else:
    print('Invalid choice, you are now a Wizard')
    player = Wizard(name)

print(f'You are now {hero}. Your health is {player.health} and your power is {player.power}.')

stage1 = ["dark forest, narrow cave, empty field"]
stage2 = ["abandoned village, vast desert, dark building"]
stage3 = ["haunted mansion, ancient ruins, misty swamp"]
stage4 = ["spider nest, orc lair, bone cemetery"]
stage5 = ["mountain top, underwater cavern, sky labyrinth"]

stages = [stage1,
          stage2,
          stage3,
          stage4,
          stage5
          ]

current_stage = 0

def encounter():
    enemy_type = random.choice(['Goblin', 'Troll', 'Dragon'])
    if enemy_type == 'Goblin':
        enemy = {'name': 'Goblin', 'health': 30, 'power': 5}
    elif enemy_type == 'Troll':
        enemy = {'name': 'Troll', 'health': 50, 'power': 7}
    else:
        enemy = {'name': 'Dragon', 'health': 100, 'power': 15}
    
    print(f'A wild {enemy["name"]} appears! It has {enemy["health"]} health and {enemy["power"]} power.')

    while enemy['health'] > 0 and player.health > 0:
        action = input('Do you want to (a)ttack or (r)un? ')
        if action.lower() == 'a':
            enemy['health'] -= player.power
            print(f'You attacked the {enemy["name"]}. Its health is now {enemy["health"]}.')
            if enemy['health'] <= 0:
                print(f'You defeated the {enemy["name"]}!')
                break
            player.health -= enemy['power']
            print(f'The {enemy["name"]} attacked you. Your health is now {player.health}.')
            if player.health <= 0:
                print('You have been defeated! Game Over.')
                return False
        elif action.lower() == 'r':
            print('You ran away safely!')
            return True
        else:
            print('Invalid action. Please choose again.')
    return True

while current_stage < len(stages):
    print(f'You are at stage {current_stage + 1}.')
    location = random.choice(stages[current_stage][0].split(', '))
    print(f'You find yourself in a {location}.')
    
    if not encounter():
        break
    
    current_stage += 1

if current_stage == len(stages):
    print(f'Congratulations, {name}! You have completed the adventure!')
