import random

def acquire_item(inventory, item):
    """Adds an item to the inventory and displays a message."""
    inventory.append(item)
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """Displays the current inventory."""
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """Handles the dungeon exploration and challenges."""
    for room in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = room
        print(f"\n{room_description}")
        
        try:
            room[1] = "modified item"
        except TypeError:
            print("Error: Tuples are immutable and cannot be modified.")
        
        if item:
            acquire_item(inventory, item)
        
        if challenge_type == "puzzle":
            print("You encounter a puzzle!")
            choice = input("Do you want to solve it? (solve/skip): ").strip().lower()
            if choice == "solve":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])
                else:
                    print(challenge_outcome[1])
                    player_health += challenge_outcome[2]
        
        elif challenge_type == "trap":
            print("You see a potential trap!")
            choice = input("Do you want to disarm it? (disarm/bypass): ").strip().lower()
            if choice == "disarm":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])
                else:
                    print(challenge_outcome[1])
                    player_health += challenge_outcome[2]
        
        elif challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        
        if player_health <= 0:
            print("You are barely alive!")
            player_health = 0
        
        display_inventory(inventory)
        
    print(f"\nYou exit the dungeon with {player_health} health.")
    return player_health, inventory

def main():
    """Main game function."""
    player_health = 100
    inventory = []
    
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]
    
    print("Welcome to the adventure game!")
    player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)
    print("Game over.")

if __name__ == "__main__":
    main()# Your code goes here
