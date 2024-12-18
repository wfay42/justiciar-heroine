# Characters and other variables are defined in script.rpy

"""
Chapter 02: Naga
Kaede is heroine of this story.
Kaede gives new medicine to patients, turns out to be naga venom, TF'ing them.
Zoe and Yukino TF first in medical ward.
Kaede and Maika restrain Zoe, but realize Yukino escaped.
Maika stays to guard Zoe, Yukino goes to Hazel for help.
Yukino sneaks into Chisato's office, TF Chisato.
Yukino and Chisato go back to free Zoe. Yukino distracts Maika while Chisato frees Zoe. All 3 overpower Maika and TF her.
Kaede and Hazel make antivenom
    Decision: inject self, or inject converted.
    Inject self leads to capture in eggs and conversion.
    Inject others leads to Hazel TF'ing, but Zoe reverts, then Kaede helps her revert others.
Kaede bad end, she has antivenom, making her immune to bites, but gets incubated in an egg for multiple days until TF'd.
"""

$ kaedeInnoculateSelf = False

define nagas = Character("Naga Troopers", who_color="#cc66cc")

label ch02_start:
    scene black with dissolve
    jump ch02_villain_intro

label ch02_villain_intro:
    scene black
    "Chapter 2"
    show hospital v 01 with dissolve
    v "Well, that plan with Amane was a complete failure. Naga troopers, I hope your plots are performing better."

    show hospital v 02
    nagas "Yes mistress. It has taken many years, but through a combination of tax loopholes, shell companies, bribery, blackmail, and exploitation of existing corruption within the local government, we have been able to inject ourselves into the local healthcare supply chain!"

    show hospital v 03
    v "Disrupting a necessary part of modern society is certainly nefarious, which I love, but how does that further our plans to defeat the Justiciars?"

    show hospital v 02
    nagas "We have been able to displace an existing trusted healthcare vendor for one type of common injection."

    show hospital v 03
    v "I'm still lost."

    show hospital v 04
    nagas "We have replaced the true injection with our naga venom. In no time, our naga army will grow to become unstoppable."

    show hospital v 05
    v "Quite a complicated plan, but if you can pull this off, I will be very pleased. Report back to me as we see the results of this."
    scene black with dissolve

    jump ch02_hospital_01

label ch02_hospital_01:
    scene bg hospital 01 with dissolve
    "We join our heroines in the medical ward of Justiciar HQ. Kaede dutifully takes cares of her injured comrades."
    show hospital 01
    k "And how is my favorite patient doing?"
    z "Heh. Just fine Kaede, thanks."
    y "If she's your favorite patient, what am I? Chopped liver?"

    show hospital 02
    k "Oh, don't worry Yukino. You're also my favorite patient!"
    y "How does that even make sense? Whatever. My stomach is starting to act up again, can you give me something?"
    k "The antacids are next to your bed. Take 2 tablets, get some rest, and you should be right as rain soon enough!"
    k "Now if you'll excuse me, I need to get Zoe her shot. We just got a new shipment I need to inspect."

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
    show hospital 06
    "Zoe winces a little bit this time. She feels a hot burn in her arm after the shot, but it quickly fades."

    show hospital 07
    k "Are you OK? I saw you wince a bit there?"
    z "It's fine, Kaede. Nothing a professional Justiciar can't handle."
    k "Alright, well you go ahead and keep resting. You and your bunkmate over there both need rest to recover."
    z "Thanks, Kaede."

    show hospital 08
    "Kaede heads for the door; her other duties calling."
    "Zoe lays down, having trouble finding a comfortable spot. She didn't want to worry her friend, but she does think she may have some kind of reaction to the injection."
    "Zoe calms herself down a bit. She knows that if things get worse, she'll call Kaede back."

    jump ch02_hospital_z_nagatf

