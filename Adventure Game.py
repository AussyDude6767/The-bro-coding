import time
import random


# ==========================================
# SLOW PRINT
# ==========================================

def printSlow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


# ==========================================
# START GAME
# ==========================================

print("======================================")
print("       WELCOME TO THE ADVENTURE")
print("======================================")

name = input("What is your name, adventurer? ")

Coins = 100
Health = 100
Strength = 100

weapon = "fists"
armor = "none"

inventory = []

printSlow(f"\nWelcome, {name}!\n")
printSlow(f"Coins = {Coins}\n")
printSlow(f"Health = {Health}\n")
printSlow(f"Strength = {Strength}\n")

printSlow("\nYou have arrived at a small village.")
printSlow("\nYou can buy weapons, food, or armor before beginning your adventure.\n")


# ==========================================
# VILLAGE SHOP
# ==========================================

buy_choice = input(
    "\nWhat would you like to buy? "
    "Your choices are weapons, food, armor or nothing: "
)

# ==========================================
# WEAPONS
# ==========================================

if buy_choice == "weapons":

    printSlow("\nWelcome to the village blacksmith's shop!\n")

    printSlow(
        "Your choices are:\n"
        "dagger - 20 coins - +10 strength\n"
        "sword - 30 coins - +20 strength\n"
        "axe - 40 coins - +30 strength\n"
    )

    weapon_choice = input("What weapon would you like? ")

    if weapon_choice == "dagger":

        if Coins >= 20:
            Coins = Coins - 20
            Strength = Strength + 10
            weapon = "dagger"
            inventory.append("dagger")

            print("You got the lv.1 dagger!")
            print(f"Strength = {Strength}")
        else:
            print("You don't have enough coins!")

    elif weapon_choice == "sword":

        if Coins >= 30:
            Coins = Coins - 30
            Strength = Strength + 20
            weapon = "sword"
            inventory.append("sword")

            print("You got the lv.1 sword!")
            print(f"Strength = {Strength}")
        else:
            print("You don't have enough coins!")

    elif weapon_choice == "axe":

        if Coins >= 40:
            Coins = Coins - 40
            Strength = Strength + 30
            weapon = "axe"
            inventory.append("axe")

            print("You got the lv.1 axe!")
            print(f"Strength = {Strength}")
        else:
            print("You don't have enough coins!")

    else:
        print("That is not one of the weapons.")

# ==========================================
# FOOD
# ==========================================

elif buy_choice == "food":

    printSlow("\nWelcome to the village food shop!\n")

    printSlow(
        "Your choices are:\n"
        "beef - 40 coins - +10 health\n"
        "chicken - 30 coins - +7 health\n"
        "lettuce - 20 coins - +4 health\n"
    )

    food_choice = input("What food would you like? ")

    if food_choice == "beef":

        if Coins >= 40:
            Coins = Coins - 40
            Health = Health + 10
            inventory.append("beef")

            print("You got beef!")
            print(f"Health = {Health}")
        else:
            print("You don't have enough coins!")

    elif food_choice == "chicken":

        if Coins >= 30:
            Coins = Coins - 30
            Health = Health + 7
            inventory.append("chicken")

            print("You got chicken!")
            print(f"Health = {Health}")
        else:
            print("You don't have enough coins!")

    elif food_choice == "lettuce":

        if Coins >= 20:
            Coins = Coins - 20
            Health = Health + 4
            inventory.append("lettuce")

            print("You got lettuce!")
            print(f"Health = {Health}")
        else:
            print("You don't have enough coins!")

    else:
        print("That is not one of the foods.")

# ==========================================
# ARMOR
# ==========================================

