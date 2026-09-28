import random
import time


def printSlow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


def clear_screen():
    print("\n" * 100)


def inputSlow(prompt):
    printSlow(prompt)
    return input()


class Wizard:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 100
        self.shield = 0
        self.stunned = 0
        self.controlled = 0
        self.disarmed = 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.shield)
        self.health -= actual_damage
        self.shield = 0
        return actual_damage

    def is_alive(self):
        return self.health > 0


class Spell:
    def __init__(self, name, damage, energy_cost, description):
        self.name = name
        self.damage = damage
        self.energy_cost = energy_cost
        self.description = description


# ==========================================
# SPELLS
# ==========================================

SPELLS = {
    1: Spell("\nExpelliarmus", 15, 20, "Deals small damage\n"),
    2: Spell("\nStupefy", 25, 30, "Stun opponent\n"),
    3: Spell("\nCrucio", 35, 40, "Powerful curse\n"),
    4: Spell("\nAvada Kedavra", 50, 50, "Killing curse (risky)\n"),
    5: Spell("\nImperio", 20, 25, "Control opponent's actions\n"),
    6: Spell("\nProtego", 0, 25, "Shield spell (reduce 20 damage)\n"),
    7: Spell("\nExpecto Patronum", 30, 35, "Powerful defensive spell\n"),
}


def display_spells():
    print("\n" + "=" * 50)
    print("AVAILABLE SPELLS")
    print("=" * 50)

    for key, spell in SPELLS.items():
        print(
            f"{key}. {spell.name:<20} | "
            f"Damage: {spell.damage:<2} | "
            f"Energy: {spell.energy_cost:<2}"
        )
        print(f"   {spell.description}")

    print("=" * 50)


# ==========================================
# NORMAL PLAYER TURN
# ==========================================

