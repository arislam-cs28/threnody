import time
import random
import var_storage as vts
import questionary

def char_print(stringy):
    for ch in stringy:
        print(ch, end="", flush=True)
        time.sleep(random.uniform(0.05,0.15))
    print()
    time.sleep(1)

def one_choice1(): # the WHAT ARE YOU DOING HERE? choice
    vts.emotion["harsh"] += 1
    char_print("Muriel cocked her head, stepping forward languidly, her typical avant-garde dress swapped for a black embroidered coat that looked" \
    " just like Mirai's casket's pall.")
    char_print("\"You forget Mirai's my sister too, no?\" She took another step forward, her fan hitting the underside of my chin. \"Where else would I be if not here?" \
    " I'm more surprised you attended, considering the fact that Mirai wanted nothing to do with you.\"")
    char_print("I grimaced. It had been thirteen weeks since Mirai and I's last interaction, where she left the annual gala at Drijkhart screaming that I was a blithering fool." \
    " \033[3mCoward,\033[0m she cried violently. \033[3mYou'd let a child, a family, anyone die just to save your own fucking skin.\033[0m" \
    " She wasn't particularly wrong, but the knights of Drijkhart did have to hold her back from swinging her heels at my neck.")
    char_print("\"Why bring that up now? She's gone, Muriel. Telling me this changes nothing.")
    char_print("Muriel just stared, her fan leaving my face as she grimaced. \"Forgive me. Her death is still fresh.\"")
    char_print("I paced side to side, my fingers scratching at the cigarette body in my pocket.")
    char_print("\"The children still ask where you went. Mirai told them you were dead in a ditch.\"")
    char_print("I frowned deeper.")

def one_choice2(): # the NO NEED TO REMIND ME choice
    vts.emotion["harsh"] += 2
    print("")

def beginning():
    char_print("""\033[3mThe lost, the lost he cannot restore,
And, looking over the hills, I mourn
The darling who shall not return.\033[0m""")
    char_print("                    - \"Threnody,\" Ralph Waldo Everson")
    char_print("---")
    char_print("On the thirteenth night of November, Mirai Leytmer commissioned a coffin.")
    char_print("A week later, the Queen’s Legion of Drijkhart buried Ulschadt’s most beloved singer in a half-carved casket, " \
    "the sound of wood-grain scraping against wood-grain mimicking the rasp of her voice as they threw it into the dirt.")
    char_print("While the rain pelted us in the crowd, wailing filling the ceremony, I half expected Mirai to raise from the dead just to laugh in our faces.")
    char_print("She would tell us off as fools for not singing on the occasion.")
    char_print("Yes, indeed, she would be as horrible as ever. I could feel the ghost of her voice against my ear.")
    char_print("The mob of mourners continued to grow despite the ever increasing torrent. At one point, I was sure Ulschadt's Queen had come by but the endless" \
    " drivel of the night and the frequenting of reporters and parasocial fans and family and friends and everyone in the Capital had " \
    "thrown my head into a faint buzz.")
    char_print("The most I could do was to tell the funeral band to stop playing classical piano and worse, Lyubon; Mirai would have my head in heaven for that.")
    char_print("But Mirai Leytmer was dead, and buried in a half-carved coffin, and would never reawaken because there is no mercy for the good.")
    char_print("Ulschadt would not get her best spy back.")
    char_print("")
    char_print("It took two days and 14 hours for the people to die down from the initial ceremony.")
    char_print("In the meantime, I amongst the rest of the funeral procession had resided in the Greenwich House. The fear of facing Mirai's family again had left me " \
    "shut inside, but I eventually decided that I should leave for a cigarette break.")
    char_print("I stepped outside.")
    char_print(f"\"You look like shit, {vts.player_name},\" came a voice from the other side of the hall. Leaned against the doorframe of suite 503 was Muriel, second sister to Mirai.")

    actions = {
        "\"What are you doing here?\"" : one_choice1,
        "\"No need to remind me.\"" : one_choice2,
    }

    choice = questionary.select("\"Muriel.\" I paused, staggering in my tracks. \"I...\"", choices=list(actions.keys())).ask()

    if choice:
        actions[choice]()



beginning()