elif buy_choice == "armor":

    printSlow("\nWelcome to the village armor shop!\n")

    printSlow(
        "Your choices are:\n"
        "helmet - 50 coins\n"
        "chestplate - 60 coins\n"
        "leggings - 40 coins\n"
        "boots - 30 coins\n"
        "gloves - 20 coins\n"
    )

    armor_choice = input("What armor would you like? ")

    if armor_choice == "helmet":

        if Coins >= 50:
            Coins = Coins - 50
            inventory.append("helmet")

            helmet_choice = input(
                "You got the helmet! "
                "Would you like to put it on now or later? "
            )

            if helmet_choice == "put on":
                armor = "helmet"
                Health = Health + 4
                print("You put on the helmet.")
                print(f"Health = {Health}")

            else:
                print("You put the helmet in your backpack.")

        else:
            print("You don't have enough coins!")

    elif armor_choice == "chestplate":

        if Coins >= 60:
            Coins = Coins - 60
            inventory.append("chestplate")

            chestplate_choice = input(
                "You got the chestplate! "
                "Would you like to put it on now or later? "
            )

            if chestplate_choice == "put on":
                armor = "chestplate"
                Health = Health + 5
                Strength = Strength + 5

                print("You put on the chestplate.")
                print(f"Health = {Health}")
                print(f"Strength = {Strength}")

            else:
                print("You put the chestplate in your backpack.")

        else:
            print("You don't have enough coins!")

    elif armor_choice == "leggings":

        if Coins >= 40:
            Coins = Coins - 40
            inventory.append("leggings")

            leggings_choice = input(
                "You got the leggings! "
                "Would you like to put them on now or later? "
            )

            if leggings_choice == "put on":
                armor = "leggings"
                Health = Health + 3
                Strength = Strength + 3

                print("You put on the leggings.")
                print(f"Health = {Health}")
                print(f"Strength = {Strength}")

            else:
                print("You put the leggings in your backpack.")

        else:
            print("You don't have enough coins!")

    elif armor_choice == "boots":

        if Coins >= 30:
            Coins = Coins - 30
            inventory.append("boots")

            boot_choice = input(
                "You got the boots! "
                "Would you like to put them on now or later? "
            )

            if boot_choice == "put on":
                armor = "boots"
                Health = Health + 2
                Strength = Strength + 2

                print("You put on the boots.")
                print(f"Health = {Health}")
                print(f"Strength = {Strength}")

            else:
                print("You put the boots in your backpack.")

        else:
            print("You don't have enough coins!")

    elif armor_choice == "gloves":

        if Coins >= 20:
            Coins = Coins - 20
            inventory.append("gloves")

            glove_choice = input(
                "You got the gloves! "
                "Would you like to put them on now or later? "
            )

            if glove_choice == "put on":
                armor = "gloves"
                Health = Health + 1
                Strength = Strength + 1

                print("You put on the gloves.")
                print(f"Health = {Health}")
                print(f"Strength = {Strength}")

            else:
                print("You put the gloves in your backpack.")

        else:
            print("You don't have enough coins!")

else:

    printSlow("\nYou decided not to buy anything.")


# ==========================================
# STATUS AFTER SHOPPING
# ==========================================

printSlow("\n======================================\n")
printSlow("YOUR CURRENT STATUS\n")
printSlow("======================================\n")

print(f"Coins = {Coins}")
print(f"Health = {Health}")
print(f"Strength = {Strength}")
print(f"Weapon = {weapon}")
print(f"Armor = {armor}")

print("\nYour inventory:")
print(inventory)


# ==========================================
# NIGHT 1
# ==========================================

printSlow(
    "\n\nYou are now ready to leave the village."
    "\nNight time is approaching."
    "\nLuckily, you packed one sleeping bag."
    "\nYou must be careful not to lose it.\n"
)

sleep_hunt_choice = input(
    "Would you like to immediately sleep or eat dinner? "
)

if sleep_hunt_choice == "sleep":

    printSlow("\nYou set up your sleeping bag.")
    printSlow("\nYou sleep through the night...")
    time.sleep(1)

    Health = Health + 5
    Strength = Strength + 5

    printSlow("\nYou wake up feeling rested!")
    print(f"\nHealth = {Health}")
    print(f"Strength = {Strength}")