label ch02_hospital_z_nagatf:
    show hospital 09
    "After half an hour, Zoe begins sweating as she lays on her back."
    show hospital 10
    "The dull pain has been slowly creeping up her arm. Zoe decides to undress again, to see if she sees any sign of brusing."

    show hospital 10a
    "Taking off her sentai top, Zoe is shocked by what she sees."
    show hospital 11
    "Scales creep across most of her arm and onto her chest."
    "Worry turns into panic as her heart races at the sight of this. Her beating heart pumps the toxin inside of her ever faster to the different parts of her body."

    show hospital 12
    "The scales spread more quickly, covering the entirety of her upper body."
    show hospital 13 with dissolve_2
    "Her face follows soon after, along with changes to her eyes..."
    show hospital 14 with dissolve_2
    "Followed by her hair."

    show hospital 15
    "If all of that wasn't bad enough, something even worse begins happening to her legs."
    show hospital 16 with dissolve_2
    "Her muscles jerk as her legs are drawn closer together."
    show hospital 17 with dissolve_2
    "Her boots melt off of her feet. With her legs unable to squeeze together any tighter, they begin to merge together."
    show hospital 18 with dissolve_2
    "Within a few moments, her legs have merged, covering themselves in scales like the rest of her body."
    jump ch02_hospital_y_nagatf

label ch02_hospital_y_nagatf:
    show hospital 19
    "Unaccustomed to a tail where her legs used to be, Zoe clumsily rolls over, hoping to get the attention of Yukino, sleeping in the bed next to her."
    show hospital 20
    "Zoe sees Yukino, fast asleep on the hospital bed. Before she can call out, Zoe feels something... strange."
    show hospital 21
    "The sight of her sleeping friend makes her heart race. The feeling is almost instinctual."
    "She can't help but feel excited to see such a defenseless piece of... prey."
    show hospital 22
    "Zoe shakes her head, dismissing the thought from her mind. She needs Yukino's help, after all."
    show hospital 23
    "Zoe crawls out of the bed, slithering over next to her comrade. She opens her mouth once again to wake Yukino, but the feeling returns."
    show hospital 24
    "Zoe sits, mouth agape, watering."
    show hospital 25
    "She sees the delicate, vulnerable body of Yukino lying before her."
    show hospital 26
    "Zoe feels another pulse of excitement, this time in what had been her loins. Her mind is clouded by these insatiable impulses."
    show hospital 27
    "She begins to bring her mouth closer to Yukino. She knows she wants to speak, to wake her friend, to get the help she needs, but she cannot."
    show hospital 28
    "Silently, Zoe's fangs pierce Yukino's skin. Yukino does not react at all."
    "Immediately, Zoe's fangs begin to inject her venom into Yukino. The sensation is fast and intense. Zoe feels this must be what ejaculation must feel like."
    "After only a moment, Zoe's venom is spent, and the toxin now courses through Yukino's body. The process has begun, and now it cannot be stopped."
    show hospital 28a
    "Zoe experiences an ecstasy she has never felt before. An orgasmic release as she has done what her body craved so badly."
    show hospital 29
    "Zoe is momentarily scared and frightened by what she has done, but this washes away almost instantly with the excitement of welcoming her friend into her sisterhood."

    show hospital 32
    "Zoe sits up, watching the change take hold of Yukino. The injection of Zoe's venom works much faster than the chilled venom from the syringe. Yukino begins changing quickly."
    window hide
    pause
    show hospital 32a with dissolve_2
    pause
    show hospital 33 with dissolve_2
    pause
    window show
    "Zoe's excitement increases as she knows that under her uniform, the rest of Yukino's skin is transforming into scales."
    window hide
    show hospital 33a with dissolve_2
    pause
    window show
    "As if Zoe's will to see Yukino's body had caused it, Yukino's uniform tears apart as her breasts transform larger than her skin-tight uniform can handle."
    window hide
    show hospital 34 with dissolve_2
    pause
    window show
    "Yukino's strong fortitude allows her to sleep through the transformation, completely undisturbed."

