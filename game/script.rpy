# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Erika", image="mock-mc2")


# NVL characters are used for the phone texting
define n_nvl = Character("Jonathan", kind=nvl, callback=Phone_ReceiveSound)
define e_nvl = Character("Erika", kind=nvl, image="mock-mc2", callback=Phone_SendSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

init: 
    $ left = Position(xpos= -0.148, ypos=1.2, xanchor='left')
    $ right = Position(xpos=1.0, xanchor='right')
    $ uppercenter = Position(xpos= 0.5, ypos=0.9, xanchor='center')
    $ uppercenter2 = Position(xpos= 0.5, ypos=0.55, xanchor='center')
    $ uppercenter3 = Position(xpos= 0.5, ypos=0.65, xanchor='center')


    $ center = Position()


    $ fade = Fade(.5, 0, .5) # Fade to black and back.
    $ dissolve = Dissolve(0.5)

    image duskcity = im.Scale("bg city dusk.png", 1920, 1080)
    image backalley = im.Scale("bg back alley.png", 1920, 1080)
    image black = Solid((0, 0, 0, 255))

    #define e = Character("Erika")
    image erika serious= Image("mock-mc2.png")
    image erika happy = Image("mock-mc1.png")

    image elf sitting= Image("poor-elf-boy.png")
    image elf standing= Image("mock-elf.png")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene duskcity
    play music "Late Night Radio.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show erika serious at left
    
    # These display lines of dialogue.
    e "Another day in bustling Midcity. You'd never guess the stories this place hides, just by walking with the crowds."


    show erika happy at left
    e "Though, I suppose ignorance is preferable when it comes to all those secrets hiding in plain sight..."
    "I feel a faint vibration from the device wrapped on my wrist. I check it, and I can't help but chuckle a little under my breath."
    e "Straight to the deep end on my first day, huh?"

    nvl_narrator "Volatile magical frequencies have been detected in the area. Immediate intervention required."
    n_nvl "Hey! New blood! Hear that?"
    n_nvl "You are the closest to this mess, so you have to go over there first."
    e_nvl "Wonderful, my luck is quite something, is it not?"
    n_nvl "Yep, get to see the rough stuff up close."
    n_nvl "Try not to do anything too rash, rest of us are coming to the area ASAP."
    e_nvl "Sure thing chief, will keep any threats under control. {image=EileenSelfieSmall.png}"

    show erika serious at left
    "The device flashes with alerts about a nearby discrepancy."
    e "Let's see now, wild magical fluctuations, dreadfully close to the open street."
    e "Perfect recipe for a low to medium level exposure hazard."


    show erika happy at left
    e "Haa, as if my first time visiting the sanctuary wasn't enough to handle..."
    e "Well, no time for dawdling."


    show erika serious at left
    "I use the device to patch into M.O.N.D command"
    e "Operative Erika here. I've detected unusual magical interferences in district 1-O5. All details have been sent. May I proceed with investigations?"
    "..."


    show erika happy at left
    "Affirmative."
    e "Understood."


    stop music fadeout 3.0
    scene black with fade
    "I make haste towards the source of the anomaly, taking a few corners through the busy streets."
    "Steadily I close the distance between me and whatever, or whoever caused it."
    

    
    scene backalley with fade
    #play music "Grand Dark Waltz Trio Vivace.mp3" fadein 1.0
    play music "Waltz Primordial .mp3" fadein 1.0

    show erika happy at left with dissolve
    e "What a quaint back alley. I was worried I would have had to deal with a public incident for a moment."

    show erika serious at left
    e "This seems more of a private affair, however."
    "I activate my coat's invisibility feature. Nothing much changes from my point of view, but it should make me undetectable for a while."

    show erika happy at left
    e "Handy when you'd rather see what's going on before being seen yourself. Or ambushed, or struck by a stray spell."

    show erika serious at left
    e "Now then."

    "With steady steps, I advance into the alley."
    "The sound of laboured breathing is the first thing I notice. I survey my surroundings once again."

    show elf sitting at uppercenter
    "Pitted against a wall, there is a desperate looking figure."
    "An elf hybrid by the looks of it, already transformed. Clearly affected by that red orb he is clutching to his chest. "

    "Not an ancestry particularly difficult to deal with, no. That artefact he is holding is the problem here."
    "He could either be in grave danger, or pose it."
    

    show erika happy at left
    "Still, given that it's an elf, I suppose this coat is useless."
    "I notice the elf glance at me warily, desperation in his eyes. Of course he sees me, nothing can get past those senses."
    "I deactivate my invisibility cloak. This startles him even more."
    "His breathing grows quicker and sharper, the shadows in the alley stretching and twisting as if reacting to his distress."
    "Elf" "Damn this all..."
    hide elf sitting with dissolve
    "No need for things to escalate, but if his mind is in a dark place, this could get ugly fast. I should handle this with care."

    menu:
        "Warn to stay down":
            show erika serious at left
            e "I wouldn't make any sudden moves if I were you."
            "I slowly reveal the badge I've been clutching, its insignia clearly marking me as an operative of the Magical Oversight and Neutralization Department."
            e "Just a formality, but an important one. You know what this badge represents. Stand down and release the artefact. It's causing a disturbance far too close to human eyes."
            e "On MOND authority, I need you to cease all magical activity and comply with our standard procedures. It's for your safety as much as theirs."

        "Calm and reassure":
            show erika serious at left
            e "Easy now, I'm not here to hurt you. But let's avoid any rash moves, alright?"
            "I carefully pull the badge from my coat's pocket, showing my position as an operative of the Magical Oversight and Neutralization Department."
            e "All supernaturals should recognize this badge, this is just standard procedure. Your magical activity pinged our radars."
            show erika happy at left
            e "Just let go of the artefact and follow my lead, you'll be fine."
    
    "I keep my voice low and steady, showing any hint of aggression could provoke him further."
    show erika serious at left
    "The importance of my role here is clear enough, though seeing it for the first time is unsettling."
    "That desperate look in his eyes, he feels cornered by my presence, much as he may be in an open alley."

    
    "Elf" "Damn it! DAMN HIM!"

    "He doesn't seem to process my words, his eyes darting around wildly as he slowly gets to his feet, still holding onto that glowing red orb."
    e "Stand down."
    show elf-eyes at uppercenter2 with dissolve
    "I command, hoping to snap him back to reality, but it's like he's lost in his own world, driven by whatever power that orb holds."
    
    
    show erika happy at left
    "He's not just trying to flee; something about that orb has him completely overwhelmed. I need to end this quickly, before anyone gets hurt."

    "As he suddenly dashes toward me, his movements betray his elven lineage—quick, but noticeably less fluid than typical of his kind."
    "He's trying to overpower me, or perhaps just desperate to escape. Either way, I can't let him get past me."
    hide elf-eyes at uppercenter2 with dissolve

    "I dodge his attempts to strike, though some do come a bit too close for comfort."
    show elf standing at center with dissolve
    show erika serious at left

    e "Enough of this."

    "Seizing a moment of his hesitation, I fire my weapon. A magic-suppressing net envelops him."
    "It flashes brightly for a momement, and then the glow fades along with all of his elven features. Leaving a very human-looking man caught and subdued."
    hide elf standing at right with dissolve


    e "If you keep struggling, you'll only hurt yourself. It's over."

    "He makes one last feeble attempt to get out of the net, but exhaustion wins over."
    "The fight drains from him as the net cuts off his connection to magic. "

    show orb at uppercenter3 with dissolve
    "The orb rolls away, clinking against the cold pavement."

    "Elf" "Please... I never meant for this..."

    hide orb at uppercenter3 with dissolve
    stop music fadeout 5.0
    
    "His voice is weak, filled with regret. I keep an eye on him, though he doesn't appear to be in fighting spirit any longer."
    "I contact M.O.N.D HQ to report the situation."
    e "Situation in sector 1-O5 is contained. Awaiting retrieval."

    play music "Late Night Radio.mp3" fadein 5.0
    show erika happy at left
    e "He is scared and shaken, should be safe though. Let's get him some help."

    "Scene is secure and clean up is on the way. I get to breathe again."
    "I can't help but glance at the red artefact on the pavement. Wouldn't dare touch it without proper equipment."
    "I doubt I'll ever find out what the deal is with it, that is for those higher on the clearance ladder to know."

    show erika serious at left
    "My elven target appears in good shape, all things considered. A few bruises from getting tangled in the net, but nothing critical."
    "Who knows what might have happened to him if the anomaly had gone unchecked."
    "It doesn't take long for the others to arrive, and for the situation to be taken off my hands."
    "It's getting late, my first shift at the sanctuary should have already begun."

    show erika happy at left
    "No rest for the wicked."

    scene black with fade
    "I watch as the elf is inspected by the medical staff and transferred to their vehicle. He should be in good hands."
    "I'll take that as my cue to leave. Hopefully, the rest of the night will go smoother at The Spirit's Cup."


    # This ends the game.

    return