elif sleep_hunt_choice == "eat":

    if "beef" in inventory or "chicken" in inventory or "lettuce" in inventory:

        print("\nYou look through your backpack.")

        if "beef" in inventory:
            food_choice = "beef"
            Health = Health + 10
            inventory.remove("beef")

        elif "chicken" in inventory:
            food_choice = "chicken"
            Health = Health + 7
            inventory.remove("chicken")

        else:
            food_choice = "lettuce"
            Health = Health + 4
            inventory.remove("lettuce")

        print(f"You eat your {food_choice}.")
        print(f"Health = {Health}")

        printSlow("\nYou set up your sleeping bag.")
        printSlow("\nYou sleep through the night...")
        printSlow("\nYou wake up the next morning!")

    else:

        print("\nYou have no food!")

        eat_choice = input(
            "Would you like to hunt for food or sleep? "
        )

        if eat_choice == "sleep":

            Health = Health + 5
            Strength = Strength + 5

            printSlow("\nYou sleep through the night...")
            printSlow("\nYou wake up in the morning!")

        elif eat_choice == "hunt":

            printSlow(
                "\nYou walk into the forest looking for food..."
            )

            printSlow(
                "\nYou suddenly see a deer!"
            )

            hunt_choice = input(
                "\nWould you like to hit it or wait? "
            )

            if hunt_choice == "hit":

                printSlow(
                    "\nYou carefully move closer to the deer."
                )

                hit_choice = input(
                    "Will you hit it now or wait? "
                )

                if hit_choice == "hit":

                    printSlow(
                        "\nYou successfully hunted the deer!"
                    )

                    printSlow(
                        "\nYou now have enough food for dinner."
                    )

                    Health = Health + 15

                    print(f"Health = {Health}")

                else:

                    printSlow(
                        "\nThe deer runs away."
                    )

            elif hunt_choice == "wait":

                printSlow(
                    "\nYou wait quietly."
                )

                printSlow(
                    "\nYou hear something behind you..."
                )

                printSlow(
                    "\nIt is a wolf!"
                )

                wolf_choice = input(
                    "\nDo you fight the wolf or run? "
                )

                if wolf_choice == "fight":

                    damage = random.randint(5, 15)
                    Health = Health - damage
                    Strength = Strength + 5

                    printSlow(
                        f"\nYou fight the wolf!"
                    )

                    print(
                        f"\nThe wolf hurt you for {damage} health."
                    )

                    print(
                        f"Health = {Health}"
                    )

                    printSlow(
                        "\nYou manage to scare the wolf away."
                    )

                else:

                    printSlow(
                        "\nYou run away from the wolf!"
                    )

        else:

            printSlow(
                "\nYou decide to stay still and sleep."
            )


# ==========================================
# DAY 2 - RIVER
# ==========================================

printSlow(
    "\n\n======================================"
    "\nDAY 2"
    "\n======================================\n"
)

printSlow(
    "\nYou continue walking through the wilderness."
)

printSlow(
    "\nAfter several hours, you come across a raging river."
)

river_choice = input(
    "\nWould you like to swim across, go around, or build a raft? "
)


# ==========================================
# SWIM
# ==========================================

if river_choice == "swim":

    printSlow(
        "\nYou jump into the river!"
    )

    Strength = Strength - 3

    print(f"Strength = {Strength}")

    printSlow(
        "\nThe current is extremely strong..."
    )

    printSlow(
        "\nBut you make it safely to the other side!"
    )

    printSlow(
        "\nYou find a treasure chest!"
    )

    dagger_choice = input(
        "\nInside is a lv.2 dagger. "
        "Would you like to use it? "
    )

    if dagger_choice == "use":

        weapon = "lv.2 dagger"
        Strength = Strength + 20
        inventory.append("lv.2 dagger")

        printSlow(
            "\nYou equip the lv.2 dagger!"
        )

        print(f"Strength = {Strength}")

    else:

        printSlow(
            "\nYou leave the dagger in the chest."
        )


