print(
    "Pick your Trainer:\n\nAsh: \nPikachu - Thunderbolt, Thunder, Quick Attack, Thunder Shock\nCharmander - Dragon Breath, Flame Thrower, Fire Fang, Slash\nButterfree - Confusion, Bug Buzz, Air Cutter, Psybeam\n\nBrock: \nOnix - Tackle, Rock Throw, Rock Slide, Smack Down\nGeodude - Tackle, Rollout, Rock Blast, Bulldoze\nBulbasaur - Tackle, Vine Whip, Razor Leaf, Seed Bomb\n\nMisty: \nStaryu - Tackle, Rapid Spin, Water Gun, Bubble Beam\nMagikarp - Splash, Flail, Tackle\nSquirtle - Tackle, Water Gun, Aqua Tail, Skull Bash"
)

trainer = input("> ")
while True:
    if trainer == "Ash":
        pokemon1 = "Pikachu"
        pokemon2 = "Charmander"
        pokemon3 = "Butterfree"
        print(
            "- My name is Ash Ketchum from Pallet Town. My dream is to become the greatest Pokemon Trainer of them all."
        )
        break
    elif trainer == "Brock":
        pokemon1 = "Onix"
        pokemon2 = "Geodude"
        pokemon3 = "Bulbasaur"
        print(
            "- My name is Brock Harrison from Pewter City. My dream is to become a Pokemon Doctor."
        )
        break
    elif trainer == "Misty":
        pokemon1 = "Staryu"
        pokemon2 = "Magikarp"
        pokemon3 = "Squirtle"
        print(
            "- My name is Misty Williams from Cerulean City. My dream is to become a Water Pokemon Master."
        )
        break
    else:
        print("Please choose a trainer.")
        trainer = input("> ")

choose_legendary = input(
    "Choose a legendary Pokemon:\nZapdos\nMoltres\nArticuno\n> ")
print(
    "- You are now heading to Viridian City.\n- On the way, Team Rocket Leader Giovanni tries to steal your Pokemon.\n\n!!TIME TO BATTLE!!"
)

pikachu_health = 100
charm_health = 100
butter_health = 100
onix_health = 100
geo_health = 100
bulb_health = 100
star_health = 100
magik_health = 100
squirt_health = 100
legendary_health = 200

import random

