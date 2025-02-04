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
    scene black
    v "I hope by now you've heard that the naga troopers have failed as well. I pray that your plan meets with more success, Frogra."

    frog "Of course mistress Vivienne. *Ribbit* Unlike my predecessors, I will begin taking over the humans where the Justiciar's prying eyes won't find me."
    frog "I have setup my operation in a rural lake town. As I begin to kidnap and convert the locals, no one will notice. Eventually, I will have my own private army to move into more populated areas."

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
    z "I just love historic places like this. Makes me glad I moved to Japan for the Justiciars. Thanks for hanging out with me."
    h "No problem. Those three are natives here, they're used to getting naked and having a soak."
    z "Hehe, yeah. Definitely takes some getting used to. I'm not sure I'm ready to take a dip, but maybe let's at least visit everyone else."
    h "Sure, we'll see if their faces have gotten red from all the heat."

    show frog 03 02
    "Hazel and Zoe make their way to the hot spring, expecting to find their comrades."
    z "Huh. Maybe they left already?"

    show frog 03 03
    m "Ribbit!"



