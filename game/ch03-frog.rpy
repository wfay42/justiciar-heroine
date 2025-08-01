# Characters and other variables are defined in script.py

"""
Chapter 03: Frog
Frogrin can eat people, and her belly expands. Slowly dissolves their clothes.
She can eventaully lay them in eggs to hatch them into more frog monsters.
Hazel is the hero of this episode.
Maika eaten first.
Then Sumire and Zoe.
Then Kaede and Yukino.
Chisato sacrifices herself so Hazel can solve the problem.
Maybe Hazel lets herself get eaten with some kind of thing that gives indigestion.
"""

define frog = Character("Frogra", who_color="#22ee22")
define mina = Character("Minako", who_color="#444444")

$ frogZoeJoins = False

label ch03_start:
    scene black with dissolve
    jump ch03_villain_intro

label ch03_villain_intro:
    scene frog v 01
    v "I hope by now you've heard that the naga troopers have failed as well. I pray that your plan meets with more success, Frogra."

    show frog v 02
    frog "Of course mistress Vivienne. *Ribbit* Unlike my predecessors, I will begin taking over the humans where the Justiciar's prying eyes won't find me."
    frog "I have setup my operation in a rural lake town. As I begin to kidnap and convert the locals, no one will notice. Eventually, I will have my own private army to move into more populated areas."

    show frog v 03
    v "Another slow-burn plan, but indeed, it seems like it will work. Then go, my beautiful damp servant, and make the Dark Sisterhood proud!"
    jump ch03_hotspring_start

label ch03_hotspring_start:
    scene frog 01 01
    k "So you've never been to a Japanese hot spring, Zoe?"
    z "Can't say that I have. I've been so busy with Justiciar stuff I never found the time after moving here."
    m "Well, you're going to love it. It's something truly special you can't get anywhere else in world."
    y "Yup, nowhere else. Except Austria, Costa Rica, Italy, Iceland, Chile, Canada..."
    m "Shush! It's special!"

    show frog 01 02
    mina "Hello and welcome to the Yakitori hot springs. How many are you checking in?"
    h "Five. Reservation is under Justiciar Industries."

    show frog 01 03
    k "Oh yeah, it's a shame Chisato and Sumire couldn't come. They would have loved it."
    m "Well, someone had to stay back at base in case anything urgent comes up. Chisato's the director, so that made sense, but I bet Sumire is devastated she drew the short straw."
    y "I bet. But there's nobody she can blame. It was all just the luck of the draw. No funny business was invovled at all."
    show frog 01 04
    m "Well, if that wasn't suspicious."

    show frog 01 02
    mina "Alright ladies, I was just about to prepare the hot spring for you, so feel free to relax for a few minutes until I open it up."

    show frog 01 05
    y "Great. Where's the room for me to strip in?"
    z "Strip? Oh, this is one of those hot springs where we go in... naked?"
    h "I know it sounds strange, but you get used to it. After I moved to Japan, it took a couple tries, but now it's as normal as taking a shower."
    h "If you're not sure you want to go, I'm happy to stick with you, Zoe. What do you say?"
    menu:
        "Muster your courage and go to the hot spring with the others":
            $ frogZoeJoins = True
            z "N... no. I can handle it! If I'm able to fight all those villains, the least I can do is get... nude.. in front of my coworkers?"
            h "That's the spirit!"
        "Value your privacy and hang out with Hazel":
            $ frogZoeJoins = False
            z "I... uh... let's hang out for a bit. Maybe I'll dip into the hot spring later."
            h "Sure, let's go for a walk around the resort."

    show frog 01 02
    mina "Great, please wait here while I prepare the hot spring."
    call ch03_CALL_hotspring_villain_appears from ch03_hotspring_start_call01
    if frogZoeJoins:
        jump ch03_zoe_joins
    else:
        jump ch03_zoe_skips

