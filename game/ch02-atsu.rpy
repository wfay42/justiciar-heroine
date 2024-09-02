# Characters and other variables are defined in script.rpy

"""
Chapter 02: Atsugessho
Sumire gets entangled in new makeup, which is really Atsugessho
"""

define atsu = Character("Amane", who_color="#aaaaaa")

label ch02_start:
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
    atsu "What a beautiful speciment. But there is so much more we can do. We need to thin out those eyebrows, add a bold wingtip, some mascara will do."
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