label ch02_hospital_maika_inspection:
    show hospital 35
    "A few minutes later, Kaede returns with Maika."
    k "I'm sure you visiting Zoe and Yukino will make them both feel better."
    m "Of course! I'm just glad the two of them are OK. We all need some R&R every now and then. Hey Zoe, Yukino, how are you two..."
    show hospital 36
    m "Oh my god!"
    show hospital 37
    z "Oh, hey Maika. Hey Kaede. Yukino and I are feeling great, thanks for asking."
    y "Yeah, we were just playing around a bit, you know, sexually. Do you see my beautiful body? It was a gift from Zoe!"
    z "I'm glad I could share it with you. And it's all thanks to Kaede. That new batch of injections sure packs a punch."

    show hospital 37a
    "Fighting through the shock of what she's seeing and hearing, Kaede is able to piece together what happened."
    k "Oh no, the new batch of injections was tainted! It's transformed them into those... monsters!"
    m "It must be a plot from the Dark Sisterhood. Zoe, Yukino, you two stay here. We'll help find a cure for this, I promise!"

    show hospital 37
    z "Cure? For what? True beauty? And power?"
    show hospital 38
    z "I think not. We were planning to share this gift with everyone we can. I think we'll start with you two."

    show hospital 39
    m "I was afraid of that. Kaede, you think you can incapacitate them?"
    k "I think so. I'm a doctor, not a veterinarian, but I'm guessing the venom is in their fangs in their mouths. Avoid that at all costs."
    m "Alright. Sorry about this in advance!"

    show hospital 40
    window hide
    pause
    window show
    "Kaede is able to make a swift kick to Zoe's face, knocking her out in one hit."
    "Maika, however, doesn't fare as well. Knowing Maika's attack patterns, Yukino easily slips past the red sentai, darting into the hallway."

    show hospital 41
    m "Damnit, she slipped right past me."
    k "You stay here, Maika, and watch Zoe. I'll go after Yukino. I have some suppressants in my toolbelt I may be able to use."
    m "On it. Stay safe, Kaede!"

    show hospital 42
    k "Hey, Hazel, we've got a situation. Start analyzing those new syringes I got. I need you to make an anti-venom from that."
    h "Oh, sure thing. Were they tainted and now they're turning people into monsters?"
    k "Yes, exactly. Snake monsters. Wait, how the hell did you guess that?"
    h "You work in this lab long enough, you see a lot. I'm on it. Give me five minutes. Ten, tops."
    jump ch02_hospital_c_nagatf