label ch03_CALL_hotspring_villain_appears:
    scene frog mx 00
    "Minako begins her work to prepare the spring for her new guests. She hears quiet, almost squishy, footsteps on the ground behind her as someone approaches."

    show frog mx 01
    frog "You must be the proprietor of this establishment. I believe I need your help with something."
    mina "Oh I'm sorry, but the hotspring isn't ready yet for service. You'll need to come back later, I'm afraid."
    frog "Unfortunately, I'm in quite a hurry."
    show frog mx 02
    "With that, Frogra unleashes her exceedingly long tongue, sticking it to Minako, and pulling her backwards into the monster's mouth."

    show frog mx 03
    "Frogra's belly distends slightly as Minako now lays panicked inside of her abdomen. Minako can't believe she fits inside the frog woman who stood behind her."
    show frog mx 04
    frog "Oh my, you were quite a large one, I was almost worried you wouldn't make it in. But shrinking magic is my specialty."
    show frog mx 05
    frog "Either way, it's time for you to join me. Become my daughter, if you will. You must know what I mean. You seem like a mother yourself."
    show frog mx 06 with dissolve_2
    frog "I can tell from that beautiful, plump body of yours. It's the body of a hard-working mother. Forever altered by child rearing."
    show frog mx 07a
    frog "But it will be of use again. Fertile again. You will help me do the same, bring more of our daughters into the world."
    window hide
    show frog mx 07b with dissolve_2
    pause
    show frog mx 07 with dissolve_2
    pause
    show frog mx 08
    window show
    frog "The eggs you bear within your body will be fertilized, and you shall feel satisfaction as a doting mother again."
    show frog mx 09 with dissolve_2
    frog "There. The change is complete. Don't you feel better now. Like you have purpose."
    show frog mx 10
    frog "Good. Are you ready to be reborn into this world? Part of something greater than yourself?"

    show frog mx 11
    "The transformation complete, Frogra births Minako, her new daughter, expelling her from her womb."
    frog "My perfect, beautiful daughter. Are you ready to begin?"
    show frog mx 12
    mina "Ribbit ribbit!"
    frog "Then let's get started!"
    return

label ch03_CALL_eggs_01:
    "Little do our heroines know, below the surface of the water lays something sinister."
    show frog 02 05
    "The transformed Minako lay at the bottom of the hot spring."
    show frog 02 06
    "Small frog eggs leak from her body, and begin floating around in the water. The stream of eggs seems endless."

    show frog 02 07a
    "The innocuous-looking eggs float up towards our heroines, lodging themselves in their clefts."
    return

label ch03_CALL_eggs_02_with_zoe:
    show frog 02 07b
    "One by one, they begin to embed in the warm bodies of the Justiciars."

    show frog 02 08a
    "The changes begin slowly, undetected by the heroines."
    window hide
    show frog 02 08b with dissolve_2
    pause
    window show
    "Unlike Minako's forceful transformation, this is far more subtle and insidious. The Justiciars don't even know to resist anything."

    show frog 02 09b
    "Before long, it is too late. By the time they notice their transformation, there is nothing they can do to reverse it."

    show frog 02 10
    frog "Oh ho ho, such beauties have joined my clan. Welcome, daughters."

    show frog 02 11a
    frog "Are you ready to begin your work to expand our family?"

    show frog 02 11b with dissolve_2
    m "Ribbit!"
    z "Ribbit!"
    return

label ch03_zoe_joins:
    scene frog 02 01
    h "See, isn't this the best, Zoe?"
    scene frog 02 02
    z "Y... yeah. Yup. Definitely. Relaxing. Loving this. Really."

    scene frog 02 03
    y "Heh, loosen up Zoe. After that whole naga thing we've all seen each other naked. There's no secrets here."
    m "Enough Yuki. Just let Zoe get into it on her own terms. Quit bugging her."
    y "Sure thing, I've got plenty more to bug you about, Maika."

    call ch03_CALL_eggs_01 from ch03_zoe_joins_call01
    call ch03_CALL_eggs_02_with_zoe from ch03_zoe_joins_call02

    show frog 02 11b with dissolve:
        matrixcolor SaturationMatrix(0)

    "Frog Bad End 1\nMaybe Zoe joining her comrades in the pool was a mistake."
    return

label ch03_zoe_skips:
    scene frog 02 03
    y "Yessssss. This is what I was looking for. It's a shame Zoe didn't want to come."
    m "It's fine. Give her some time and I'm sure she'll come around."
    k "That just means more hot spring for us, heehee."
    call ch03_CALL_eggs_01 from ch03_zoe_skips_call01

    scene frog 03 01
    z "I just love historic places like this. Makes me glad I moved to Japan for the Justiciars. Thanks for sticking with me."
    h "No problem. Those three are natives here, they're used to getting naked and having a soak."
    z "Hehe, yeah. Definitely takes some getting used to. I'm not sure I'm ready to take a dip, but maybe let's at least visit everyone else."
    h "Sure. I bet their faces have gotten all red and swollen from being in the hot spring."

    show frog 03 02a
    "Hazel and Zoe make their way to the hot spring, expecting to find their comrades, but surprisingly finding an empty pool."
    show frog 03 02b
    z "Huh. Maybe they left already?"

    show frog 03 03
    m "Ribbit!"
    h "Ack!"

    show frog 03 04a
    h "Get off me you..."
    show frog 03 04b
    h "*Gasp*! Maika!"
    show frog 03 04c
    m "Ribbit!"

    show frog 03 05
    z "Hyaa! Sorry Maika!"

    show frog 03 06
    z "Come on Hazel, we have to transform."
    h "Right!"

    show frog 03 07a
    window hide
    pause
    show frog 03 07b with dissolve_2
    pause
    show frog 03 08
    window show
    frog "Look who we have here. I didn't think I'd trap two as useful as you."
    z "Of course. The Dark Sisterhood. Transform our friends back, or you're going to pay!"
    frog "That's what I thought you'd say, but I'm afraid I have the upper hand."

    # shoots tongue out hitting Hazel
    show frog 03 09
    h "Ack! Zoe!"
    z "Hazel!"
    menu:
        "Grab onto Hazel to pull her back":
            jump ch03_zoe_goodend
        "Stay back, grabbing Hazel is too dangerous":
            jump ch03_zoe_badend01

