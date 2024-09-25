# Trevor Spence
# Welcome message and game instructions
print("Welcome to Beneath the Surface - a text-based adventure game!")
print("In this game, you will explore various rooms and collect items to complete your quest.")
print("You can move between rooms by typing 'move _____' (north, south, east, or west).")
print("You can also pick up items in a room by typing 'get'.")
print("Your current location and available items will be displayed after each action.")
print("Type 'help' at any time to see these instructions again.")
print('\n')

# Define the rooms and their properties
#FIX ME add more detail explanation of the rooms
#FIX ME add more detail descriptions of the items in the rooms
rooms = {
    "Ladder Room": {"description": "You are in the Ladder Room. There is a large metal door block by massive chains "
                                   "on the north wall and doors to your east and west.",
                    "items": [],
                    "connections": {"east": "Lab", "west": "Library", "north": "Locked Metal Door"}},

    "Library": {"description": "You are in the Library. There are shelves full of books.",
                "items": ["Grandpa's Notebook"],
                "connections": {"east": "Ladder Room", "north": "West Corridor"}},

    "West Corridor": {"description": "You are in the West Corridor. It's dimly lit.",
                      "items": ["Blue Furby"],
                      "connections": {"north": "Altar Room", "south": "Library"}},

    "Altar Room": {"description": "You are in the Altar Room. There is an altar with a Prayer of Protection.",
                   "items": ["Prayer of Protection"],
                   "connections": {"east": "West Corridor"}},

    "Armory": {"description": "You are in the Armory. There is Glowing Leather Armor here.",
               "items": ["Glowing Leather Armor"],
               "connections": {"south": "West Corridor", "east": "Storage Room"}},

    "Storage Room": {"description": "You are in the Storage Room. There is a Missing Jewel Crown here.",
                     "items": ["Missing Jewel Crown"],
                     "connections": {"west": "Armory", "east": "Trophy Room"}},

    "Trophy Room": {"description": "You are in the Trophy Room. There is an Engraved Great Sword here.",
                    "items": ["Engraved Great Sword"],
                    "connections": {"west": "Storage Room", "south": "East Corridor"}},

    "East Corridor": {"description": "You are in the East Corridor. It's quiet here.",
                      "items": ["White Porcelain Cat"],
                      "connections": {"north": "Trophy Room", "east": "Ritual Room", "south": "Lab"}},

    "Ritual Room": {"description": "You are in the Ritual Room. There is a Swirling Black Gemstone here.",
                    "items": ["Swirling Black Gemstone"],
                    "connections": {"west": "East Corridor"}},

    "Lab": {"description": "You are in the Lab. There are various scientific equipment.",
            "items": ["Potion of Enduring Light"],
            "connections": {"north": "East Corridor", "west": "Ladder Room"}},

    "Locked Metal Door": {"description": "You are facing a Large Metal Door blocked by massive chains. It seems "
                                         "heavily secured.",
                          "items": [],
                          "connections": {"south": "Ladder Room"}},
    # Other room definition
    "Exit": {"description": "You are at the Exit. Type 'exit' to leave the game.",
             "items": [],
             "connections": {}}
}
# Start the game at the "Ladder Room"
current_room = "Ladder Room"
inventory = []

while True:
    print(rooms[current_room]["description"])
    if rooms[current_room]["items"]:
        print("Items in this room:", ", ".join(rooms[current_room]["items"]))

    action_input = input("What would you like to do? (Enter 'help' for options): ").lower().split()
    action = action_input[0]

    if action == "help":
        possible_actions = ["move (direction)", "get"] #FIX ME Change to make actions happen in one statement
        if current_room == "Locked Metal Door":
            possible_actions.append("open")
        print("Possible actions:", ", ".join(possible_actions))
    elif action == "move":
        if len(action_input) > 1:
            direction = action_input[1]
        else:
            direction = input("Which direction would you like to move? (north, south, east, west): ").lower()
        if direction in rooms[current_room]["connections"]:
            current_room = rooms[current_room]["connections"][direction]
        else:
            print("There is no path in that direction.")
    elif action == "get":
        if rooms[current_room]["items"]:
            item_to_pick_up = rooms[current_room]["items"][0]
            inventory.append(item_to_pick_up)
            print("You picked up", item_to_pick_up)
            rooms[current_room]["items"].remove(item_to_pick_up)
        else:
            print("There are no items to pick up in this room.")
    elif action == "open" and current_room == "Locked Metal Door":
        if "completed jewel crown" in inventory:
            required_items = {"prayer of protection", "glowing leather armor", "potion of enduring light",
                              "grandpa's notebook", "completed jewel crown", "engraved great sword"}
            if required_items.issubset(inventory):
                print("The heavy chains recoil into the wall and the metal door opens.")
                print("Congratulations! You have unlocked the door and completed your quest. You win!")
                break
            else:
                print("The heavy chains recoil into the wall and the metal door opens. Suddenly, the villain Mor'oth "
                      "appears out of the darkness and attacks!")
                print("Without the rest of the items, you are no match for the powerful demon. You have been "
                      "defeated. Game over!")
                break
        else:
            print("You do not have the required item(s) to open this door.")
    elif action == "exit":
        current_room = "Exit"
    else:
        print("Invalid action. Type 'help' for options.")



