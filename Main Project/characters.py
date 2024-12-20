import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power, avoid, heal_uses):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        #adding an attribute
        self.avoid = avoid
        #adding an attribute self heal uses
        self.heal_uses = heal_uses

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):
        if self.heal_uses > 0:
             if self.health + 50 > self.max_health:
                self.health = self.max_health
             else:
                self.health += 50
             self.heal_uses -= 1
             print(f'{self.name} healed +50! ❤️‍🩹 Health uses left: {self.heal_uses}')
        else:
            print("No heals left!")


# 1. Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, avoid = False, heal_uses = 2)  # Boost health and attack power

    def choose_ability(self, opponent):
        ability = input(f"Choose your ability:\n1. Power Attack\n2. Spit Fire\nWhich one do you choose: ")
        if ability == '1':
            self.power_attack(opponent)
            
        elif ability == '2':
            self.spit_fire(opponent)
            
        else:
            print(f'Invalid selection.. Defaulting to power attack! {self.power_attack(opponent)}')

    # created by me. Add your power attack method here
    def power_attack(self, opponent):
        # power attack will be the warrior's insane jump kick
        print(f"{self.name} says, take that! 🦵💥")
        opponent.health -= (self.attack_power + 10)
        print(f"{opponent.name}'s health just dropped by {self.attack_power + 10}! Nice work!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            print(f"{self.name} says, I've defeated you {opponent.name}. Until next time!")

    def spit_fire(self, opponent):
        # spit fire will be the warriors attempt to do more damage with a higher attack power
        print(f"{self.name} spits out a huge flame! 🔥")
        opponent.health -= (self.attack_power + 15)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power + 15} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            print(f"{self.name} says, I've defeated you {opponent.name}. Until next time!")

# 2. Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, avoid = False, heal_uses = 3)  # Boost attack power

    def choose_ability(self, opponent):
        ability = input(f"Choose your ability:\n1. Cast A Spell\n2. Invisible Cloak\nWhich one do you choose: ")
        if ability == '1':
            self.cast_spell(opponent)
            
        elif ability == '2':
            self.invisible_cloak(opponent)
            
        else:
            print(f'Invalid selection.. Defaulting to cast spell! {self.cast_spell(opponent)}')

    # created by me. Add your cast spell method here
    def cast_spell(self, opponent):
        # cast_spell will be the Mage's way of shutting down the wizard with magic
        print(f"{self.name} is casting a spell! 🪄")
        opponent.health -= (self.attack_power + 5)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power + 5} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            print(f"{self.name} says, I've defeated you {opponent.name}. Until next time!")

     # created by me. invisible cloak gives the ability to be invisible and avoid attacks
    def invisible_cloak(self, opponent):
        # invisible cloak
        self.avoid = True
        print(f"{self.name} is now invisible! 👻")
        print(f"{self.name} escapes the attack! Health remains the same!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# 3. created by me. Archer Class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=135, attack_power=30, avoid = False, heal_uses = 3)

    def choose_ability(self, opponent):
        ability = input(f"Choose your ability:\n1. Quick Shot\n2. Evade\nWhich one do you choose: ")
        if ability == '1':
            self.quick_shot(opponent)
            
        elif ability == '2':
            self.evade(opponent)
            
        else:
            print(f'Invalid selection.. Defaulting to Quick Shot! {self.quick_shot(opponent)}')

    def quick_shot(self, opponent):
        # quick shot will be the Archer's two arrow shot at the evil wizard
        print(f"{self.name} is shooting 2 arrows at once! 🏹")
        opponent.health -= (self.attack_power + 10)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power + 10} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            print(f"{self.name} says, I've defeated you {opponent.name}. Until next time!")

    def evade(self, opponent):
        self.avoid = True
        # evade will be the Archer's way of evading attacks
        print(f"{self.name} is evading the attack! 🏃‍♂️‍➡️")
        print(f"{self.name} evades the attack! Health remains the same! {self.health + 15}")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            print(f"{self.name} says, I've defeated you {opponent.name}. Until next time!")

# created by me. Paladin Class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=145, attack_power=20, avoid=False, heal_uses = 1)

    def choose_ability(self, opponent):
        ability = input(f"Choose your ability:\n1. Holy Strike\n2. Divine Shield\nWhich one do you choose: ")
        if ability == '1':
            self.holy_strike(opponent)
            
        elif ability == '2':
            self.divine_shield(opponent)
            
        else:
            print(f'Invalid selection.. Defaulting to Holy Strike! {self.holy_strike(opponent)}')

    def holy_strike(self, opponent):
        # holy strike will get the paladin out of trouble!
        print(f"{self.name}'s doing the Holy Strike! ✨")
        opponent.health -= (self.attack_power + 5)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power + 5} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            print(f"{self.name} says, I've defeated you {opponent.name}. Until next time!")

    def divine_shield(self, opponent):
        self.avoid = True
         # divine shield will help Paladin not lose too much health
        print(f"{self.name} is shielding himself! 🛡️")
        print(f"{self.name} shields the attack! Health remains the same! {self.health + 15}")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            print(f"{self.name} says, I've defeated you {opponent.name}. Until next time!")
# Rogue Class (inherits from Character)
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health = 135, attack_power=20, avoid=False, heal_uses = 3)

    def choose_ability(self, opponent):
        # choose special ability
        ability = input(f"Choose your ability:\n1. Backstab 🗡️\n2. Shadow Step 🌀\nWhich one do you choose: ")
        if ability == '1':
            self.backstab(opponent)
        elif ability == '2':
            self.shadow_step(opponent)
        else:
            print(f"Invalid selection.. Defaulting to Backstab!")
            self.backstab(opponent)

    def backstab(self, opponent):
        critical_hit = random.randint(1, 10)
        #allow Rogue to punish the evil wizard with a chance of a critical hit
        if critical_hit > 8:
            damage = self.attack_power * 2
            print(f'{self.name} just performed a critical hit!')
        else:
            damage = self.attack_power
            print(f'{self.name} attacks {opponent.name} with {damage} damage!')
        opponent.health = damage

    def shadow_step(self, opponent):
        self.avoid = True
        print(f"{self.name} avoids the attack with a shadow step! ")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, avoid= False, heal_uses = 5)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        print(f'Player 2 is up! {self.name}🧙‍♂️')
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
