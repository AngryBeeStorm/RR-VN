# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Erika")
define f = Character("Felix")
define j = Character("Johan")
define t = Character("Tian")


# NVL characters are used for the phone texting
#define n_nvl = Character("Jonathan", kind=nvl, callback=Phone_ReceiveSound)
#define e_nvl = Character("Erika", kind=nvl, image="mock-mc2", callback=Phone_SendSound)

#define config.adv_nvl_transition = None
#define config.nvl_adv_transition = Dissolve(0.3)

init: 
    $ bottom_left = Position(xpos= -0.03, ypos=1.35, xanchor='left')
    $ left = Position(xpos=0.2, xanchor='left')
    $ right = Position(xpos=0.9, xanchor='right')
    $ uppercenter = Position(xpos= 0.5, ypos=0.9, xanchor='center')
    $ uppercenter2 = Position(xpos= 0.5, ypos=0.55, xanchor='center')
    $ uppercenter3 = Position(xpos= 0.5, ypos=0.65, xanchor='center')
    $ offscreen_right = Position(xpos=2, xanchor='right')
    $ other_center = Position(xpos= 0.5, ypos=1.0, xanchor='center')

    $ center = Position()


    $ fade = Fade(.5, 0, .5) # Fade to black and back.
    $ dissolve = Dissolve(0.5)

    image duskcity = im.Scale("bg city dusk.png", 1920, 1080)
    image backalley = im.Scale("bg back alley.png", 1920, 1080)
    image black = Solid((0, 0, 0, 255))
    image bedroom = im.Scale("Ai_placeholders/Ai_backgrounds/mc_bedroom1.png", 1920, 1080)
    image street = im.Scale("Ai_placeholders/Ai_backgrounds/street2_day.png", 1920, 1080)
    image tavern = im.Scale("Ai_placeholders/Ai_backgrounds/tavern2.png", 1920, 1080)
    image office = im.Scale("Ai_placeholders/Ai_backgrounds/tian_office.png", 1920, 1080)
    image company = im.Scale("Ai_placeholders/Ai_backgrounds/tian_company1.png", 1920, 1080)
    image flower_saloon_int = im.Scale("Ai_placeholders/Ai_backgrounds/flower_saloon_interior.png", 1920, 1080)
    image flower_saloon_ext = im.Scale("Ai_placeholders/Ai_backgrounds/flower_saloon_exterior.png", 1920, 1080)

    #define e = Character("Erika")
    image erika default= Image("placeholders/erika default.png")
    #image erika default= im.Scale("placeholders/erika default.png", 627, 1317)

    image felix default= Image("placeholders/felix default.png")
    #image felix default= im.Scale("placeholders/felix default.png")#, 336, 782)

    image johan default= Image("placeholders/johan default.png")
    #image johan default= im.Scale("placeholders/johan default.png")#, 442, 824)

    image tian default= Image("placeholders/tian default.png")
    #image tian default= im.Scale("placeholders/tian default.png")#, 465, 958)

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,time,child,add_sizes=True,**properties)

        Shake = renpy.curry(_Shake)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bedroom with fade
    play music "Late Night Radio.mp3"
    "FIRST SCENE - CLEANING GUN"
    show erika default at left with dissolve
    "I take my gun from the safe and start cleaning out the barrel."
    e "Right, can't let you get too dusty now."
    e "Much as I hope you won't get much use."

    "Using a gun as a pet rock to listen to all your woes is preferable to using it as a weapon, no?"
    e "A new home, new city, and our first real day on the job."
    e "Hmm, first night on the job is probably more appropriate. All I have to do this morning is to run an errand."
    e "Shouldn't be too difficult, considering I'm still a rookie. Hope the higher ups have mercy."

    "I finish cleaning the barrel and making sure everything is in working order."

    e "Still, can't risk going at it unprepared."
    e "Well, it's about time I got going."
    "Before leaving the still unfamilliar apartment, I take the containment suitcase. Important, for this kind of errand."

    scene black with fade
    "Let's see now..."
    "What an interesting meeting spot."

    scene flower_saloon_ext with fade
    
    show erika default at center with dissolve
    

    # These display lines of dialogue.
    "MEETING WITH JOHAN"
    e "Collecting artifacts from a flower salon… I sure hope it won't be something big, alive or, gods forbid, sentient. I hate sentient artifacts."
    e "Not you, Maggie, you're a treat."
    e "I can't really see the lights, I wonder if they're even open this early."

    scene flower_saloon_int with fade
    
    show erika default at bottom_left with dissolve
    show johan default at offscreenright
    e "Anyone here? Hello?"
    "?" "Coming! Ouch! Fuck! Who the fuck put that here!"
    "Yeah, that definitely sounds like a professional MOND informant."
    
    show johan default at other_center with move
    j "Hi, what brings you here today?"

    menu:
        "Show MOND ID":
            jump artifact_transaction
        "I'm here to collect something, I'm sure you must have been warned":
            j "I don't really think I understand you."
            menu:
                "Show MOND ID":
                    jump artifact_transaction

 
    

