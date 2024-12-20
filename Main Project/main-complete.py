from characters import Character, Warrior, Mage, Archer, Paladin, Rogue, EvilWizard
# New Section. Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  
    print("4. Paladin") 
    print("5. Rogue")  
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name.title())
    elif class_choice == '2':
        return Mage(name.title())
    elif class_choice == '3':
        return Archer(name.title())
    elif class_choice == '4':
        return Paladin(name.title())
    elif class_choice == '5':
        return Rogue(name.title())
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name.title())

# Last Section. Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn Player 1 ---")
        print("1. Attack ⚔️")
        print("2. Use Special Ability ✨")
        print("3. Heal ❤️‍🩹")
        print("4. View Stats 📊")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.choose_ability(wizard) 
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            # Check if the player is able to avoid the attack
            if player.avoid == True:
                print(f"{wizard.name} says, I'll get you next time!")
                player.avoid = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()