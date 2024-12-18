﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main characters
define c = Character("Chisato", who_color="#8D7077")
define h = Character("Hazel", who_color="#0000ff")
define k = Character("Kaede", who_color="#F187BA")
define m = Character("Maika", who_color="#ee3333")
define s = Character("Sumire", who_color="#0fb20f")
define v = Character("Vivienne", who_color="#880088")
define y = Character("Yukino", who_color="#eeee00")
define z = Character("Zoe", who_color="#bbbbbb")

# colors
image white = "#ffffff"

# A smooth dissolve over 2 seconds
define dissolve_2 = Dissolve(2)

# The game starts here.

label start:

    jump intro

label intro:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene white

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show intro all bg
    "This is the story of the Justiciar Sentai. An international group of women devoted to maintaining peace and justice."

    show h intro
    "Hazel, the scientist. Eldest of the Justiciars, she is in charge of the technology used by the team."
    show z intro
    "Zoe, the tactician. Zoe comes from a prestigious military family, and applies that knowledge to keep missions running smoothly."
    show y intro
    "Yukino, the fighter. Powerful, energetic, and a mite brash. Yukino knows how to get a mission done, no matter what."
    show k intro
    "Kaede, the caretaker. The medic of the group, Kaede keeps the group's morale high no matter the situation."
    show s intro
    "Sumire, the idol. Sumire is responsible for the public image of the Justiciars and acts as a moral compass for the group."
    show m intro
    "Maika, the leader. With a feeling of deep responsibility, Maika takes charge of any situation, leading her Justiciars into danger, but always back home again."

    scene white
    "The Justiciars protect Earth from the villainous Dark Sisterhood, led by the witch Vivienne."

    jump ch01_start

    return