label artifact_transaction:

    j "Oh, right, MOND… I'll be right back."

    "Will he run away? He doesn't look the part but better safe than sorry."
    menu:
        "Ok, if you make it in five minutes":
            j "It will take much less, you won't even get bored!"
        "I think I'd rather come with you":
            j "I'm sorry, officer, but I can't let you in the back rooms"
            menu:
                "Ok, if you make it in five minutes":
                    j "It will take much less, you won't even get bored!"
    
    show johan default at offscreenright with move

    "Feels like an opportunity to take a look around anyway. "
    "Everything seems fairly normal for a flower shop, but still…"

    menu:
        "come to the lotuses in a small pond":
            e "Even the flowers aren't really magical."
        "come to the potted flowers":
            e "Even the flowers aren't really magical."

    show johan default at other_center with move
    j "Here, be careful with this thing."
    "He hands me a strange mechanical orb, shinig slightly with a magical glow."
    j "Should be a grade A artefact, I wouldn't want to carry that thing around for too long."
    e "Right, I'll deliver it as soon as I am able."
    "I open up my suitcase and seal it inside."
    "Whatever weird properties it may have it won't attract too much attention while in there."
    j "Well then, MOND cub. Take care out there!"
    "He waves me goodbye as I exit the flower shop."



label felix_runin:
    scene street with fade
    show erika default at bottom_left with dissolve
    "RUN IN WITH FELIX"
    

    "The street is bustling already, all these people going along their ways."
    "Eager to meet their destinations, I'm sure. Just like me."
    "Heh, this potato is just too hot to hold. I'm not exactly a fan of handling unknown artifacts."
    "... This will take some time… i should think about something on the way" 

    menu:
        "Think about artifact":
            "Hmm, I wonder what makes this artefact so special."
            "Artifacts in general are fairly rare, all things considered, so it's not a surprise that they should be handled with care."
            "But still, a covert delivery to artifact traders?"
            "That information is far above my paygrade, I'm sure."
            "Even then..."
        "Think about Jonathan":
            "That informant sure was interesting."
            "Covert operative running a flower shop, what a fun job he must have."
            "Seemed friendly enough, but something felt off about that smile of his."
            "Hmm, I wonder..."
    
    "!!!"

    show felix default at center with dissolve
    "...?!"

    f "Excuse me! Sorry, Sorry!"
    "That didn't feel like just a bump, this girl pushed herself into me. Was she trying to throw off my balance?"
    f "{size=20}...damn, sturdy on your feet.{/size}"
    e "Are you alright?"
    f "Ah hah, I should ask you that. Didn't mean for that to happen!"
    "Right, of course she..."
    "No, she, also had no intention of prying the suitcase out of my hands. Yet there it is."
    "I grab the girl by the wrist, can't have her getting away so easily."
    f "Wow! You saw me coming from a mile away, didn't you officer? I can see You're not just any newbie. "
    f "And you have such strong hands!"
    f "...Well, I'm at your mercy now; arrest me officer."
    "Right, what to do with this one?"
    menu:
        "Question him":
            e "I ask a question"
            f "And I answer the question in a vague way, hinting at the fact that I know more than I let on."
            e "cool"
            "He frees himself from my grip."
        "Flirt back":
            e "flirt flirt"
            f "flirt flirt flirt"
            e "shocked"
            "He frees himself from my grip."
        "Let him go":
            "He hardly did anything, to be fair. I let him go."
    show felix default at right with move

    f "I must say, you have a very nice grip, ma'am but you are not getting rid of me that easily!"

    menu:
        "Arrest him":
                "..."
        "Peg him":
                "..."
        "Hug him":
                "..."

    f "B-Before you do anything, officer, you can't arrest me; i didn't do anything!" 
    f "Plus you can't just arrive at your superiors with just any random guy, can you?"

    "Is she- i mean is he a guy?"

    f "You're letting me go, right? It was nice talking to you lady officer, maybe you'll catch me next time… i wouldn't mind to be grabbed by those big and strong arms of yours again."
    f "So uh… could you turn away so it looks like I disappeared? It'd be cool"
    e "..."
    f "No? then I'll just… ill just walk over there… bye"
    show felix default at offscreenleft with move
    "..."
    "Not an entirely smooth operation after all."
    "Something tells me an attempt like that isn't exactly the work of the underworld. "
    "Let's leave it like that for now. I want this thing off my hands, pronto. "
    scene black with fade
    "I walk over to the drop location, maintaining a strong grip on the suitcase."