if trainer == "Ash":
    choose_pokemon = input("\nChoose your Pokemon: ")
    print(f"You chose {choose_pokemon}!")
    while True:
        if legendary_health <= 0:
            print(
                "You have defeated the almighty Team Rocket Leader Giovanni!")
            break
        elif legendary_health <= 0 and pikachu_health <= 0 and charm_health <= 0 and butter_health <= 0:
            print("All the Pokemon fainted and its a Tie!")
            break
        else:
            if choose_pokemon == "Pikachu":
                if pikachu_health <= 0 and charm_health <= 0 and butter_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if pikachu_health <= 0:
                        choose_pokemon = input("Choose your Pokemon:")
                    else:
                        print(
                            f"Pikachu's Health: {pikachu_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Pikachu do?: ")
                        if choose_attack == "Thunderbolt":
                            thunderbolt = random.randint(25, 30)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 80:
                                print(
                                    f"Pikachu used Thunder Bolt and dealt {thunderbolt} damage to {choose_legendary}!"
                                )
                                legendary_health -= thunderbolt
                            else:
                                print(
                                    "Pikachu used Thunderbolt but he missed!")
                        elif choose_attack == "Thunder":
                            thunder = random.randint(30, 35)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 75:
                                print(
                                    f"Pikachu used Thunder and dealt {thunder} damage to {choose_legendary}!"
                                )
                                legendary_health -= thunder
                            else:
                                print("Pikachu used Thunder but he missed!")
                        elif choose_attack == "Quick Attack":
                            quick = random.randint(10, 15)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 95:
                                print(
                                    f"Pikachu used Quick Attack and dealt {quick} damage to {choose_legendary}!"
                                )
                                legendary_health -= quick
                            else:
                                print(
                                    "Pikachu used Quick Attack but he missed!")
                        elif choose_attack == "Thunder Shock":
                            shock = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 95:
                                print(
                                    f"Pikachu used Thunder Shock and dealt {shock} damage to {choose_legendary}!"
                                )
                                legendary_health -= shock
                            else:
                                print(
                                    "Pikachu used Thunder Shock but he missed!"
                                )
            elif choose_pokemon == "Charmander":
                if pikachu_health <= 0 and charm_health <= 0 and butter_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if charm_health <= 0:
                        choose_pokemon = input("Choose your Pokemon:")
                    else:
                        print(
                            f"Charmander's Health: {charm_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Charmander do?: ")
                        if choose_attack == "Dragon Breath":
                          breath = random.randint(15, 20)
                          hit_chance = random.randint(1, 100)
                          if hit_chance <= 80:
                            print(
                                f"Charmander used Dragon Breath and dealt {breath} damage to {choose_legendary}!"
                            )
                            legendary_health -= breath
                          else:
                            print(
                                "Charmander used Dragon Breath but he missed!")
                        elif choose_attack == "Flame Thrower":
                          throw = random.randint(25, 30)
                          hit_chance = random.randint(1, 100)
                          if hit_chance <= 75:
                            print(
                                f"Charmander used Flame Thrower and dealt {throw} damage to {choose_legendary} !"
                            )
                            legendary_health -= throw
                          else:
                            print(
                                "Charmander used Flame Thrower but he missed!")
                        elif choose_attack == "Fire Fang":
                          fang = random.randint(15, 20)
                          hit_chance = random.randint(1, 100)
                          if hit_chance <= 85:
                            print(
                                f"Charmander used Fire Fang and dealt {fang} damage to {choose_legendary}!"
                            )
                            legendary_health -= fang
                          else:
                            print("Charmander used Fire Fang but he missed!")
                        elif choose_attack == "Slash":
                          slash = random.randint(20, 25)
                          hit_chance = random.randint(1, 100)
                          if hit_chance <= 85:
                            print(
                                f"Charmander used Slash and dealt {slash} damage to {choose_legendary}!"
                            )
                            legendary_health -= slash
                          else:
                            print("Charmander used Slash but he missed!")
            elif choose_pokemon == "Butterfree":
                if pikachu_health <= 0 and charm_health <= 0 and butter_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if butter_health <= 0:
                        choose_pokemon = input("Choose your Pokemon: ")
                        if choose_pokemon != "Pikachu" or choose_pokemon != "Charmander" or choose_pokemon != "Butterfree":
                            print("Please choose a Pokemon")
                            choose_pokemon = input("Choose your Pokemon: ")
                    else:
                        print(
                            f"Butterfree's Health: {butter_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Butterfree do?: ")
                        if choose_attack == "Confusion":
                          fusion = random.randint(15, 20)
                          hit_chance = random.randint(1, 100)
                          if hit_chance <= 85:
                            print(
                                f"Butterfree used Confusion and dealt {fusion} damage to {choose_legendary}!"
                            )
                            legendary_health -= fusion
                          else:
                            print("Butterfree used Confusion but he missed!")
                        elif choose_attack == "Bug Buzz":
                          buzz = random.randint(20, 25)
                          hit_chance = random.randint(1, 100)
                          if hit_chance <= 75:
                            print(
                                f"Butterfree used Bug Buzz and dealt {buzz} damage to {choose_legendary}!"
                            )
                            legendary_health -= buzz
                          else:
                            print("Butterfree used Bug Buzz but he missed!")
                        elif choose_attack == "Air Cutter":
                          cut = random.randint(20, 25)
                          hit_chance = random.randint(1, 100)
                          if hit_chance <= 78:
                            print(
                                f"Butterfree used Air Cutter and dealt {cut} damage to {choose_legendary}!"
                            )
                            legendary_health -= cut
                          else:
                            print("Butterfree used Air Cutter but he missed!")
                        elif choose_attack == "Psybeam":
                          beam = random.randint(10, 15)
                          hit_chance = random.randint(1, 100)
                          if hit_chance <= 90:
                            print(
                                f"Butterfree used Psybeam and dealt {beam} damage to {choose_legendary}!"
                            )
                            legendary_health -= beam
                          else:
                            print("Butterfree used Psybeam but he missed!")
            elif choose_pokemon != "Pikachu" or choose_pokemon != "Charmander" or choose_pokemon != "Butterfree":
                print("Please choose a Pokemon")
                choose_pokemon = input("Choose your Pokemon: ")
            if choose_legendary == "Zapdos":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    pluck = random.randint(35, 40)
                    if hit_chance <= 85:
                        print(
                            f"Zapdos used Pluck and dealt {pluck} to {choose_pokemon}!"
                        )
                    if choose_pokemon == "Pikachu":
                        pikachu_health -= pluck
                    elif choose_pokemon == "Charmander":
                        charm_health -= pluck
                    elif choose_pokemon == "Butterfree":
                        butter_health -= pluck
                    elif choose_pokemon == "Onix":
                        onix_health -= pluck
                    elif choose_pokemon == "Geodude":
                        geo_health -= pluck
                    elif choose_pokemon == "Bulbasaur":
                        bulb_health -= pluck
                    elif choose_pokemon == "Staryu":
                        star_health -= pluck
                    elif choose_pokemon == "Magikarp":
                        magik_health -= pluck
                    elif choose_pokemon == "Squirtle":
                        squirt_health -= pluck
                    else:
                        print("Zapdos used Pluck but he missed!")
                elif legendary_attack == 2:
                    power = random.randint(20, 25)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Ancient Power and dealt {power} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= power
                        elif choose_pokemon == "Charmander":
                            charm_health -= power
                        elif choose_pokemon == "Butterfree":
                            butter_health -= power
                        elif choose_pokemon == "Onix":
                            onix_health -= power
                        elif choose_pokemon == "Geodude":
                            geo_health -= power
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= power
                        elif choose_pokemon == "Staryu":
                            star_health -= power
                        elif choose_pokemon == "Magikarp":
                            magik_health -= power
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= power
                    else:
                        print("Zapdos used Ancient Power but he missed!")
                elif legendary_attack == 3:
                    drill = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Drill Peck and dealt {drill} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= drill
                        elif choose_pokemon == "Charmander":
                            charm_health -= drill
                        elif choose_pokemon == "Butterfree":
                            butter_health -= drill
                        elif choose_pokemon == "Onix":
                            onix_health -= drill
                        elif choose_pokemon == "Geodude":
                            geo_health -= drill
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= drill
                        elif choose_pokemon == "Staryu":
                            star_health -= drill
                        elif choose_pokemon == "Magikarp":
                            magik_health -= drill
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= drill
                    else:
                        print("Zapdos used Drill Peck but he missed!")
                elif legendary_attack == 4:
                    thunder2 = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Thunder and dealt {thunder2} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= thunder2
                        elif choose_pokemon == "Charmander":
                            charm_health -= thunder2
                        elif choose_pokemon == "Butterfree":
                            butter_health -= thunder2
                        elif choose_pokemon == "Onix":
                            onix_health -= thunder2
                        elif choose_pokemon == "Geodude":
                            geo_health -= thunder2
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= thunder2
                        elif choose_pokemon == "Staryu":
                            star_health -= thunder2
                        elif choose_pokemon == "Magikarp":
                            magik_health -= thunder2
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= thunder2
                    else:
                        print("Zapdos used Thunder but he missed!")
            if choose_legendary == "Moltres":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    cane = random.randint(40, 45)
                    if hit_chance <= 85:
                        print(
                            f"Moltres used Hurricane and dealt {cane} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= cane
                        elif choose_pokemon == "Charmander":
                            charm_health -= cane
                        elif choose_pokemon == "Butterfree":
                            butter_health -= cane
                        elif choose_pokemon == "Onix":
                            onix_health -= cane
                        elif choose_pokemon == "Geodude":
                            geo_health -= cane
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= cane
                        elif choose_pokemon == "Staryu":
                            star_health -= cane
                        elif choose_pokemon == "Magikarp":
                            magik_health -= cane
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= cane
                    else:
                        print("Moltres used Hurricane but he missed!")
                elif legendary_attack == 2:
                    attack = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Sky Attack and dealt {attack} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= attack
                        elif choose_pokemon == "Charmander":
                            charm_health -= attack
                        elif choose_pokemon == "Butterfree":
                            butter_health -= attack
                        elif choose_pokemon == "Onix":
                            onix_health -= attack
                        elif choose_pokemon == "Geodude":
                            geo_health -= attack
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= attack
                        elif choose_pokemon == "Staryu":
                            star_health -= attack
                        elif choose_pokemon == "Magikarp":
                            magik_health -= attack
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= attack
                    else:
                        print("Moltres used Sky Attack but he missed!")
                elif legendary_attack == 3:
                    wave = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Heat Wave and dealt {wave} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= wave
                        elif choose_pokemon == "Charmander":
                            charm_health -= wave
                        elif choose_pokemon == "Butterfree":
                            butter_health -= wave
                        elif choose_pokemon == "Onix":
                            onix_health -= wave
                        elif choose_pokemon == "Geodude":
                            geo_health -= wave
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= wave
                        elif choose_pokemon == "Staryu":
                            star_health -= wave
                        elif choose_pokemon == "Magikarp":
                            magik_health -= wave
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= wave
                    else:
                        print("Moltres used Heat Wave but he missed!")
                elif legendary_attack == 4:
                    slash2 = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Air Slash and dealt {slash2} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= slash2
                        elif choose_pokemon == "Charmander":
                            charm_health -= slash2
                        elif choose_pokemon == "Butterfree":
                            butter_health -= slash2
                        elif choose_pokemon == "Onix":
                            onix_health -= slash2
                        elif choose_pokemon == "Geodude":
                            geo_health -= slash2
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= slash2
                        elif choose_pokemon == "Staryu":
                            star_health -= slash
                        elif choose_pokemon == "Magikarp":
                            magik_health -= slash2
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= slash2
                    else:
                        print("Moltres used Air Slash but he missed!")
            if choose_legendary == "Articuno":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    cane1 = random.randint(40, 45)
                    if hit_chance <= 80:
                        print(
                            f"Articuno used Hurricane and dealt {cane1} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= cane1
                        elif choose_pokemon == "Charmander":
                            charm_health -= cane1
                        elif choose_pokemon == "Butterfree":
                            butter_health -= cane1
                        elif choose_pokemon == "Onix":
                            onix_health -= cane1
                        elif choose_pokemon == "Geodude":
                            geo_health -= cane1
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= cane1
                        elif choose_pokemon == "Staryu":
                            star_health -= cane1
                        elif choose_pokemon == "Magikarp":
                            magik_health -= cane1
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= cane1
                    else:
                        print("Articuno used Hurricane but he missed!")
                elif legendary_attack == 2:
                    dry = random.randint(35, 40)
                    if hit_chance <= 85:
                        print(
                            f"Articuno used Freeze-Dry and dealt {dry} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= dry
                        elif choose_pokemon == "Charmander":
                            charm_health -= dry
                        elif choose_pokemon == "Butterfree":
                            butter_health -= dry
                        elif choose_pokemon == "Onix":
                            onix_health -= dry
                        elif choose_pokemon == "Geodude":
                            geo_health -= dry
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= dry
                        elif choose_pokemon == "Staryu":
                            star_health -= dry
                        elif choose_pokemon == "Magikarp":
                            magik_health -= dry
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= dry
                    else:
                        print("Articuno used Freeze-Dry but he missed!")
                elif legendary_attack == 3:
                    shard = random.randint(20, 25)
                    if hit_chance <= 90:
                        print(
                            f"Articuno used Ice Shard and dealt {shard} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= shard
                        elif choose_pokemon == "Charmander":
                            charm_health -= shard
                        elif choose_pokemon == "Butterfree":
                            butter_health -= shard
                        elif choose_pokemon == "Onix":
                            onix_health -= shard
                        elif choose_pokemon == "Geodude":
                            geo_health -= shard
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= shard
                        elif choose_pokemon == "Staryu":
                            star_health -= shard
                        elif choose_pokemon == "Magikarp":
                            magik_health -= shard
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= shard
                    else:
                        print("Articuno used Ice Shard but he missed!")
                elif legendary_attack == 4:
                    beam1 = random.randint(30, 35)
                    if hit_chance <= 85:
                        print(
                            f"Articuno used Ice Beam and dealt {beam1} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= beam1
                        elif choose_pokemon == "Charmander":
                            charm_health -= beam1
                        elif choose_pokemon == "Butterfree":
                            butter_health -= beam1
                        elif choose_pokemon == "Onix":
                            onix_health -= beam1
                        elif choose_pokemon == "Geodude":
                            geo_health -= beam1
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= beam1
                        elif choose_pokemon == "Staryu":
                            star_health -= beam1
                        elif choose_pokemon == "Magikarp":
                            magik_health -= beam1
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= beam1
                    else:
                        print("Articuno used Ice Beam but he missed!")
if trainer == "Brock":
    choose_pokemon = input("Choose your Pokemon: ")
    print(f"You chose {choose_pokemon}!")
    while True:
        if legendary_health <= 0:
            print(
                "You have defeated the almighty Team Rocket Leader Giovanni!")
            break
        elif legendary_health <= 0 and onix_health <= 0 and geo_health <= 0 and bulb_health <= 0:
            print("All the Pokemon fainted and its a Tie!")
            break
        else:
            if choose_pokemon == "Onix":
                if onix_health <= 0 and geo_health <= 0 and bulb_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if onix_health <= 0:
                        choose_pokemon = input("Choose your Pokemon:")
                    else:
                        print(
                            f"Onix's Health: {onix_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Onix do?: ")
                        if choose_attack == "Tackle":
                            tackle1 = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Onix used Tackle and dealt {tackle1} damage to {choose_legendary}!"
                                )
                                legendary_health -= tackle1
                            else:
                                print("Onix used Tackle but he missed!")
                        elif choose_attack == "Rock Throw":
                            throw1 = random.randint(20, 25)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 80:
                                print(
                                    f"Onix used Rock Throw and dealt {throw1} damage to {choose_legendary}!"
                                )
                                legendary_health -= throw1
                            else:
                                print("Onix used Rock Throw but he missed!")
                        elif choose_attack == "Rock Slide":
                            slide = random.randint(25, 30)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 75:
                                print(
                                    f"Onix used Rock Slide and dealt {slide} damage to {choose_legendary}!"
                                )
                                legendary_health -= slide
                            else:
                                print("Onix used Rock Slide but he missed!")
                        elif choose_attack == "Smack Down":
                            down = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Onix used Smack Down and dealt {down} damage to {choose_legendary}!"
                                )
                                legendary_health -= down
                            else:
                                print("Onix used Smack Down but he missed!")
            elif choose_pokemon == "Geodude":
                if onix_health <= 0 and geo_health <= 0 and bulb_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if geo_health <= 0:
                        choose_pokemon = input("Choose your Pokemon: ")
                    else:
                        print(
                            f"Geodude's Health: {geo_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Geodude do?: ")
                        if choose_attack == "Tackle":
                            tackle2 = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Geodude used Tackle and dealt {tackle2} damage to {choose_legendary}!"
                                )
                                legendary_health -= tackle2
                            else:
                                print("Geodude used Tackle but he missed!")
                        elif choose_attack == "Rollout":
                            roll = random.randint(20, 25)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 80:
                                print(
                                    f"Geodude used Rollout and dealt {roll} damage to {choose_legendary}!"
                                )
                                legendary_health -= roll
                            else:
                                print("Geodude used Rollout but he missed!")
                        elif choose_attack == "Rock Blast":
                            blast = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 85:
                                print(
                                    f"Geodude used Rock Blast and dealt {blast} damage to {choose_legendary}!"
                                )
                                legendary_health -= blast
                            else:
                                print("Geodude used Rock Blast but he missed!")
                        elif choose_attack == "Bulldoze":
                            doze = random.randint(25, 30)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 75:
                                print(
                                    f"Geodude used Bulldoze and dealt {doze} damage to {choose_legendary}!"
                                )
                                legendary_health -= doze
                            else:
                                print("Geodude used Bulldoze but he missed!")
            elif choose_pokemon == "Bulbasaur":
                if onix_health <= 0 and geo_health <= 0 and bulb_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if bulb_health <= 0:
                        choose_pokemon = input("Choose your Pokemon: ")
                    else:
                        print(
                            f"Bulbasaur's Health: {bulb_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Bulbasaur do?: ")
                        if choose_attack == "Tackle":
                            tackle3 = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Bulbasaur used Tackle and dealt {tackle3} damage to {choose_legendary}!"
                                )
                                legendary_health -= tackle3
                            else:
                                print("Bulbasaur used Tackle but he missed!")
                        elif choose_attack == "Vine Whip":
                            whip = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Bulbasaur used Vine Whip and dealt {whip} damage to {choose_legendary}!"
                                )
                                legendary_health -= whip
                            else:
                                print(
                                    "Bulbasaur used Vine Whip but he missed!")
                        elif choose_attack == "Razor Leaf":
                            leaf = random.randint(20, 25)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 80:
                                print(
                                    f"Bulbasaur used Razor Leaf and dealt {leaf} damage to {choose_legendary}!"
                                )
                                legendary_health -= leaf
                            else:
                                print(
                                    "Bulbasaur used Razor Leaf but he missed!")
                        elif choose_attack == "Seed Bomb":
                            bomb = random.randint(10, 15)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Bulbasaur used Seed Bomb and dealt {bomb} damage to {choose_legendary}!"
                                )
                                legendary_health -= bomb
                            else:
                                print(
                                    "Bulbasaur used Seed Bomb but he missed!")
            elif choose_pokemon != "Onix" or choose_pokemon != "Geodude" or choose_pokemon != "Bulbasaur":
                print("Please choose a Pokemon")
                choose_pokemon = input("Choose your Pokemon: ")
            if choose_legendary == "Zapdos":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    pluck = random.randint(35, 40)
                    if hit_chance <= 85:
                        print(
                            f"Zapdos used Pluck and dealt {pluck} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= pluck
                        elif choose_pokemon == "Charmander":
                            charm_health -= pluck
                        elif choose_pokemon == "Butterfree":
                            butter_health -= pluck
                        elif choose_pokemon == "Onix":
                            onix_health -= pluck
                        elif choose_pokemon == "Geodude":
                            geo_health -= pluck
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= pluck
                        elif choose_pokemon == "Staryu":
                            star_health -= pluck
                        elif choose_pokemon == "Magikarp":
                            magik_health -= pluck
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= pluck
                    else:
                        print("Zapdos used Pluck but he missed!")
                elif legendary_attack == 2:
                    power = random.randint(20, 25)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Ancient Power and dealt {power} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= power
                        elif choose_pokemon == "Charmander":
                            charm_health -= power
                        elif choose_pokemon == "Butterfree":
                            butter_health -= power
                        elif choose_pokemon == "Onix":
                            onix_health -= power
                        elif choose_pokemon == "Geodude":
                            geo_health -= power
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= power
                        elif choose_pokemon == "Staryu":
                            star_health -= power
                        elif choose_pokemon == "Magikarp":
                            magik_health -= power
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= power
                    else:
                        print("Zapdos used Ancient Power but he missed!")
                elif legendary_attack == 3:
                    drill = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Drill Peck and dealt {drill} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= drill
                        elif choose_pokemon == "Charmander":
                            charm_health -= drill
                        elif choose_pokemon == "Butterfree":
                            butter_health -= drill
                        elif choose_pokemon == "Onix":
                            onix_health -= drill
                        elif choose_pokemon == "Geodude":
                            geo_health -= drill
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= drill
                        elif choose_pokemon == "Staryu":
                            star_health -= drill
                        elif choose_pokemon == "Magikarp":
                            magik_health -= drill
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= drill
                    else:
                        print("Zapdos used Drill Peck but he missed!")
                elif legendary_attack == 4:
                    thunder2 = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Thunder and dealt {thunder2} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= thunder2
                        elif choose_pokemon == "Charmander":
                            charm_health -= thunder2
                        elif choose_pokemon == "Butterfree":
                            butter_health -= thunder2
                        elif choose_pokemon == "Onix":
                            onix_health -= thunder2
                        elif choose_pokemon == "Geodude":
                            geo_health -= thunder2
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= thunder2
                        elif choose_pokemon == "Staryu":
                            star_health -= thunder2
                        elif choose_pokemon == "Magikarp":
                            magik_health -= thunder2
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= thunder2
                    else:
                        print("Zapdos used Thunder but he missed!")
            if choose_legendary == "Moltres":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    cane = random.randint(40, 45)
                    if hit_chance <= 85:
                        print(
                            f"Moltres used Hurricane and dealt {cane} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= cane
                        elif choose_pokemon == "Charmander":
                            charm_health -= cane
                        elif choose_pokemon == "Butterfree":
                            butter_health -= cane
                        elif choose_pokemon == "Onix":
                            onix_health -= cane
                        elif choose_pokemon == "Geodude":
                            geo_health -= cane
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= cane
                        elif choose_pokemon == "Staryu":
                            star_health -= cane
                        elif choose_pokemon == "Magikarp":
                            magik_health -= cane
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= cane
                    else:
                        print("Moltres used Hurricane but he missed!")
                elif legendary_attack == 2:
                    attack = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Sky Attack and dealt {attack} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= attack
                        elif choose_pokemon == "Charmander":
                            charm_health -= attack
                        elif choose_pokemon == "Butterfree":
                            butter_health -= attack
                        elif choose_pokemon == "Onix":
                            onix_health -= attack
                        elif choose_pokemon == "Geodude":
                            geo_health -= attack
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= attack
                        elif choose_pokemon == "Staryu":
                            star_health -= attack
                        elif choose_pokemon == "Magikarp":
                            magik_health -= attack
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= attack
                    else:
                        print("Moltres used Sky Attack but he missed!")
                elif legendary_attack == 3:
                    wave = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Heat Wave and dealt {wave} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= wave
                        elif choose_pokemon == "Charmander":
                            charm_health -= wave
                        elif choose_pokemon == "Butterfree":
                            butter_health -= wave
                        elif choose_pokemon == "Onix":
                            onix_health -= wave
                        elif choose_pokemon == "Geodude":
                            geo_health -= wave
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= wave
                        elif choose_pokemon == "Staryu":
                            star_health -= wave
                        elif choose_pokemon == "Magikarp":
                            magik_health -= wave
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= wave
                    else:
                        print("Moltres used Heat Wave but he missed!")
                elif legendary_attack == 4:
                    slash2 = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Air Slash and dealt {slash2} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= slash2
                        elif choose_pokemon == "Charmander":
                            charm_health -= slash2
                        elif choose_pokemon == "Butterfree":
                            butter_health -= slash2
                        elif choose_pokemon == "Onix":
                            onix_health -= slash2
                        elif choose_pokemon == "Geodude":
                            geo_health -= slash2
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= slash2
                        elif choose_pokemon == "Staryu":
                            star_health -= slash
                        elif choose_pokemon == "Magikarp":
                            magik_health -= slash2
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= slash2
                    else:
                        print("Moltres used Air Slash but he missed!")
            if choose_legendary == "Articuno":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    cane1 = random.randint(40, 45)
                    if hit_chance <= 80:
                        print(
                            f"Articuno used Hurricane and dealt {cane1} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= cane1
                        elif choose_pokemon == "Charmander":
                            charm_health -= cane1
                        elif choose_pokemon == "Butterfree":
                            butter_health -= cane1
                        elif choose_pokemon == "Onix":
                            onix_health -= cane1
                        elif choose_pokemon == "Geodude":
                            geo_health -= cane1
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= cane1
                        elif choose_pokemon == "Staryu":
                            star_health -= cane1
                        elif choose_pokemon == "Magikarp":
                            magik_health -= cane1
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= cane1
                    else:
                        print("Articuno used Hurricane but he missed!")
                elif legendary_attack == 2:
                    dry = random.randint(35, 40)
                    if hit_chance <= 85:
                        print(
                            f"Articuno used Freeze-Dry and dealt {dry} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= dry
                        elif choose_pokemon == "Charmander":
                            charm_health -= dry
                        elif choose_pokemon == "Butterfree":
                            butter_health -= dry
                        elif choose_pokemon == "Onix":
                            onix_health -= dry
                        elif choose_pokemon == "Geodude":
                            geo_health -= dry
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= dry
                        elif choose_pokemon == "Staryu":
                            star_health -= dry
                        elif choose_pokemon == "Magikarp":
                            magik_health -= dry
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= dry
                    else:
                        print("Articuno used Freeze-Dry but he missed!")
                elif legendary_attack == 3:
                    shard = random.randint(20, 25)
                    if hit_chance <= 90:
                        print(
                            f"Articuno used Ice Shard and dealt {shard} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= shard
                        elif choose_pokemon == "Charmander":
                            charm_health -= shard
                        elif choose_pokemon == "Butterfree":
                            butter_health -= shard
                        elif choose_pokemon == "Onix":
                            onix_health -= shard
                        elif choose_pokemon == "Geodude":
                            geo_health -= shard
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= shard
                        elif choose_pokemon == "Staryu":
                            star_health -= shard
                        elif choose_pokemon == "Magikarp":
                            magik_health -= shard
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= shard
                    else:
                        print("Articuno used Ice Shard but he missed!")
                elif legendary_attack == 4:
                    beam1 = random.randint(30, 35)
                    if hit_chance <= 85:
                        print(
                            f"Articuno used Ice Beam and dealt {beam1} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= beam1
                        elif choose_pokemon == "Charmander":
                            charm_health -= beam1
                        elif choose_pokemon == "Butterfree":
                            butter_health -= beam1
                        elif choose_pokemon == "Onix":
                            onix_health -= beam1
                        elif choose_pokemon == "Geodude":
                            geo_health -= beam1
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= beam1
                        elif choose_pokemon == "Staryu":
                            star_health -= beam1
                        elif choose_pokemon == "Magikarp":
                            magik_health -= beam1
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= beam1
                    else:
                        print("Articuno used Ice Beam but he missed!")
if trainer == "Misty":
    choose_pokemon = input("Choose your Pokemon: ")
    while True:
        if legendary_health <= 0:
            print(
                "You have defeated the almighty Team Rocket Leader Giovanni!")
            break
        elif legendary_health <= 0 and star_health <= 0 and magik_health <= 0 and squirt_health <= 0:
            print("All the Pokemon fainted and its a Tie!")
            break
        else:
            if choose_pokemon == "Staryu":
                if star_health <= 0 and magik_health <= 0 and squirt_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if star_health <= 0:
                        choose_pokemon = input("Choose your Pokemon:")
                    else:
                        print(
                            f"Staryu's Health: {star_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Staryu do?: ")
                        if choose_attack == "Tackle":
                            tackle4 = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Staryu used Tackle and dealt {tackle4} damage to {choose_legendary}!"
                                )
                                legendary_health -= tackle4
                            else:
                                print("Staryu used Tackle but he missed!")
                        elif choose_attack == "Rapid Spin":
                            spin = random.randint(10, 15)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 95:
                                print(
                                    f"Staryu used Rapid Spin and dealt {spin} damage to {choose_legendary}!"
                                )
                                legendary_health -= spin
                            else:
                                print("Staryu used Rapid Spin but he missed!")
                        elif choose_attack == "Water Gun":
                            water = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 85:
                                print(
                                    f"Staryu used Water Gun and dealt {water} damage to {choose_legendary}!"
                                )
                                legendary_health -= water
                            else:
                                print("Staryu used Water Gun but he missed!")
                        elif choose_attack == "Bubble Beam":
                            beam = random.randint(20, 25)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 80:
                                print(
                                    f"Staryu used Bubble Beam and dealt {beam} damage to {choose_legendary}!"
                                )
                                legendary_health -= beam
                            else:
                                print("Staryu used Bubble Beam but he missed!")
            elif choose_pokemon == "Magikarp":
                if star_health <= 0 and magik_health <= 0 and squirt_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if magik_health <= 0:
                        choose_pokemon = input("Choose your Pokemon: ")
                    else:
                        print(
                            f"Magikarp's Health: {magik_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Magikarp do?: ")
                        if choose_attack == "Splash":
                            splish = 0
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Magikarp used Splash on {choose_legendary}\nBut it had no effect!"
                                )
                                legendary_health -= splish
                            else:
                                print("Magikarp used Splash but he missed!")
                        elif choose_attack == "Tackle":
                            tackle5 = random.randint(20, 25)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 80:
                                print(
                                    f"Magikarp used Tackle and dealt {tackle5} damage to {choose_legendary}!"
                                )
                                legendary_health -= tackle5
                            else:
                                print("Magikarp used Tackle but he missed!")
                        elif choose_attack == "Flail":
                            flail = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 85:
                                print(
                                    f"Magikarp used Flail and dealt {flail} damage to {choose_legendary}!"
                                )
                                legendary_health -= flail
                            else:
                                print("Magikarp used Flail but he missed!")
            elif choose_pokemon == "Squirtle":
                if star_health <= 0 and magik_health <= 0 and squirt_health <= 0:
                    print(
                        "You have been defeated by the almighty Team Rocket Giovanni!"
                    )
                    break
                else:
                    if squirt_health <= 0:
                        choose_pokemon = input("Choose your Pokemon: ")
                    else:
                        print(
                            f"Squirtle's Health: {squirt_health}\n{choose_legendary}'s Health: {legendary_health}"
                        )
                        choose_attack = input("What will Squirtle do?: ")
                        if choose_attack == "Tackle":
                            tackle6 = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 90:
                                print(
                                    f"Squirtle used Tackle and dealt {tackle6} damage to {choose_legendary}!"
                                )
                                legendary_health -= tackle6
                            else:
                                print("Squirtle used Tackle but he missed!")
                        elif choose_attack == "Water Gun":
                            water1 = random.randint(15, 20)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 85:
                                print(
                                    f"Squirtle used Water Gun and dealt {water1} damage to {choose_legendary}!"
                                )
                                legendary_health -= water1
                            else:
                                print("Squirtle used Water Gun but he missed!")
                        elif choose_attack == "Aqua Tail":
                            tail = random.randint(25, 30)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 75:
                                print(
                                    f"Squirtle used Aqua Tail and dealt {tail} damage to {choose_legendary}!"
                                )
                                legendary_health -= tail
                            else:
                                print("Squirtle used Aqua Tail but he missed!")
                        elif choose_attack == "Skull Bash":
                            bash = random.randint(20, 25)
                            hit_chance = random.randint(1, 100)
                            if hit_chance <= 80:
                                print(
                                    f"Squirtle used Skull Bash and dealt {bash} damage to {choose_legendary}!"
                                )
                                legendary_health -= bash
                            else:
                                print(
                                    "Squirtle used Skull Bash but he missed!")
            elif choose_pokemon != "Staryu" or choose_pokemon != "Magikarp" or choose_pokemon != "Squirtle":
                print("Please choose a Pokemon.")
                choose_pokemon = input("Choose your Pokemon: ")
            if choose_legendary == "Zapdos":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    pluck = random.randint(35, 40)
                    if hit_chance <= 85:
                        print(
                            f"Zapdos used Pluck and dealt {pluck} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= pluck
                        elif choose_pokemon == "Charmander":
                            charm_health -= pluck
                        elif choose_pokemon == "Butterfree":
                            butter_health -= pluck
                        elif choose_pokemon == "Onix":
                            onix_health -= pluck
                        elif choose_pokemon == "Geodude":
                            geo_health -= pluck
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= pluck
                        elif choose_pokemon == "Staryu":
                            star_health -= pluck
                        elif choose_pokemon == "Magikarp":
                            magik_health -= pluck
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= pluck
                    else:
                        print("Zapdos used Pluck but he missed.")
                elif legendary_attack == 2:
                    power = random.randint(20, 25)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Ancient Power and dealt {power} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= power
                        elif choose_pokemon == "Charmander":
                            charm_health -= power
                        elif choose_pokemon == "Butterfree":
                            butter_health -= power
                        elif choose_pokemon == "Onix":
                            onix_health -= power
                        elif choose_pokemon == "Geodude":
                            geo_health -= power
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= power
                        elif choose_pokemon == "Staryu":
                            star_health -= power
                        elif choose_pokemon == "Magikarp":
                            magik_health -= power
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= power
                    else:
                        print("Zapdos used Ancient Power but he missed!")
                elif legendary_attack == 3:
                    drill = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Drill Peck and dealt {drill} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= drill
                        elif choose_pokemon == "Charmander":
                            charm_health -= drill
                        elif choose_pokemon == "Butterfree":
                            butter_health -= drill
                        elif choose_pokemon == "Onix":
                            onix_health -= drill
                        elif choose_pokemon == "Geodude":
                            geo_health -= drill
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= drill
                        elif choose_pokemon == "Staryu":
                            star_health -= drill
                        elif choose_pokemon == "Magikarp":
                            magik_health -= drill
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= drill
                    else:
                        print("Zapdos used Drill Peck but he missed!")
                elif legendary_attack == 4:
                    thunder2 = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Zapdos used Thunder and dealt {thunder2} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= thunder2
                        elif choose_pokemon == "Charmander":
                            charm_health -= thunder2
                        elif choose_pokemon == "Butterfree":
                            butter_health -= thunder2
                        elif choose_pokemon == "Onix":
                            onix_health -= thunder2
                        elif choose_pokemon == "Geodude":
                            geo_health -= thunder2
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= thunder2
                        elif choose_pokemon == "Staryu":
                            star_health -= thunder2
                        elif choose_pokemon == "Magikarp":
                            magik_health -= thunder2
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= thunder2
                    else:
                        print("Zapdos used Thunder but he missed!")
            if choose_legendary == "Moltres":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    cane = random.randint(40, 45)
                    if hit_chance <= 85:
                        print(
                            f"Moltres used Hurricane and dealt {cane} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= cane
                        elif choose_pokemon == "Charmander":
                            charm_health -= cane
                        elif choose_pokemon == "Butterfree":
                            butter_health -= cane
                        elif choose_pokemon == "Onix":
                            onix_health -= cane
                        elif choose_pokemon == "Geodude":
                            geo_health -= cane
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= cane
                        elif choose_pokemon == "Staryu":
                            star_health -= cane
                        elif choose_pokemon == "Magikarp":
                            magik_health -= cane
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= cane
                    else:
                        print("Moltres used Hurricane but he missed.")
                elif legendary_attack == 2:
                    attack = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Sky Attack and dealt {attack} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= attack
                        elif choose_pokemon == "Charmander":
                            charm_health -= attack
                        elif choose_pokemon == "Butterfree":
                            butter_health -= attack
                        elif choose_pokemon == "Onix":
                            onix_health -= attack
                        elif choose_pokemon == "Geodude":
                            geo_health -= attack
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= attack
                        elif choose_pokemon == "Staryu":
                            star_health -= attack
                        elif choose_pokemon == "Magikarp":
                            magik_health -= attack
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= attack
                    else:
                        print("Moltres used Sky Attack but he missed!")
                elif legendary_attack == 3:
                    wave = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Heat Wave and dealt {wave} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= wave
                        elif choose_pokemon == "Charmander":
                            charm_health -= wave
                        elif choose_pokemon == "Butterfree":
                            butter_health -= wave
                        elif choose_pokemon == "Onix":
                            onix_health -= wave
                        elif choose_pokemon == "Geodude":
                            geo_health -= wave
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= wave
                        elif choose_pokemon == "Staryu":
                            star_health -= wave
                        elif choose_pokemon == "Magikarp":
                            magik_health -= wave
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= wave
                    else:
                        print("Moltres used Heat Wave but he missed!")
                elif legendary_attack == 4:
                    slash2 = random.randint(30, 35)
                    if hit_chance <= 90:
                        print(
                            f"Moltres used Air Slash and dealt {slash2} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= slash2
                        elif choose_pokemon == "Charmander":
                            charm_health -= slash2
                        elif choose_pokemon == "Butterfree":
                            butter_health -= slash2
                        elif choose_pokemon == "Onix":
                            onix_health -= slash2
                        elif choose_pokemon == "Geodude":
                            geo_health -= slash2
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= slash2
                        elif choose_pokemon == "Staryu":
                            star_health -= slash
                        elif choose_pokemon == "Magikarp":
                            magik_health -= slash2
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= slash2
                    else:
                        print("Moltres used Air Slash but he missed!")
            if choose_legendary == "Articuno":
                legendary_attack = random.randint(1, 4)
                hit_chance = random.randint(1, 100)
                if legendary_attack == 1:
                    cane1 = random.randint(40, 45)
                    if hit_chance <= 80:
                        print(
                            f"Articuno used Hurricane and dealt {cane1} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= cane1
                        elif choose_pokemon == "Charmander":
                            charm_health -= cane1
                        elif choose_pokemon == "Butterfree":
                            butter_health -= cane1
                        elif choose_pokemon == "Onix":
                            onix_health -= cane1
                        elif choose_pokemon == "Geodude":
                            geo_health -= cane1
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= cane1
                        elif choose_pokemon == "Staryu":
                            star_health -= cane1
                        elif choose_pokemon == "Magikarp":
                            magik_health -= cane1
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= cane1
                    else:
                        print("Articuno used Hurricane but he missed.")
                elif legendary_attack == 2:
                    hit_chance = random.randint(1, 100)
                    dry = random.randint(35, 40)
                    if hit_chance <= 85:
                        print(
                            f"Articuno used Freeze-Dry and dealt {dry} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= dry
                        elif choose_pokemon == "Charmander":
                            charm_health -= dry
                        elif choose_pokemon == "Butterfree":
                            butter_health -= dry
                        elif choose_pokemon == "Onix":
                            onix_health -= dry
                        elif choose_pokemon == "Geodude":
                            geo_health -= dry
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= dry
                        elif choose_pokemon == "Staryu":
                            star_health -= dry
                        elif choose_pokemon == "Magikarp":
                            magik_health -= dry
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= dry
                    else:
                        print("Articuno used Freeze-Dry but he missed!")
                elif legendary_attack == 3:
                    hit_chance = random.randint(1, 100)
                    shard = random.randint(20, 25)
                    if hit_chance <= 90:
                        print(
                            f"Articuno used Ice Shard and dealt {shard} to {choose_pokemon}!"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= shard
                        elif choose_pokemon == "Charmander":
                            charm_health -= shard
                        elif choose_pokemon == "Butterfree":
                            butter_health -= shard
                        elif choose_pokemon == "Onix":
                            onix_health -= shard
                        elif choose_pokemon == "Geodude":
                            geo_health -= shard
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= shard
                        elif choose_pokemon == "Staryu":
                            star_health -= shard
                        elif choose_pokemon == "Magikarp":
                            magik_health -= shard
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= shard
                    else:
                        print("Articuno used Ice Shard but he missed!")
                elif legendary_attack == 4:
                    hit_chance = random.randint(1, 100)
                    beam1 = random.randint(30, 35)
                    if hit_chance <= 85:
                        print(
                            f"Articuno used Ice Beam and dealt {beam1} to {choose_pokemon}"
                        )
                        if choose_pokemon == "Pikachu":
                            pikachu_health -= beam1
                        elif choose_pokemon == "Charmander":
                            charm_health -= beam1
                        elif choose_pokemon == "Butterfree":
                            butter_health -= beam1
                        elif choose_pokemon == "Onix":
                            onix_health -= beam1
                        elif choose_pokemon == "Geodude":
                            geo_health -= beam1
                        elif choose_pokemon == "Bulbasaur":
                            bulb_health -= beam1
                        elif choose_pokemon == "Staryu":
                            star_health -= beam1
                        elif choose_pokemon == "Magikarp":
                            magik_health -= beam1
                        elif choose_pokemon == "Squirtle":
                            squirt_health -= beam1
                    else:
                        print("Articuno used Ice Beam but he missed!")