# ==========================================
# GO AROUND
# ==========================================

elif river_choice == "go around":

    printSlow(
        "\nYou decide to walk around the river."
    )

    printSlow(
        "\nAfter a while, you hear a loud growl."
    )

    printSlow(
        "\nA grizzly bear walks onto the path!"
    )

    bear_choice = input(
        "\nWill you fight the bear or run? "
    )

    if bear_choice == "fight":

        printSlow(
            f"\nYou prepare your {weapon}."
        )

        damage = random.randint(5, 15)

        Strength = Strength - 5
        Health = Health - damage

        print(
            f"\nThe fight hurts you for {damage} health."
        )

        print(f"Health = {Health}")
        print(f"Strength = {Strength}")

        printSlow(
            "\nYou manage to defeat the bear!"
        )

        bear_eat_choice = input(
            "\nWould you like to take the bear with you "
            "for food or leave it? "
        )

        if bear_eat_choice == "take":

            inventory.append("bear meat")

            printSlow(
                "\nYou take some bear meat with you."
            )

        else:

            printSlow(
                "\nYou leave the bear and continue."
            )

    elif bear_choice == "run":

        printSlow(
            "\nYou run as fast as you can!"
        )

        printSlow(
            "\nThe bear stops chasing you."
        )

        printSlow(
            "\nYou continue around the river."
        )


# ==========================================
# BUILD RAFT
# ==========================================

elif river_choice == "build a raft":

    printSlow(
        "\nYou search around for some wood."
    )

    printSlow(
        "\nYou find several strong branches."
    )

    printSlow(
        "\nYou build a small raft."
    )

    printSlow(
        "\nYou push the raft into the river."
    )

    raft_choice = input(
        "\nDo you want to trust the raft or swim instead? "
    )

    if raft_choice == "trust":

        printSlow(
            "\nYou climb onto the raft."
        )

        printSlow(
            "\nThe raft moves surprisingly well!"
        )

        printSlow(
            "\nYou make it safely across the river!"
        )

        printSlow(
            "\nYou find a treasure chest on the other side."
        )

        sword_choice = input(
            "\nInside is a lv.2 sword. "
            "Would you like to use it? "
        )

        if sword_choice == "use":

            weapon = "lv.2 sword"
            Strength = Strength + 25
            inventory.append("lv.2 sword")

            printSlow(
                "\nYou equip the lv.2 sword!"
            )

            print(f"Strength = {Strength}")

        else:

            printSlow(
                "\nYou leave the sword in the chest."
            )

    else:

        printSlow(
            "\nYou decide to swim."
        )

        Strength = Strength - 3

        print(
            f"Strength = {Strength}"
        )

        printSlow(
            "\nYou make it across safely!"
        )

else:

    printSlow(
        "\nYou stand beside the river for a moment."
    )

    printSlow(
        "\nYou decide to follow the river until you find a bridge."
    )


# ==========================================
# RANDOM EVENT AFTER RIVER
# ==========================================

printSlow(
    "\n\nYou continue your adventure..."
)

random_event = random.randint(1, 3)

if random_event == 1:

    printSlow(
        "\nYou find 25 coins on the ground!"
    )

    Coins = Coins + 25

elif random_event == 2:

    printSlow(
        "\nYou find a mysterious old map."
    )

    inventory.append("old map")

else:

    printSlow(
        "\nYou find nothing unusual."
    )


# ==========================================
# DAY 3 - FOREST
# ==========================================

printSlow(
    "\n\n======================================"
    "\nDAY 3"
    "\n======================================\n"
)

printSlow(
    "\nYou enter a huge forest."
)

printSlow(
    "\nThe trees are so tall that you can barely see the sky."
)

