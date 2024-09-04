# Characters and other variables are defined in script.rpy

"""
Chapter 02: Atsugessho
Sumire gets entangled in new makeup, which is really Atsugessho
"""

define atsu = Character("Amane", who_color="#aaaaaa")

label ch02_start:
    jump ch02_at_salon

label ch02_at_salon:
    scene bg hq
    "After a successful mission, the Justiciars are relaxing."

    show s unsure
    s "That last fight was bonkers!"

    show s casual excited
    s "I'm off to do some retail therapy, see you all later!"

    scene bg street
    show s atsu 01
    atsu "Hello young miss, would you be interested in a free sample?"
    s "Ooh, free sample of what?"
    atsu "Our latest perfume, Eau de Atsu."
    show s atsu 02
    s "Sure thing!"

    show s atsu 03
    "The clerk gives a heavy spritz of the perfume to Sumire. Sumire takes in a deep breath enjoying its flowery scent."

    show s atsu 04
    atsu "How do you like it? Most patrons find it... enchanting. If you like that, please follow me into the salon for more samples."
    s "There's more free stuff! I mean, err, yes, I do like it. I'd love to see more."

    scene bg salon
    "Sumire is escorted into the salon by the clerk. The smell of the perfume is found throughout the store, although a bit stronger."
    show s atsu 05
    atsu "Please, have a seat in the chair."

    menu:
        "Sit in the chair":
            show s atsu 06 yes
            "Sumire sits in the chair willingly, excited to see what the beautician will do."

        "Refuse":
            s "Oh, I'm not sure I have enough time for a full routine like this."
            atsu "Please, I insist."
            show s atsu 06 no
            "Before she knows it, the beautician puts her hands on Sumire's shoulders, forcing Sumire down into the chair."
    show s atsu 07
    "The chair is extremely soft. Without much thought, Sumire begins to completely relax every muscle in her body. She barely notices the beautician begin working."
    show s atsu 08
    atsu "What a beautiful specimen. But there is so much more we can do. We need to thin out those eyebrows, add a bold wingtip, some mascara will do."
    atsu "And of course a beautiful lipstick and some matching eye shadow. I can see you love green, so of course we'll have to match that."

    "Sumire barely acknowledges what is being said to her. The combination of the chair and the smell of the perfume within the salon have rendered her into a state of nirvana."
    show s atsu 09
    "The beautician begins work immediately. Sumire sees every step of the process. She remains completely still. An ideal customer."
    atsu "(Thinking) Ha, this was too easy! This young woman will provide our kingdom with so much life energy!"
    "Sumire doesn't even notice nearly half an hour of time passes while she is being dilligently worked on."

    show s atsu 10
    atsu "Alright miss, all done! What do you think?"

    hide s atsu 10
    "Sumire leans forward as the beautician raises a mirror to her face."

    show s atsu 11 with dissolve_2
    "Sumire sees herself, changed by the process she has undergone, completely delighted by what she sees."
    "A slight smile plastered on her face, as it has been during the entire procedure."
    "Under the spell of the salon, Sumire is unable to see how the color of her skin has been completely drained, and her pupils have been replaced by hearts."
    show s atsu 12
    s "It's beautiful! You've done such an amazing job? How can I thank you?"
    atsu "Please tell all of your friends about this place! And of course, come back any time!"

    show s atsu 13
    atsu "In fact, we're still hiring. Would a beautiful young lady like yourself be interested?"
    s "Oh, I already have a full-time job."
    "Sumire's heart begins to beat a little faster with the thought of getting to apply makeup on customers just as the beautician had done to her."
    "Part of her tries to leave the salon without another word, but she just can't bring herself to do it."
    s "But I do have time off on the weekends! I'll be here tomorrow, that's normally my day off."

    show s atsu 14
    atsu "I very much look forward to it."
    "Sumire walks out of the store. She can't believe she said that, but she feels so excited to return the next day that she doesn't care."

    show s atsu 15
    atsu "A perfect specimen indeed. She will be a crucial component of the plan."

    jump ch02_saturday_street

label ch02_saturday_street:
    scene bg street
    "The next day, Sumire bubbles with excitement as she makes her way to the salon."
    "On the way, she sees fellow Justiciar Hazel looking worried."

    s "Oh hey Hazel! What's up?"
    h "Hey Sumire... Whoa, what's with the makeup?"
    s "I found this amazing salon yesterday! She gave me this whole makeover for free, and it even lasted all night long!"
    h "Uhh, you're supposed to take makeup off before you go to bed or else your pillow looks like nightmare fuel. But... it did stay on really well."
    s "You have to come with me! The lady who owns the place said they could even use some part-time help!"
    h "Well... I guess I could. OK, can you keep a secret? I've got a date later tonight, and I'm super nervous."
    s "Then you should *definitely* come with me Hazel. They'll help you feel confident and sexy in no time!"
    h "S... sexy!? I'm not sure I need that much before I..."
    "Without another word, Sumire grabs Hazel's hand and starts skipping down the road to the salon."

    jump ch02_saturday_salon

label ch02_saturday_salon:
    scene bg salon
    atsu "Welcome back young miss. And I see you've brought a friend!"
    s "Hello again! This is Hazel, and she told me she has a hot date tonight and needs to look *sexy*! Can we help her!"
    h "W... wait! I... I don't want to look too sexy!"
    atsu "Not a problem, please have a seat right here!"