def player_turn(attacker, defender):

    printSlow(f"\n{attacker.name}'s Turn\n")

    printSlow(
        f"Health: {attacker.health} | "
        f"Energy: {attacker.energy} | "
        f"Shield: {attacker.shield}"
    )

    printSlow(
        f"\n{defender.name}'s Health: {defender.health}"
    )

    # ======================================
    # STUNNED
    # ======================================

    if attacker.stunned > 0:

        printSlow(
            f"\n⚡ {attacker.name} is stunned and cannot attack!"
        )

        attacker.stunned -= 1
        return

    # ======================================
    # IMPERIO CONTROL
    # ======================================

    if attacker.controlled > 0:

        printSlow(
            f"\n🌀 {attacker.name} is under Imperio's control!"
        )

        attacker.controlled -= 1

        printSlow(
            f"\nYou control {attacker.name}'s next move!"
        )

        while True:

            display_spells()

            try:

                choice = int(
                    inputSlow(
                        f"\nChoose {attacker.name}'s spell "
                        f"(1-{len(SPELLS)}): "
                    )
                )

                if choice not in SPELLS:
                    printSlow("Invalid choice! Try again.")
                    continue

                spell = SPELLS[choice]

                if attacker.energy < spell.energy_cost:

                    printSlow(
                        f"Not enough energy! "
                        f"{attacker.name} has "
                        f"{attacker.energy} energy."
                    )

                    continue

                attacker.energy -= spell.energy_cost

                # ----------------------------------
                # CONTROLLED PROTEGO
                # ----------------------------------

                if spell.name == "\nProtego":

                    attacker.shield += 20

                    printSlow(
                        f"\n🌀 You force {attacker.name} "
                        f"to cast Protego!"
                    )

                    printSlow(
                        f"\n🛡️ {attacker.name}'s shield is raised!"
                    )

                # ----------------------------------
                # CONTROLLED SPELL DAMAGES THEMSELVES
                # ----------------------------------

                else:

                    damage = spell.damage

                    if attacker.disarmed > 0:
                        damage = int(damage * 0.5)

                    actual_damage = attacker.take_damage(damage)

                    printSlow(
                        f"\n🌀 You force {attacker.name} "
                        f"to cast {spell.name} on themselves!"
                    )

                    printSlow(
                        f"\n💥 {attacker.name} takes "
                        f"{actual_damage} damage!"
                    )

                attacker.energy = min(
                    100,
                    attacker.energy + 10
                )

                return

            except ValueError:

                printSlow(
                    "Please enter a number."
                )

    # ======================================
    # DISARMED
    # ======================================

    if attacker.disarmed > 0:

        printSlow(
            f"\n🪄 {attacker.name} is disarmed! "
            f"Spell damage reduced!"
        )

        attacker.disarmed -= 1

    # ======================================
    # NORMAL SPELL SELECTION
    # ======================================

    while True:

        display_spells()

        try:

            choice = int(
                inputSlow(
                    f"\n{attacker.name}, "
                    f"choose a spell (1-{len(SPELLS)}): "
                )
            )

            if choice not in SPELLS:

                printSlow(
                    "Invalid choice! Try again."
                )

                continue

            spell = SPELLS[choice]

            if attacker.energy < spell.energy_cost:

                printSlow(
                    f"Not enough energy! "
                    f"You have {attacker.energy}, "
                    f"but need {spell.energy_cost}."
                )

                continue

            # Use energy
            attacker.energy -= spell.energy_cost

            # ==================================
            # PROTEGO
            # ==================================

            if spell.name == "\nProtego":

                attacker.shield += 20

                printSlow(
                    f"\n✨ {attacker.name} casts {spell.name}!"
                )

                printSlow(
                    "\n🛡️ Shield raised! "
                    "(blocks up to 20 damage)"
                )

            # ==================================
            # EXPELLIARMUS
            # ==================================

            elif spell.name == "\nExpelliarmus":

                defender.disarmed = 1

                damage = spell.damage

                if attacker.disarmed > 0:
                    damage = int(damage * 0.5)

                actual_damage = defender.take_damage(
                    damage
                )

                printSlow(
                    f"\n✨ {attacker.name} casts {spell.name}!"
                )

                printSlow(
                    f"\n🪄 {defender.name} is disarmed!"
                )

                printSlow(
                    f"\n💥 {defender.name} takes "
                    f"{actual_damage} damage!"
                )

            # ==================================
            # STUPEFY
            # ==================================

            elif spell.name == "\nStupefy":

                defender.stunned = 1

                damage = spell.damage

                if attacker.disarmed > 0:
                    damage = int(damage * 0.5)

                actual_damage = defender.take_damage(
                    damage
                )

                printSlow(
                    f"\n✨ {attacker.name} casts {spell.name}!"
                )

                printSlow(
                    f"\n⚡ {defender.name} is stunned!"
                )

                printSlow(
                    f"\n💥 {defender.name} takes "
                    f"{actual_damage} damage!"
                )

            # ==================================
            # IMPERIO
            # ==================================

            elif spell.name == "\nImperio":

                defender.controlled = 1

                damage = spell.damage

                if attacker.disarmed > 0:
                    damage = int(damage * 0.5)

                actual_damage = defender.take_damage(
                    damage
                )

                printSlow(
                    f"\n✨ {attacker.name} casts {spell.name}!"
                )

                printSlow(
                    f"\n🌀 {defender.name} falls under control!"
                )

                printSlow(
                    f"\n💥 {defender.name} takes "
                    f"{actual_damage} damage!"
                )

                printSlow(
                    f"\n🌀 On {defender.name}'s next turn, "
                    f"you will control their spell!"
                )

            # ==================================
            # EXPECTO PATRONUM
            # ==================================

            elif spell.name == "\nExpecto Patronum":

                attacker.shield += 30

                damage = spell.damage

                if attacker.disarmed > 0:
                    damage = int(damage * 0.5)

                actual_damage = defender.take_damage(
                    damage
                )

                printSlow(
                    f"\n✨ {attacker.name} casts {spell.name}!"
                )

                printSlow(
                    f"\n🌟 A Patronus protects "
                    f"{attacker.name}!"
                )

                printSlow(
                    f"\n💥 {defender.name} takes "
                    f"{actual_damage} damage!"
                )

            # ==================================
            # NORMAL DAMAGE SPELL
            # ==================================

            else:

                crit_chance = random.random()

                if crit_chance > 0.8:

                    damage = int(
                        spell.damage * 1.5
                    )

                    is_crit = True

                else:

                    damage = spell.damage
                    is_crit = False

                if attacker.disarmed > 0:
                    damage = int(damage * 0.5)

                actual_damage = defender.take_damage(
                    damage
                )

                printSlow(
                    f"\n✨ {attacker.name} casts "
                    f"{spell.name}!"
                )

                if is_crit:

                    printSlow(
                        "\n⚡ CRITICAL HIT! ⚡"
                    )

                printSlow(
                    f"\n💥 {defender.name} takes "
                    f"{actual_damage} damage!"
                )

            # Restore energy
            attacker.energy = min(
                100,
                attacker.energy + 10
            )

            break

        except ValueError:

            print(
                "Please enter a number between 1 and 7."
            )