forest_choice = input(
    "\nDo you want to follow a trail, climb a hill, or explore the forest? "
)

if forest_choice == "trail":

    printSlow(
        "\nYou follow the old trail."
    )

    printSlow(
        "\nAfter walking for a while, you find an abandoned camp."
    )

    camp_choice = input(
        "\nWould you like to search the camp or leave it alone? "
    )

    if camp_choice == "search":

        treasure = random.randint(10, 40)
        Coins = Coins + treasure

        printSlow(
            f"\nYou find {treasure} coins!"
        )

        print(f"Coins = {Coins}")

    else:

        printSlow(
            "\nYou leave the camp alone."
        )


elif forest_choice == "climb":

    printSlow(
        "\nYou climb the hill."
    )

    printSlow(
        "\nFrom the top, you can see a giant castle far away!"
    )

    inventory.append("castle information")

    printSlow(
        "\nYou now know where you are going."
    )


elif forest_choice == "explore":

    printSlow(
        "\nYou explore the forest."
    )

    printSlow(
        "\nYou find a strange wooden sign."
    )

    printSlow(
        "\nIt says: THE OLD MINE."
    )

    mine_choice = input(
        "\nDo you want to enter the mine? "
    )

    if mine_choice == "yes":

        printSlow(
            "\nYou enter the dark mine."
        )

        printSlow(
            "\nYou find some shiny rocks."
        )

        mine_reward = random.randint(20, 50)
        Coins = Coins + mine_reward

        printSlow(
            f"\nYou collect the rocks and sell them for {mine_reward} coins!"
        )

        print(f"Coins = {Coins}")

    else:

        printSlow(
            "\nYou decide not to enter the mine."
        )

else:

    printSlow(
        "\nYou choose your own path through the forest."
    )


# ==========================================
# NIGHT 3
# ==========================================

printSlow(
    "\n\nThe sun begins to disappear."
)

printSlow(
    "\nYou need to find somewhere to sleep."
)

camp_choice = input(
    "\nWould you like to sleep under a tree or search for a cave? "
)

if camp_choice == "tree":

    printSlow(
        "\nYou sleep under a large tree."
    )

    Health = Health + 5
    Strength = Strength + 5

    printSlow(
        "\nYou wake up feeling rested."
    )

elif camp_choice == "cave":

    printSlow(
        "\nYou find a small cave."
    )

    printSlow(
        "\nIt looks safe."
    )

    cave_sleep = input(
        "\nWould you like to sleep inside? "
    )

    if cave_sleep == "yes":

        Health = Health + 8
        Strength = Strength + 8

        printSlow(
            "\nYou sleep peacefully inside the cave."
        )

    else:

        printSlow(
            "\nYou decide to sleep outside instead."
        )

        Health = Health + 3
        Strength = Strength + 3


# ==========================================
# DAY 4 - MOUNTAINS
# ==========================================

printSlow(
    "\n\n======================================"
    "\nDAY 4"
    "\n======================================\n"
)

printSlow(
    "\nYou leave the forest and reach a huge mountain."
)

printSlow(
    "\nThe castle you saw before is on the other side."
)

mountain_choice = input(
    "\nWould you like to climb the mountain, "
    "look for a tunnel, or walk around it? "
)

if mountain_choice == "climb":

    printSlow(
        "\nYou begin climbing."
    )

    Strength = Strength - 10

    print(f"Strength = {Strength}")

    printSlow(
        "\nThe climb is difficult..."
    )

    printSlow(
        "\nBut you make it to the top!"
    )

    printSlow(
        "\nYou can see the castle clearly now."
    )


elif mountain_choice == "tunnel":

    printSlow(
        "\nYou search for a tunnel."
    )

    printSlow(
        "\nYou discover a hidden tunnel!"
    )

    printSlow(
        "\nYou walk through it."
    )

    printSlow(
        "\nThe tunnel takes you almost all the way to the castle."
    )

    inventory.append("secret tunnel")