label ch02_hospital_c_nagatf:
    show hospital 43
    "Elsewhere, Director Chisato is hard at work in her office."
    "Little does she know, she has an uninvited guest."
    show hospital 44 with dissolve_2
    "Yukino dangles upside-down behind Chisato. Yukino managed to evade Kaede by entering the air ducts. Something she learned from her last mission."
    show hospital 45
    "Yukino lowers herself down slowly, curling her upper body right-side up without touching the ground, her heart racing."
    show hospital 46
    "Her heart beats faster with every inch she gets closer. Her mind swarms with thoughts of how beautiful Chisato will be once she becomes a naga like Yukino. She can almost feel the warmth from Chisato's skin."
    show hospital 47
    "It's now or never. If she moves any closer, Chisato will feel Yukino's breath, or a glancing disturbance of her hair. With animal precision, Yukino launches to bite Chisato."
    show hospital 48
    window hide
    pause
    c "AHH! G... get off me!"
    show hospital 49
    "Chisato grabs Yukino's head, attempting to dislodge the monster attached to her neck. But Yukino is undeterred. Waves of pleasure course through Yukino's body as she feels the venom rush into her victim."
    show hospital 50a
    "Yukino, having finished filling her victim with venom, drops her tail from the ceiling, and relaxes backwards as if she had just engaged in coitus."
    "Chisato sits in her chair, shocked, and unable to move. Yukino's venom has had a mutation, adding a paralytic effect."
    "Chisato sits in terror as she cannot speak, cannot move, barely able to breathe, as the venom runs through her."
    "Chisato is unsure what is happening, but she knows that she is changing."

    window hide
    show hospital 50c with dissolve_2
    window show
    "Chisato feel her skin change, starting at the injection site. It crawls up to her mouth, and she feels her own incisors grow into pointed fangs."

    window hide
    show hospital 50d with dissolve_2
    window show
    "Next, she feels the change creep up her face. Her ears begin to point into tips; knocking her glasses off of her face. Her nose shrinks to be replaced by two slits."

    window hide
    show hospital 50e with dissolve_2
    window show
    "Chisato's vision changes as her face completes it's trasformation. She looks out of new, reptilian eyes. Colors look different than they ever had before."
    "At first she experiences shock, followed by wonder at how the world now looks. But it is cut short, as she feels her chest throbbing as it pushes against her tight suit."

    window hide
    show hospital 50f with dissolve_2
    window show
    "Chisato's expanding breasts tear through her suit like tissue paper. This is the first Chisato can see of her changing skin. Her full chest jiggles as she notices the same scales crwaling up her arms."

    window hide
    show hospital 50b with dissolve_2
    window show
    "Chisato watches as the inevitable happens. Her tattered suit falls from her body as her hands cover in scales, and her fingernails turn to sharp claws. \"What kind of monster have I become?\" she thinks to herself."
    "Chisato's near-infinite willpower keeps the venom's psychoactive effects at bay. She knows if she can outlast the paralysis, she can find a way out of this."
    "That's when Yukino leans over to fondle her supervisor's new assets."

    show hospital 51
    y "Wow, Chisato. I didn't know you were hiding these gorgeous knockers all this time."
    "Chisato struggles against the venom, reclaiming her ability to speak."
    c "Y... Yukino. Stop this. Have to... reverse this."
    y "Oh come on, don't be like that, captain. You have no idea how great it felt to bite into you like that. The rush of venom shooting out of my glands into your warm blood."

    show hospital 52
    "Yukino's words begin to have an effect on Chisato. The overwhelming power of the venom combined with Yukino's fondling, capped off of by this dirty talk is almost too much to bear."
    y "Besides, I need your help. Zoe was the first to transform, but now Maika is guarding her. How about you come with me."
    "Yukino leans in close to Chisato. Maneuvering right next to Chisato's ear. Chisato trembles with excitement, trying to fight it. Yukino breathes once into Chisato's ear, then begins to whisper."

    show hospital 52a
    y "I'll even let you be the one to bite Maika."

    show hospital 53
    "That was it. Something snapped inside Chisato's mind at the thought of envenoming Maika. The taboo thoughts of biting down on her most trusted comrade, converting her into a monster."
    "Chisato can't stop thinking about her body entwined with Maika's as Maika transforms. Feeling Maika struggle. Knowing that the venom will win. Knowing they can be together in bliss as nagas."

    show hospital 54
    c "OK, my sister. We have work to do."
    y "Yes! That's what I'm talking about!"
    jump ch02_hospital_m_nagatf

