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

define frog = Character("Frogrin", who_color="#22ee22")

label ch03_start:
    scene black with dissolve
    jump ch03_villain_intro

label ch03_villain_intro:
    scene black
    v "I hope by now you've heard that the naga troopers have failed as well. I pray that your plan meets with more success, Frogrin."

    frog "Of course mistress Vivienne. *Ribbit* Unlike my predecessors, I will begin taking over the humans where the Justiciar's prying eyes won't find me."
    frog "I have setup my operation in a rural lake town. As I begin to kidnap and convert the locals, no one will notice. Eventually, I will have my own private army to move into more populated areas."

    v "Another slow-burn plan, but indeed, it seems like it will work. Then go, my beautiful damp servant, and make the Dark Sisterhood proud!"
    jump ch03_lake_start

label ch03_lake_start:
    scene black
