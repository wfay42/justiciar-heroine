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

label ch03_start:
    scene black with dissolve
    jump ch03_villain_intro

label ch03_villain_intro:
    scene black
    v "I hope by now you've heard that the naga troopers have failed as well. I pray that your plan meets with more success, Frogra."

    frog "Of course mistress Vivienne. *Ribbit* Unlike my predecessors, I will begin taking over the humans where the Justiciar's prying eyes won't find me."
    frog "I have setup my operation in a rural lake town. As I begin to kidnap and convert the locals, no one will notice. Eventually, I will have my own private army to move into more populated areas."

    v "Another slow-burn plan, but indeed, it seems like it will work. Then go, my beautiful damp servant, and make the Dark Sisterhood proud!"
    jump ch03_hotspring_villain_appears

label ch03_lake_start:
    scene black

label ch03_hotspring_villain_appears:
    scene frog mx 01
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