label ch02_hospital_m_nagatf:
    show hospital 55
    "Maika stands diligently, watching the captive Zoe."
    z "Maika, can you let me out of this already? My venom's refractory period is over, and I feel like I need a bite."
    m "You're going to stay right there until Kaede is back with a cure."
    "*Thump*"

    show hospital 56
    m "Yukino! So I guess you evaded Kaede. But I'm glad you're back. We just need you to sit tight until Kaede gets back with a cure."
    y "Ha! In this body, I don't think I can do much \"sitting\" any more. And besides, I'm not here to surrender. I'm here for round two."
    m "I was afraid you'd say that. Alright then, let's do this!"

    show hospital 57
    "As Maika engages in combat with Yukino, she is oblivious to Chisato sneaking into the room from outside the window."
    show hospital 57a
    z "Chisato! You look great! Now get me out of here!"
    c "Shhhhh! We have to do this quietly or Maika will notice."

    show hospital 58
    "Yukino puts on a good show trying to stall Maika, but Maika eventually lands a healthy blow."
    m "It's over Yukino. Time to tie you up like Zoe."
    show hospital 58a
    y "Heh, like Zoe, huh?"

    show hospital 59
    m "Z... Zoe! But how did you?"
    m "Ch... Chisato! No! That's what Yukino was doing?"
    c "That's right, she paid me a delightful visit. And she promised me something. You."
    m "Chisato, no! Stop! You have to fight this!"
    "Maika's words only feed into Chisato's arousal. Seeing the proud justiciar helplessly struggling against the three nagas titillates Chisato to no end."
    show hospital 60
    "Chisato moves her fangs closer to Maika's skin. Slowly. Savoring every sound of Maika's resistance."
    m "Chisato, no, please, stop! Stop! I don't want to be a snake! No! Please, let me go!"
    "Maika begging for release was all that Chisato could take. She needed to release her venom. Now."

    show hospital 61
    window hide
    pause
    window show
    m "No!"
    "Maika weakly let out her last plea. But it was enough to send Chisato over the edge. The feeling of the venom leaving her mouth was unlike any orgasm she had experienced."

    show hospital 62
    "Zoe releases Maika's arms. She knows the transformation has begun, and there is no need to restrain her comrade."
    m "Chisato... What have you done to me?"
    "Chisato just chuckles to herself, giving Maika no verbal response."

    show hospital 62a with dissolve_2
    "Within moments, the change spreads across half of Maika's face, and down her ponytail. Her hair takes on an even more vibrant color as her nose is replaced by slits, and her eyes become reptilian."

    show hospital 62c with dissolve_2
    "The change spreads even further, completing the transformation of Maika's face and hair."

    show hospital 64c
    "The nagas tear Maika's shirt off of her so that they can see how the change is developing."
    c "Beautiful. You're progressing well."
    show hospital 64d with dissolve_2
    pause

    show hospital 65c
    "Maika is shocked and disgusted at the sight of her breasts growing rapidly; jiggling around like balloons."
    "Her captors can't help but laugh at Maika's helplessness."

    show hospital 66
    "Before she can say another word, Maika begins falling backwards as if she was pushed."

    show hospital 67
    m "Ack. What now?"

    show hospital 68
    m "*Gasp* No! No no no no no no no NO!"

    show hospital 69
    "Maika looks at her legs, or what is left of her legs. A beautiful snake tail is all that remains. Her body's transformation is complete."

    show hospital 69a
    c "That was so cute, the way you stumbled and fell. Don't worry, you're going to get used to that tail."
    "Maika sits, dumbfounded, as her comrades kneel down besided her. Maika feels her skin get warm as Chisato's breast brushes against her ear. The closeness of the other nagas begins to make her sweat."
    m "Chisato... we... we have to get the cure from Kaede. It's not too late!"
    c "You're still on that? Do you think we want to go back to being boring humans? I think we need to convince you another way."

    show hospital 69b
    window hide
    pause
    window show
    "Chisato and the other close in on Maika, deciding to give her a sexual pampering she won't forget."
    m "Wha... what are you doing?"
    c "Just giving you a little massage. Isn't that what friends are for?"
    y "That's right, Maika. Just relax. Here, hold my hand while the others help you."
    z "Exactly. Stop worrying and feel our hands sliding across your new, buttery soft body. Feel each finger as it passes by your nipples, up and down, and up and down."
    m "No. Please. Stop! I can't handle much more of this. I think I'd lose my mind if you squeezed my breasts, even a little, as you slide over them. Please, anything but that!"
    c "Oh, we wouldn't want that, would we?"
    z "Oops, my hand slipped Maika, I hope that doesn't..."

    show hospital 69c
    window hide
    pause
    window show
    m "Yes! Ohhhh fuck."
    "With Zoe's slip of the wrist, Maika is sent over the edge."
    c "Have we convinced you yet, Maika?"
    m "Heh. Heh. Whoo. Yes, we need to share this everyone."
    c "My thoughts exactly."


    jump ch02_hospital_hazel_helping

