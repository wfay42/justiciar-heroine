# Characters and other variables are defined in script.rpy

"""
Chapter 03: Naga
Kaede is heroine of this story.
Kaede gives new medicine to patients, turns out to be naga venom, TF'ing them.
Zoe and Yukino TF first in medical ward.
Kaede and Maika restrain Zoe, but realize Yukino escaped.
Maika stays to guard Zoe, Yukino goes to Hazel for help.
Yukino sneaks into Chisato's office, TF Chisato.
Yukino and Chisato go back to free Zoe. Yukino distracts Maika while Chisato frees Zoe. All 3 overpower Maika and TF her.
Kaede and Hazel find antivenom and inject themselves.
Kaede bad end, she has antivenom, making her immune to bites, but gets incubated in an egg for multiple days until TF'd.
"""

label ch03_start:
    scene black
    jump ch03_villain_intro:

label ch03_villain_intro:
    jump ch03_hospital_01

label ch03_hospital_01:
    scene bg hospital 01
    "We join our heroines in the medical ward of Justiciar HQ. Kaede dutifully takes cares of her injured comrades."
    show hospital 01
    k "And how is my favorite patient doing?"
    z "Heh. Just fine Kaede, thanks."
    y "If she's your favorite patient, what am I? Chopped liver?"

    show hopsital 02
    k "Oh, don't worry Yukino. You're also my favorite patient!"
    y "How does that even make sense? Whatever. My stomach is starting to act up again, can you give me something?"
    k "The antacids are next to your bed. Take 2 tablets, get some rest, and you should be right as rain soon enough!"
    k "Now if you'll excuse me, I need to get Zoe her shot."

    k "Of course! We just got a new shipment of medicine, just for you."

    show hospital 03b
    "Kaede looks at the new medicine. She knew her supplier had recently changed, but the pharmacy assured her that the dosages and everything else were equivalent."
    "Kaede always gets nervous with a change like this, but she knows it's inevitable."
    k "OK Zoe, are you ready?"
    z "Yup, my top is off."

    show hospital 04
    k "Sorry again that you have to take the whole uniform top off."
    y "Wait, what did you say?"
    k "No peeking at your fellow patients, please!"
    z "It's fine, it's just how they're engineered. It's my fault for not wearing anything more comfortable when I come in."
    k "OK, here comes a little pinch."

    show hospital 05
    "Zoe always puts on a brave face, but she is still a little nervous around needles."
    show hopsital 06
    "Zoe winces a little bit this time. She feels a hot burn in her arm after the shot, but it quickly fades."

    show hospital 07
    k "Are you OK? I saw you wince a bit there?"
    z "It's fine, Kaede. Nothing a professional Justiciar can't handle."
    k "Alright, well you go ahead and keep resting. You and your bunkmate over there both need rest to recover."
    z "Thanks, Kaede."

    show hospital 08
    "Kaede heads for the door; her other duties calling."
    "Zoe lays down, having trouble finding a comfortable spot. She didn't want to worry her friend, but she does think she may have some kind of reaction to the injection."
    "If things get worse, she'll call Kaede back."

label ch03_hospital_02:
    show hospital 09
    "Zoe lay on her back with growing discomfort. Her body burning"