label ch03_zoe_badend01:
    scene frog 05 01a
    "Knowing that Hazel is already lost, Zoe looks on in terror as she sees her comrade shrink and quickly get gulped down by the monster."
    show frog 05 01b with dissolve
    "Distracted by the predicament, she doesn't notice two more minions approach her from behind."
    show frog 05 01
    frog "Oh my. Not much of a team, are you? Can't even help your friend? Well, she's about to join a new team, aren't you dear?"
    show frog 05 02
    "Struggle as she might, Hazel is stuck inside the frog monster."
    show frog 05 03
    "She feels her body changing and her clothes dissolving. She lets out a slight yelp, but no sound can be heard outside the fluid sack."
    show frog 05 04
    "Hazel looks down, frightened, as she is almost completely transformed. Zoe can see Hazel's lips move, as if mouthing 'Help' one last time. Before Zoe can do anything..."
    show frog 05 05 with dissolve_2
    "Hazel completes her transformation into another frog minion. Another daughter of Frogra."

    show frog 05 06
    z "Hazel... I'm too late... But I have to figure out a plan. I have to."
    show frog 05 07
    z "Ack. Get... off of me you, *gasp*! Yukino! Kaede!"
    show frog 05 08
    z "You two have to snap out of it! Get off of me! I'm trying to save you!"
    show frog 05 09
    z "H... Hazel. Please, you have to hear me in there!"
    show frog 05 10
    "Hazel peered down at Zoe, prone on the ground, helpless. What was left of Hazel's mind only felt excited."
    show frog 05 13a
    "Hazel jumped onto Zoe's face, thrusting her vulva to touch Zoe's lips."
    show frog 05 13b with dissolve_2
    "Underneath, Hazel was releasing her eggs directly into Zoe's accepting mouth. Unable to do anything, Zoe could only look on in horror."
    show frog 05 13c
    "After swallowing the eggs, Zoe face stiffened. She could feel the changes happening inside of herself."
    show frog 05 13d with dissolve_2
    "Zoe's fate was sealed. It would only take moments for her to share the same fate as her friends. Her face and eyes began to mutate."
    show frog 05 13e with dissolve_2
    "Her facial features became entirely frog-like in a matter of seconds."
    show frog 05 13f with dissolve_2
    "Her sentai costume began to melt away, ready to show her new body."
    show frog 05 13g with dissolve_2
    "Zoe had joined her sisters. Another frog minion, ready to serve the Dark Sisterhood."
    show frog 05 14
    frog "Perfect. Now, it's time for us to get to work. Our guests aren't going to convert themselves."


    show frog 05 14 with dissolve:
        matrixcolor SaturationMatrix(0)

    "Frog Bad End 2\nZoe abandons Hazel, and pays the price."
    return

label ch03_zoe_goodend:
    scene frog 04 01
    z "I've... I've got you... Hazel..."
    z "Ahhh! No!"
    show frog 04 03
    frog "Ha ha ha. You should have known it would end this way. I'm afraid I'm too strong for the two of you."
    frog "Now, I believe it's time for you to join us as well. We just need a little bit more time for you to gestate."
    show frog 04 05
    z "OK, we have to think fast. Any ideas?"
    h "Well it's clearly pretty cramped in here. Think we can blow her up from the inside?"
    z "It's worth a shot!"
    show frog 04 06
    "Zoe and Hazel push against each other has hard as they can, trying to extend the belly of the frog monster."
    show frog 04 06a
    frog "Hey, what are you two doing down there! Ow!"
    show frog 04 06
    h "Just... a little... more..."
    frog "No! Stop!"
    show frog 04 07
    "With one last push, Zoe and Hazel burst out of the stomach of Frogra, destroying her and ending her curse."
    show frog 04 08
    z "Wow. That was one hell of a longshot."
    h "Yeah, but I'm glad it worked! And it's all because you came after me. You really are a good friend Zoe."
    z "Thanks. I know you would've done the same."
    show frog 04 09
    z "And look. The rest of our friends are back to being their normal selves."
    h "And still naked. Heh."
    h "Well, what do you think? Want to take a dip in the hot spring?"
    show frog 04 10
    z "Not a freaking chance."

    show frog 04 10 with dissolve:
        matrixcolor SaturationMatrix(0)
    "End of Chapter 3."

    call screen confirm("Do you want to save?", yes_action=[ShowMenu('save'), Return()], no_action=Return())
    jump ch04_start