# ==========================================
# AI VS AI DUEL
# ==========================================

def aiduel():

    wizard1 = Wizard(
        random.choice([
            "Voldemort",
            "Harry",
            "Lucius",
            "Draco",
            "Severus",
            "Bellatrix",
            "Sirius",
            "Remus",
            "Albus",
            "Minerva",
            "Ron",
            "Hermione",
            "Neville",
            "Luna",
            "Ginny",
            "Fred",
            "George"
        ])
    )

    wizard2 = Wizard(
        random.choice([
            "Voldemort",
            "Harry",
            "Lucius",
            "Draco",
            "Severus",
            "Bellatrix",
            "Sirius",
            "Remus",
            "Albus",
            "Minerva",
            "Ron",
            "Hermione",
            "Neville",
            "Luna",
            "Ginny",
            "Fred",
            "George"
        ])
    )

    round_num = 1

    while wizard1.is_alive() and wizard2.is_alive():

        print(f"\n{'=' * 50}")
        print(f"AI DUEL - ROUND {round_num}")
        print(f"{'=' * 50}")

        printSlow(
            f"\n{wizard1.name}'s Health: "
            f"{wizard1.health} | Energy: "
            f"{wizard1.energy} | Shield: "
            f"{wizard1.shield}\n"
        )

        printSlow(
            f"{wizard2.name}'s Health: "
            f"{wizard2.health} | Energy: "
            f"{wizard2.energy} | Shield: "
            f"{wizard2.shield}"
        )

        # ======================================
        # AI 1
        # ======================================

        if wizard1.stunned > 0:

            printSlow(
                f"\n\n⚡ {wizard1.name} is stunned!"
            )

            wizard1.stunned -= 1

        elif wizard1.controlled > 0:

            # AI 1 is controlled.
            # AI 2 controls its next spell.

            printSlow(
                f"\n\n🌀 {wizard1.name} is "
                f"under Imperio's control!"
            )

            wizard1.controlled -= 1

            available_spells = [
                s for s in SPELLS.values()
                if wizard1.energy >= s.energy_cost
            ]

            if available_spells:

                spell = random.choice(
                    available_spells
                )

                wizard1.energy -= spell.energy_cost

                if spell.name == "\nProtego":

                    wizard1.shield += 20

                    printSlow(
                        f"\n🌀 {wizard2.name} controls "
                        f"{wizard1.name}'s move!"
                    )

                    printSlow(
                        f"\n🛡️ {wizard1.name} casts Protego!"
                    )

                else:

                    damage = spell.damage

                    actual_damage = wizard1.take_damage(
                        damage
                    )

                    printSlow(
                        f"\n🌀 {wizard2.name} forces "
                        f"{wizard1.name} to cast "
                        f"{spell.name} on themselves!"
                    )

                    printSlow(
                        f"\n💥 {wizard1.name} takes "
                        f"{actual_damage} damage!"
                    )

                wizard1.energy = min(
                    100,
                    wizard1.energy + 10
                )

        else:

            available_spells = [
                s for s in SPELLS.values()
                if wizard1.energy >= s.energy_cost
            ]

            if available_spells:

                spell = random.choice(
                    available_spells
                )

                wizard1.energy -= spell.energy_cost

                # AI 1 uses Imperio
                if spell.name == "\nImperio":

                    wizard2.controlled = 1

                    damage = spell.damage

                    actual_damage = wizard2.take_damage(
                        damage
                    )

                    printSlow(
                        f"\n{wizard1.name} casts Imperio!"
                    )

                    printSlow(
                        f"\n🌀 {wizard2.name} falls "
                        f"under control!"
                    )

                    printSlow(
                        f"\n💥 {wizard2.name} takes "
                        f"{actual_damage} damage!"
                    )

                elif spell.name == "\nProtego":

                    wizard1.shield += 20

                    printSlow(
                        f"\n{wizard1.name} casts Protego!"
                    )

                else:

                    damage = spell.damage

                    if random.random() > 0.8:
                        damage = int(damage * 1.5)

                        printSlow(
                            "\n⚡ CRITICAL HIT! ⚡"
                        )

                    actual_damage = wizard2.take_damage(
                        damage
                    )

                    printSlow(
                        f"\n{wizard1.name} casts "
                        f"{spell.name}!"
                    )

                    printSlow(
                        f"\n💥 {wizard2.name} takes "
                        f"{actual_damage} damage!"
                    )

                wizard1.energy = min(
                    100,
                    wizard1.energy + 10
                )

        if not wizard2.is_alive():
            break

        # ======================================
        # AI 2
        # ======================================

        if wizard2.stunned > 0:

            printSlow(
                f"\n\n⚡ {wizard2.name} is stunned!"
            )

            wizard2.stunned -= 1

        elif wizard2.controlled > 0:

            # AI 2 is controlled.
            # AI 1 controls its next spell.

            printSlow(
                f"\n\n🌀 {wizard2.name} is "
                f"under Imperio's control!"
            )

            wizard2.controlled -= 1

            available_spells = [
                s for s in SPELLS.values()
                if wizard2.energy >= s.energy_cost
            ]

            if available_spells:

                spell = random.choice(
                    available_spells
                )

                wizard2.energy -= spell.energy_cost

                if spell.name == "\nProtego":

                    wizard2.shield += 20

                    printSlow(
                        f"\n🌀 {wizard1.name} controls "
                        f"{wizard2.name}'s move!"
                    )

                    printSlow(
                        f"\n🛡️ {wizard2.name} casts Protego!"
                    )

                else:

                    damage = spell.damage

                    actual_damage = wizard2.take_damage(
                        damage
                    )

                    printSlow(
                        f"\n🌀 {wizard1.name} forces "
                        f"{wizard2.name} to cast "
                        f"{spell.name} on themselves!"
                    )

                    printSlow(
                        f"\n💥 {wizard2.name} takes "
                        f"{actual_damage} damage!"
                    )

                wizard2.energy = min(
                    100,
                    wizard2.energy + 10
                )

        else:

            available_spells = [
                s for s in SPELLS.values()
                if wizard2.energy >= s.energy_cost
            ]

            if available_spells:

                spell = random.choice(
                    available_spells
                )

                wizard2.energy -= spell.energy_cost

                # AI 2 uses Imperio
                if spell.name == "\nImperio":

                    wizard1.controlled = 1

                    damage = spell.damage

                    actual_damage = wizard1.take_damage(
                        damage
                    )

                    printSlow(
                        f"\n{wizard2.name} casts Imperio!"
                    )

                    printSlow(
                        f"\n🌀 {wizard1.name} falls "
                        f"under control!"
                    )

                    printSlow(
                        f"\n💥 {wizard1.name} takes "
                        f"{actual_damage} damage!"
                    )

                elif spell.name == "\nProtego":

                    wizard2.shield += 20

                    printSlow(
                        f"\n{wizard2.name} casts Protego!"
                    )

                else:

                    damage = spell.damage

                    if random.random() > 0.8:
                        damage = int(damage * 1.5)

                        printSlow(
                            "\n⚡ CRITICAL HIT! ⚡"
                        )

                    actual_damage = wizard1.take_damage(
                        damage
                    )

                    printSlow(
                        f"\n{wizard2.name} casts "
                        f"{spell.name}!"
                    )

                    printSlow(
                        f"\n💥 {wizard1.name} takes "
                        f"{actual_damage} damage!"
                    )

                wizard2.energy = min(
                    100,
                    wizard2.energy + 10
                )

        round_num += 1

    print(f"\n{'=' * 50}")
    print("⚔️  AI DUEL COMPLETE ⚔️")
    print(f"{'=' * 50}")

    if wizard1.is_alive():

        print(
            f"\n🏆 {wizard1.name} WINS! 🏆"
        )

        print(
            f"Victory with "
            f"{wizard1.health} health remaining!"
        )

    else:

        print(
            f"\n🏆 {wizard2.name} WINS! 🏆"
        )

        print(
            f"Victory with "
            f"{wizard2.health} health remaining!"
        )

    print(
        f"\nBattle lasted {round_num} rounds!"
    )