label ch02_hospital_hazel_helping:
    scene black
    show hospital 70
    h "Alright, the synthesis is complete. We've only got the one dose so far. The rest are still cooking."
    s "I can make sure those finish processing. What do you think you'll do with that one?"

    k "I'm sure I'll know what to do when the time is right."
    jump ch02_hospital_h_and_s_nagatf

label ch02_hospital_bad_hazeltf:
    show hospital 71a
    k "Best to innoculate myself so I can subdue them until the other doses synthesize."
    $ kaedeInnoculateSelf = False
    jump ch02_hospital_h_and_s_nagatf

label ch02_hospital_good_hazeltf:
    show hospital 71b
    k "I need to inject one of them soon before they spread further. If I can slow them down and rally our forces, we should be able to contain things."
    $ kaedeInnoculateSelf = True
    jump ch02_hospital_h_and_s_nagatf

label ch02_hospital_h_and_s_nagatf:
    show hospital 71c
    k "I still need to find Yukino. Wish me luck."

    show hospital 72
    "Kaede rushes through the hallways of the headquarters, unable to locate Yukino. Running out of ideas, she decides to give Maika another visit."

    show hospital 73
    k "Wait, where's Maika!? And Zoe is gone too. Ohh, this can't be good."
    k "OK. Time to regroup with Hazel and Sumire. I hope those extra doses are ready."

    show hospital 74a
    "Rushing back to the lab..."
    show hospital 74b
    "Kaede is shocked by what she sees."

    show hospital 75
    window hide
    pause
    window show
    "Hazel and Sumire are forced down to their knees, stripped completely naked."
    show hospital 76
    "Their mouths are forced to entertain the breasts of two nagas."
    y "Looking for me, Kaede?"
    c "We're glad you could join us."

    show hospital 77
    k "Ch... Chisato! No, not you too! I'm sorry, but I have to stop you!"

    show hospital 78
    "Before she can take another step, Kaede is ambushed. Without any warning, she feels two fangs sink deep into her neck along with the hot rush of venom entering her body."
    k "Maika! No! They got you too! And now... and now me..."
    k "I have to think fast, I need to use the syringe before it's too late."
    jump ch02_goodend_kaede_tf

label ch02_goodend_kaede_tf:

    k "Sorry about this, Maika."
    show hospital 79b
    window hide
    pause
    window show
    "Kaede thrusts the syringe into Maika's belly, catching the naga completely off guard."

    show hospital g 01
    z "Whoa there tiger. We got a feisty one here."
    "Maika reels from Kaede puncturing her with the syringe. Before Kaede can proceed any further, Zoe swoops in, grabbing her arms."
    z "Well, it looks like our roles are reversed now, huh Kaede? You know, I didn't like being chained up to that gurney very much."
    k "Maika, you have to resist the infection! You're our last hope now!"

    show hospital g 02
    z "Enough of that. How about we have a little sit and think about what we've done. And enjoy the show in front of you."

    show hospital g 03
    "Kaede had almost forgotten about Hazel and Sumire. Still forced onto their knees, pleasuring the nagas in front of them."
    y "That's it Sumire, I'm almost there."
    c "Oh god, me too. Keep it up Hazel."

    show hospital g 04
    window hide
    pause
    window show
    "Chisato and Yukino unload juices from their breasts directly into the mouths of their victims, with spray landing over the rest of their bodies."

    show hospital g 05
    c "Thank you for that ladies. You two are dismissed."
    h "Quick, Sumire, get the syringes before it's too late."
    s "Y... yes. I'm going. Urg. Why do my legs feel like jelly?"

    show hospital g 06
    window hide
    pause
    window show
    s "Oh no!"
    h "But how!?"
    "Hazel and Sumire are shocked to find their lower extremeties have been replaced by the same snake tails of their comrades."

    show hospital g 07c
    window hide
    pause
    window show
    s "Hazel, I'm scared! What... what do we do?"
    h "It's too late. We can't move our bodies in this state."


    show hospital g 07d with dissolve_2
    h "I'm sorry to say, but we've lost."
    show hospital g 07e with dissolve_2
    h "Once we finish the transformation, we're going to like it. Just like them. Even though we have the antidote we won't want to use it."
    show hospital g 07b with dissolve_2
    h "We're going to be sex-crazed nagas, just like them."

    show hospital g 08
    z "You say that like it's a bad thing. Well Kaede, how did you like the show?"
    z "Kaede?"
    show hospital g 09
    window hide
    pause
    window show
    k "Oh yesssss. It was amazing."
    "While everyone was distracted by Hazel and Sumire's struggles, Kaede had completely transformed as well. The venom had already completely taken over her body and corrupted her mind."

    jump ch02_goodend_maika

