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
    atsu "Please, have a seat in the chair."

    menu:
        "Sit in the chair":
            "Sumire sits in the chair willingly, excited to see what the beautician will do."

        "Refuse":
            s "Oh, I'm not sure I have enough time for a full routine like this."
            atsu "Please, I insist."
            "Before she knows it, the beautician puts her hands on Sumire's shoulders, forcing Sumire down into the chair."
    "The chair is extremely soft. Without much thought, Sumire begins to completely relax every muscle in her body. She barely notices the beautician begin working."
    atsu "What a beautiful speciment. But there is so much more we can do. We need to thin out those eyebrows, add a bold wingtip, some mascara will do."
    atsu "And of course a beautiful lipstick and some matching eye shadow. I can see you love green, so of course we'll have to match that."

    "Sumire barely acknowledges what is being said to her. The combination of the chair and the smell of the perfume within the salon have rendered her into a state of nirvana."
    "Sumire doesn't even notice nearly half an hour of time passes while she is being dilligently worked on."

    atsu "(Thinking) Ha, this was too easy! This young woman will provide our kingdom with so much life energy!"
    atsu "Alright miss, all done! What do you think?"

    "Sumire snaps out of her stupor, but she is not quite herself. She sees herself in the mirror, completely delighted by what she sees."
    "Under the spell of the salon, Sumire is unable to see how the color of her skin has been completely drained, and her pupils are now replaced by hearts."
    s "It's beautiful! You've done such an amazing job? How can I thank you?"
    atsu "Please tell all of your friends about this place! And of course, come back any time!"