label tian_meeting:
    scene company with fade
    show erika default at center with dissolve
    "MEETING WITH TIAN"

    "Ah, Gilded Globe Ventures. They're a big enough player in the exportation game."
    "They are also deep into the supernatural. Best artifact handlers around, with an ancestry to boot. "
    "I step into the tall glass building and a well dressed guard escorts me to my contact's office. "
    scene office with fade
    show erika default at bottom_left with dissolve
    "I open the door and find him - Tian Nirvay - standing at his desk, seemingly unperturbed, sipping coffee out of a plain mug among piles of organized paperwork."
    show tian default at center with dissolve
    "The artifact's final destination, as far as I'm concerned."
    
    menu: 
        "Your order is here, fresh out the oven!":
            t "{size=20}Heh{/size}"
            t "Ahem. Good."
        "The artifact has been delivered as per instructions.":
            t "I see. Good."
    
    t "...I take it the extraction operation went smoothly, then?"

    menu:
        "Brought it here in one piece, yes.":
            t "Good. I would like to inspect it and ensure that it is indeed what we were expecting."

        "There was one tinsy tiny incident.":
            t "...and this incident entailed what exactly?"
            menu:
                "Nothing worth reporting":
                    t "I certainly hope you are fit to ascertain the risks posed by even the smallest incident in our world."
                    t "Nonetheless, I would like to inspect the artifact to make sure it is what we were expecting."
                "An unsuccessful theft":
                    t "If the artifact is still in your possession, I can assume the attempt wasn't made by any of the top players."
                    t "...could just be a cat at play."
                    t "In any case, I must examine it and ensure that it hasn't been damaged or forged."
    
    e "Right, right. Here you go."
    "I bring the suitcase over to his desk and unlock the sealing mechanism."
    e "Anything amiss?"
    "He takes the mechanical ball into his hands and starts fiddling with it. Likely using that ancestry of his."
    t "Everything appears to be in order."
    t "We can ensure its safekeeping now that it has been entrusted to us."

    menu: 
        "Right, that's my job done":
            "I take my leave from the office full of paperwork, stealing one last glance at the artefact handler."
        "Need MOND for anything else?":
            t "Rest assured, we have access to official channels to contact you if need be."
            t "...though frankly, I doubt further involvement would serve either of us well."
            e "Far be it from me to change the plans of the higher ups."
            t "Of course. Well then, your business here is done."
            "I nod a brief goodbye and leave the office full of paperwork."
    
    scene street with fade
    show erika default at center with dissolve

    "Hmm, what an unnaturally professional interaction."
    "Well, that's it for this morning. I have the rest of my day free before my real job starts."
        
    
    "THE END"



    # This ends the game.

    return