# ==========================================
# MAIN DUEL
# ==========================================

def duel():

    print("\n" + "=" * 50)
    print("🪄 WELCOME TO HARRY POTTER WAND DUEL 🪄")
    print("=" * 50)

    print("\nChoose game mode:")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    print("3. Computer vs Computer (Watch AI duel!)")
    print("4. Clear Screen(for next duel)")
    print("5. Exit")

    mode = input("Enter choice (1-5): ")

    random_names = [
        "Voldemort",
        "Harry",
        "Lucius",
        "Draco",
        "Severus",
        "Bellatrix",
        "Sirius",
        "Remus",
        "Albus",
        "Minerva",
        "Ron",
        "Hermione",
        "Neville",
        "Luna",
        "Ginny",
        "Fred",
        "George"
    ]

    # ======================================
    # AI VS AI
    # ======================================

    if mode == "3":

        aiduel()
        return

    # ======================================
    # CLEAR
    # ======================================

    elif mode == "4":

        clear_screen()
        return

    # ======================================
    # EXIT
    # ======================================

    elif mode == "5":

        print(
            "\n⭐ Thanks for playing "
            "Harry Potter Wand Duel! ⭐"
        )

        exit()

    # ======================================
    # PLAYER VS PLAYER
    # ======================================

    elif mode == "1":

        name1 = input(
            "\nEnter wizard 1 name "
            "(Choices: Voldemort, Harry, Lucius, "
            "Draco, Severus, Bellatrix, Sirius, "
            "Remus, Albus, Minerva, Ron, Hermione, "
            "Neville, Luna, Ginny, Fred, George): "
        ).strip() or "Wizard 1"

        wizard1 = Wizard(name1)

        name2 = input(
            "\nEnter wizard 2 name "
            "(Choices: Voldemort, Harry, Lucius, "
            "Draco, Severus, Bellatrix, Sirius, "
            "Remus, Albus, Minerva, Ron, Hermione, "
            "Neville, Luna, Ginny, Fred, George): "
        ).strip() or "Wizard 2"

        wizard2 = Wizard(name2)

        ai_mode = False

    # ======================================
    # PLAYER VS COMPUTER
    # ======================================

    elif mode == "2":

        name1 = input(
            "\nEnter wizard 1 name "
            "(Choices: Voldemort, Harry, Lucius, "
            "Draco, Severus, Bellatrix, Sirius, "
            "Remus, Albus, Minerva, Ron, Hermione, "
            "Neville, Luna, Ginny, Fred, George): "
        ).strip() or "Wizard 1"

        wizard1 = Wizard(name1)

        available_names = [
            name for name in random_names
            if name != name1
        ]

        name2 = random.choice(
            available_names
        )

        wizard2 = Wizard(name2)

        ai_mode = True

    else:

        print(
            "Invalid choice. Starting "
            "Player vs Computer mode by default."
        )

        name1 = input(
            "\nEnter your wizard name: "
        ).strip() or "Wizard 1"

        wizard1 = Wizard(name1)

        available_names = [
            name for name in random_names
            if name != name1
        ]

        name2 = random.choice(
            available_names
        )

        wizard2 = Wizard(name2)

        ai_mode = True

    # ======================================
    # BATTLE LOOP
    # ======================================

    round_num = 1

    while (
        wizard1.is_alive()
        and wizard2.is_alive()
    ):

        print(f"\n{'=' * 50}")
        print(f"ROUND {round_num}")
        print(f"{'=' * 50}")

        # ==================================
        # WIZARD 1 TURN
        # ==================================

        if ai_mode:

            # Player 1 is still controlled by player
            player_turn(
                wizard1,
                wizard2
            )

        else:

            player_turn(
                wizard1,
                wizard2
            )

        # Check if wizard 2 lost
        if not wizard2.is_alive():
            break

        # ==================================
        # WIZARD 2 TURN
        # ==================================

        if ai_mode:

            # ==================================
            # AI IS STUNNED
            # ==================================

            if wizard2.stunned > 0:

                printSlow(
                    f"\n⚡ {wizard2.name} is stunned "
                    f"and cannot attack!"
                )

                wizard2.stunned -= 1

            # ==================================
            # AI IS CONTROLLED BY IMPERIO
            # ==================================

            elif wizard2.controlled > 0:

                printSlow(
                    f"\n🌀 {wizard2.name} is "
                    f"under Imperio's control!"
                )

                wizard2.controlled -= 1

                printSlow(
                    f"\n🌀 You control "
                    f"{wizard2.name}'s next move!"
                )

                # IMPORTANT:
                # The player gets to choose the AI's
                # spell, and the AI damages itself.

                while True:

                    display_spells()

                    try:

                        choice = int(
                            inputSlow(
                                f"\nChoose {wizard2.name}'s "
                                f"spell (1-{len(SPELLS)}): "
                            )
                        )

                        if choice not in SPELLS:

                            printSlow(
                                "Invalid choice! Try again."
                            )

                            continue

                        spell = SPELLS[choice]

                        if wizard2.energy < spell.energy_cost:

                            printSlow(
                                f"Not enough energy! "
                                f"{wizard2.name} only has "
                                f"{wizard2.energy}."
                            )

                            continue

                        wizard2.energy -= spell.energy_cost

                        # --------------------------------
                        # AI CONTROLLED PROTEGO
                        # --------------------------------

                        if spell.name == "\nProtego":

                            wizard2.shield += 20

                            printSlow(
                                f"\n🌀 You force "
                                f"{wizard2.name} to cast "
                                f"Protego!"
                            )

                            printSlow(
                                f"\n🛡️ {wizard2.name}'s "
                                f"shield is raised!"
                            )

                        # --------------------------------
                        # AI CONTROLLED SPELL
                        # DAMAGES ITSELF
                        # --------------------------------

                        else:

                            damage = spell.damage

                            actual_damage = wizard2.take_damage(
                                damage
                            )

                            printSlow(
                                f"\n🌀 You force "
                                f"{wizard2.name} to cast "
                                f"{spell.name} on themselves!"
                            )

                            printSlow(
                                f"\n💥 {wizard2.name} takes "
                                f"{actual_damage} damage!"
                            )

                        wizard2.energy = min(
                            100,
                            wizard2.energy + 10
                        )

                        break

                    except ValueError:

                        print(
                            "Please enter a number "
                            "between 1 and 7."
                        )

            # ==================================
            # NORMAL AI TURN
            # ==================================

            else:

                available_spells = [
                    s for s in SPELLS.values()
                    if wizard2.energy >= s.energy_cost
                ]

                if available_spells:

                    # Smart AI:
                    # Use Protego if health is low.

                    if (
                        wizard2.health < 40
                        and SPELLS[6].energy_cost
                        <= wizard2.energy
                    ):

                        spell = SPELLS[6]

                    else:

                        spell = random.choice(
                            available_spells
                        )

                else:

                    wizard2.energy = 100

                    spell = random.choice(
                        list(SPELLS.values())
                    )

                printSlow(
                    f"\n{wizard2.name}'s Turn!"
                )

                printSlow(
                    f"\nHealth: {wizard2.health} | "
                    f"Energy: {wizard2.energy}"
                )

                printSlow(
                    f"\n{wizard1.name}'s Health: "
                    f"{wizard1.health}"
                )

                wizard2.energy -= spell.energy_cost

                # ----------------------------------
                # AI PROTEGO
                # ----------------------------------

                if spell.name == "\nProtego":

                    wizard2.shield += 20

                    print(
                        f"\n✨ {wizard2.name} "
                        f"casts Protego!"
                    )

                    print(
                        "🛡️ Shield raised!"
                    )

                # ----------------------------------
                # AI IMPERIO
                # ----------------------------------

                elif spell.name == "\nImperio":

                    wizard1.controlled = 1

                    damage = spell.damage

                    actual_damage = wizard1.take_damage(
                        damage
                    )

                    print(
                        f"\n✨ {wizard2.name} "
                        f"casts Imperio!"
                    )

                    print(
                        f"🌀 {wizard1.name} "
                        f"falls under control!"
                    )

                    print(
                        f"💥 {wizard1.name} takes "
                        f"{actual_damage} damage!"
                    )

                    print(
                        f"🌀 {wizard1.name}'s next turn "
                        f"will be controlled by "
                        f"{wizard2.name}!"
                    )

                # ----------------------------------
                # AI STUPEFY
                # ----------------------------------

                elif spell.name == "\nStupefy":

                    wizard1.stunned = 1

                    damage = spell.damage

                    actual_damage = wizard1.take_damage(
                        damage
                    )

                    print(
                        f"\n✨ {wizard2.name} "
                        f"casts Stupefy!"
                    )

                    print(
                        f"⚡ {wizard1.name} is stunned!"
                    )

                    print(
                        f"💥 {wizard1.name} takes "
                        f"{actual_damage} damage!"
                    )

                # ----------------------------------
                # AI EXPELLIARMUS
                # ----------------------------------

                elif spell.name == "\nExpelliarmus":

                    wizard1.disarmed = 1

                    damage = spell.damage

                    actual_damage = wizard1.take_damage(
                        damage
                    )

                    print(
                        f"\n✨ {wizard2.name} "
                        f"casts Expelliarmus!"
                    )

                    print(
                        f"🪄 {wizard1.name} is disarmed!"
                    )

                    print(
                        f"💥 {wizard1.name} takes "
                        f"{actual_damage} damage!"
                    )

                # ----------------------------------
                # AI EXPECTO PATRONUM
                # ----------------------------------

                elif spell.name == "\nExpecto Patronum":

                    wizard2.shield += 30

                    damage = spell.damage

                    actual_damage = wizard1.take_damage(
                        damage
                    )

                    print(
                        f"\n✨ {wizard2.name} "
                        f"casts Expecto Patronum!"
                    )

                    print(
                        f"🌟 A Patronus protects "
                        f"{wizard2.name}!"
                    )

                    print(
                        f"💥 {wizard1.name} takes "
                        f"{actual_damage} damage!"
                    )

                # ----------------------------------
                # NORMAL AI SPELL
                # ----------------------------------

                else:

                    crit = random.random() > 0.8

                    if crit:

                        damage = int(
                            spell.damage * 1.5
                        )

                    else:

                        damage = spell.damage

                    print(
                        f"\n✨ {wizard2.name} "
                        f"casts {spell.name}!"
                    )

                    actual_damage = wizard1.take_damage(
                        damage
                    )

                    if crit:

                        print(
                            "⚡ CRITICAL HIT! ⚡"
                        )

                    print(
                        f"💥 {wizard1.name} takes "
                        f"{actual_damage} damage!"
                    )

                wizard2.energy = min(
                    100,
                    wizard2.energy + 10
                )

            input(
                "\nPress Enter to continue..."
            )

        else:

            # Player 2
            player_turn(
                wizard2,
                wizard1
            )

        # Check if wizard 1 lost
        if not wizard1.is_alive():
            break

        round_num += 1

    # ======================================
    # DUEL COMPLETE
    # ======================================

    print(f"\n{'=' * 50}")
    print("⚔️  DUEL COMPLETE ⚔️")
    print(f"{'=' * 50}")

    if wizard1.is_alive():

        print(
            f"\n🏆 {wizard1.name} WINS! 🏆"
        )

        print(
            f"Victory with "
            f"{wizard1.health} health remaining!"
        )

    else:

        print(
            f"\n🏆 {wizard2.name} WINS! 🏆"
        )

        print(
            f"Victory with "
            f"{wizard2.health} health remaining!"
        )

    print(
        f"\nBattle lasted {round_num} rounds!"
    )


# ==========================================
# MAIN GAME LOOP
# ==========================================

if __name__ == "__main__":

    while True:

        duel()

        play_again = input(
            "\n\nWould you like to duel again? "
            "(yes/no): "
        ).lower()

        if (
            play_again != "yes"
            and play_again != "y"
        ):

            print(
                "\n⭐ Thanks for playing "
                "Harry Potter Wand Duel! ⭐"
            )

            break