elif mountain_choice == "walk around":

    printSlow(
        "\nYou walk around the mountain."
    )

    printSlow(
        "\nIt takes a long time."
    )

    Health = Health - 5

    print(
        f"Health = {Health}"
    )

    printSlow(
        "\nEventually, you reach the other side."
    )

else:

    printSlow(
        "\nYou wait for a while before deciding."
    )

    printSlow(
        "\nYou eventually find a path around the mountain."
    )


# ==========================================
# THE MYSTERIOUS TRAVELER
# ==========================================

printSlow(
    "\n\nWhile walking toward the castle..."
)

printSlow(
    "\nYou see a mysterious traveler sitting beside the road."
)

traveler_choice = input(
    "\nWill you talk to the traveler or keep walking? "
)

if traveler_choice == "talk":

    printSlow(
        "\nThe traveler looks at you."
    )

    printSlow(
        "\nTraveler: 'You are heading toward the castle, aren't you?'"
    )

    printSlow(
        "\nTraveler: 'Be careful. Something strange has taken control of it.'"
    )

    printSlow(
        "\nThe traveler gives you 30 coins."
    )

    Coins = Coins + 30

    print(
        f"Coins = {Coins}"
    )

    inventory.append("traveler's advice")

else:

    printSlow(
        "\nYou keep walking."
    )

    printSlow(
        "\nYou wonder who the traveler was.")


# ==========================================
# DAY 5 - CASTLE
# ==========================================

printSlow(
    "\n\n======================================"
    "\nDAY 5"
    "\n======================================\n"
)

printSlow(
    "\nYou finally reach the castle."
)

printSlow(
    "\nThe giant doors slowly open."
)

printSlow(
    "\nInside the castle, everything is strangely quiet."
)

castle_choice = input(
    "\nDo you want to explore the library, "
    "go to the throne room, or search the basement? "
)


# ==========================================
# LIBRARY
# ==========================================

if castle_choice == "library":

    printSlow(
        "\nYou enter the enormous library."
    )

    printSlow(
        "\nYou find an old book about the castle."
    )

    printSlow(
        "\nThe book explains that the castle has a secret entrance."
    )

    inventory.append("castle book")

    printSlow(
        "\nYou now know about the secret entrance."
    )


# ==========================================
# BASEMENT
# ==========================================

elif castle_choice == "basement":

    printSlow(
        "\nYou walk down into the basement."
    )

    printSlow(
        "\nIt is dark and dusty."
    )

    printSlow(
        "\nYou discover a locked treasure chest."
    )

    chest_choice = input(
        "\nDo you want to try to open it? "
    )

    if chest_choice == "yes":

        printSlow(
            "\nYou open the chest!"
        )

        reward = random.randint(30, 70)
        Coins = Coins + reward

        printSlow(
            f"\nYou find {reward} coins!"
        )

        print(f"Coins = {Coins}")

    else:

        printSlow(
            "\nYou leave the chest alone."
        )


# ==========================================
# THRONE ROOM
# ==========================================

elif castle_choice == "throne room":

    printSlow(
        "\nYou walk into the throne room."
    )

    printSlow(
        "\nA strange shadow is sitting on the throne."
    )

    printSlow(
        "\nThe shadow stands up."
    )

    printSlow(
        "\n'YOU SHOULD NOT HAVE COME HERE.'"
    )

else:

    printSlow(
        "\nYou wander through the castle."
    )

    printSlow(
        "\nEventually, you find the throne room."
    )


# ==========================================
# FINAL BATTLE
# ==========================================

printSlow(
    "\n\nSuddenly..."
)

printSlow(
    "\nBOOM!"
)

printSlow(
    "\nThe castle shakes."
)

printSlow(
    "\nA huge dark guardian appears!"
)

printSlow(
    "\nThe guardian blocks the exit."
)

printSlow(
    "\nYou must fight your way through!"
)