label ch02_goodend_maika:
    show hospital g 10
    "As all of her friends have completed their transformation into nagas, Maika begins to feel as if a fog has lifted from her mind."
    m "Wha... what have I been doing? Zoe was tied to the bed, then... then Yukino came in, then Chisato, that's right! And then they..."

    show hospital g 11
    m "*Gasp* That's right, they turned me into a naga too!"
    m "But Kaede hit me with that syringe. OK, that must be the cure. Am I going to turn back to a human? I'd better hurry and do something before then or else they'll just do it to me again."

    show hospital g 12
    m "They got Sumire and Hazel too. And Kaede... I'm sorry. I wasn't strong enough to stop them. But I'll make this right."
    h "Hey Maika, we were going to do some science experiments with our new bodies. Care to join us? It's for science."

    show hospital g 13
    m "Oh yeah, sure, you know I'd never miss anything for science! I just, uh, need to use the bathroom for a minute."

    show hospital g 14
    m "Great, there's only three of them. There's no way I can take them all out. Unless..."
    m "Ugh, this is such a terrible idea. But it's the only one I've got."

    show hospital g 15
    m "Come to mama! God, I hope this works..."
    "Maika feels some swelling in her breasts. They begin to feel firmer and tighter. A sensation similar to needing to pee, she knows it's coming soon."

    show hospital g 16
    m "Hey ladies, open wide!"

    show hospital g 17
    "Maika's body can hold on no longer. Her breasts shoot out a firehose of liquid, enhanced by the overdose of the serum."

    show hospital g 18
    "The nagas all open their mouths gladly, excited to see Maika joining in on the fun."
    h "Yeahhh, Maika! That was great!"

    show hospital g 19
    m "Heh. Yeah. Greaaaaat."
    "Maika feels completely spent after that eruption. She can't stand for another second, and begins to fall backward."

    show hospital g 20a
    m "I... I did it."
    show hospital g 20b with dissolve_2
    m "Now it's time for a nap."

    show hospital g 21a
    h "Does this stuff taste funny to you?"
    s "Yeah, it doesn't taste like Yukino's milk."
    show hospital g 21b with dissolve_2
    k "Wait, we're human again. I knew trusting Maika was the right choice. Wait, where is Maika?"

    show hospital g 22
    "With another villainous plot thwarted by our heroines, Maika takes a well-deserved rest. Although she's going to get cold lying there. Someone should probably bring her a blanket."


label ch02_villain_outro:
    scene black
    show hospital v 06
    v "Another failure. Explain yourselves."
    show hospital v 07
    nagas "Somehow, the health inspector was tipped off to our plot and revoked our corporation's authorization to distribute. As part of their investigation, they've also begun auditing our shell company!"
    v "Without the corporate babble!"
    nagas "They figured out our injections were naga venom that would transform people into nagas, then shut us down, and are distributing the anti-venom."
    v "With the amount of resources you three have wasted, I should have you executed. But I have a better idea. A fate worse than death."

    show hospital v 08
    v "You're banished to the accounting department!"

    show hospital v 08 with dissolve:
        matrixcolor SaturationMatrix(0)
    "End of Chapter 2."