enemy_health = 100

while enemy_health > 0 and Health > 0:

    print("\n======================================")
    print(f"Your Health = {Health}")
    print(f"Your Strength = {Strength}")
    print(f"Guardian Health = {enemy_health}")
    print("======================================")

    battle_choice = input(
        "Do you want to attack, defend, or run? "
    )

    if battle_choice == "attack":

        damage = random.randint(10, 20)

        if weapon == "lv.2 sword":
            damage = damage + 10

        elif weapon == "lv.2 dagger":
            damage = damage + 8

        elif weapon == "axe":
            damage = damage + 5

        enemy_health = enemy_health - damage

        printSlow(
            f"\nYou attack with your {weapon}!"
        )

        print(
            f"\nYou deal {damage} damage!"
        )

        if enemy_health > 0:

            enemy_damage = random.randint(5, 15)

            if armor != "none":
                enemy_damage = enemy_damage - 2

            if enemy_damage < 0:
                enemy_damage = 0

            Health = Health - enemy_damage

            printSlow(
                f"\nThe guardian attacks you for {enemy_damage} damage!"
            )

    elif battle_choice == "defend":

        printSlow(
            "\nYou defend yourself."
        )

        enemy_damage = random.randint(2, 7)

        Health = Health - enemy_damage

        print(
            f"\nYou take only {enemy_damage} damage."
        )

    elif battle_choice == "run":

        printSlow(
            "\nYou try to run..."
        )

        run_chance = random.randint(1, 3)

        if run_chance == 1:

            printSlow(
                "\nYou escape the castle!"
            )

            printSlow(
                "\nYou survived, but you did not complete your mission."
            )

            Health = 0

        else:

            printSlow(
                "\nThe guardian blocks your path!"
            )

            enemy_damage = random.randint(5, 12)
            Health = Health - enemy_damage

            print(
                f"\nYou lose {enemy_damage} health."
            )

    else:

        printSlow(
            "\nYou hesitate."
        )

        printSlow(
            "\nThe guardian attacks!"
        )

        enemy_damage = random.randint(8, 15)
        Health = Health - enemy_damage

        print(
            f"\nYou lose {enemy_damage} health."
        )


# ==========================================
# ENDINGS
# ==========================================

if Health <= 0:

    printSlow(
        "\n\n======================================"
        "\nGAME OVER"
        "\n======================================"
    )

    printSlow(
        "\nYou were defeated in the castle."
    )

    printSlow(
        "\nYour adventure has ended."
    )

elif enemy_health <= 0:

    printSlow(
        "\n\n======================================"
        "\nYOU WON!"
        "\n======================================"
    )

    printSlow(
        "\nThe guardian falls to the ground."
    )

    printSlow(
        "\nThe castle becomes quiet."
    )

    printSlow(
        "\nYou discover a golden key behind the throne."
    )

    printSlow(
        "\nThe key opens a secret treasure room!"
    )

    printSlow(
        "\nInside are hundreds of coins and priceless treasures."
    )

    Coins = Coins + 200

    print(
        f"\nYou gained 200 coins!"
    )

    print(
        f"Final Coins = {Coins}"
    )

    printSlow(
        "\nYou leave the castle as a hero."
    )

    printSlow(
        f"\nCongratulations, {name}!"
    )

    printSlow(
        "\nYou completed the Adventure Game!"
    )


# ==========================================
# FINAL STATUS
# ==========================================

print("\n\n======================================")
print("          FINAL STATUS")
print("======================================")

print(f"Name = {name}")
print(f"Coins = {Coins}")
print(f"Health = {Health}")
print(f"Strength = {Strength}")
print(f"Weapon = {weapon}")
print(f"Armor = {armor}")

print("\nInventory:")

if len(inventory) == 0:

    print("Nothing")

else:

    for item in inventory:
        print("-", item)

print("\n======================================")
print("       THANKS FOR PLAYING!")
print("======================================")