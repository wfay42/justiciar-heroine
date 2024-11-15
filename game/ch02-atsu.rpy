# Characters and other variables are defined in script.rpy

"""
Chapter 02: Atsugessho
Sumire gets entangled in new makeup, which is really Atsugessho
"""

define atsu = Character("Amane", who_color="#aaaaaa")

label ch02_start:
    scene black
    "Chapter 1"
    jump ch02_villain_intro

label ch02_villain_intro:
    scene black
    show v atsu 01 with dissolve
    v "Those damn Justiciars continue to foil our plans. I hope you have a plan, Amane."

    show v atsu 02
    atsu "Of course mistress. I have already succeeded in creating a cosmetics shop in a popular shopping district. This will act as a front for our plans."
    atsu "My makeup will drain the energy from those who use it, converting them to our cause."
    v "Very well. Begin your plan. And do not disappoint me. Don your disguise and begin your mission."

    show v atsu 03 with dissolve_2
    atsu "Yes, mistress. Anything for the Dark Sisterhood."

    show v atsu 04
    v "Yes, blessed are we dark sisters. And remember, failure is not an option. Is that understood?"

    show v atsu 05
    atsu "Of course, mistress."

    jump ch02_at_salon


label ch02_at_salon:
    scene bg hq
    "After a successful mission, the Justiciars are relaxing."

    show s unsure
    s "That last fight was bonkers!"

    show s casual excited
    s "I'm off to do some retail therapy, see you all later!"

    scene bg shopping
    "Sumire strolls down the street to the local shopping district. She notices a new shop has opened up, and decides to take a look."

    show s atsu 01
    atsu "Hello young miss, would you be interested in a free sample?"
    s "Ooh, free sample of what?"
    atsu "Our latest perfume, Eau de Atsu."
    show s atsu 02
    s "Sure thing!"

    show s atsu 03
    show smoke atsu light
    "The clerk gives a heavy spritz of the perfume to Sumire. Sumire takes in a deep breath enjoying its flowery scent."

    hide smoke
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
    show smoke atsu light zorder 0
    show s atsu 07 zorder 1
    "The chair is extremely soft. Without much thought, Sumire begins to completely relax every muscle in her body. She barely notices the beautician begin working."
    show s atsu 08
    atsu "What a beautiful specimen. But there is so much more we can do. We need to thin out those eyebrows, add a bold wingtip, some mascara will do."
    atsu "And of course a beautiful lipstick and some matching eye shadow. I can see you love green, so of course we'll have to match that."
    "Sumire barely acknowledges what is being said to her. The combination of the chair and the smell of the perfume within the salon have rendered her into a state of nirvana."

    hide smoke
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
    atsu "In fact, we're still hiring. Would a beautiful young lady like yourself be interested?"
    s "Oh, I already have a full-time job."

    show s atsu 13
    "Sumire's heart begins to beat a little faster with the thought of getting to apply makeup on customers just as the beautician had done to her."
    "Part of her wants to stand up and leave the salon without another word, but she just can't bring herself to do it."

    show s atsu 12
    s "But I do have time off on the weekends! I'll be here tomorrow, that's normally my day off."
    atsu "I very much look forward to it."

    show s atsu 14
    "Sumire walks out of the store. She can't believe she said that, but she feels so excited to return the next day that she doesn't care."

    show s atsu 15
    atsu "A perfect specimen indeed."
    show s atsu 16 with dissolve_2
    atsu "She will be a crucial component of the plan."
    hide s atsu 16 with dissolve_2

    jump ch02_saturday_street

label ch02_saturday_street:
    scene bg street
    show h atsu 01
    "The next day, Sumire bubbles with excitement as she makes her way to the salon, practically sprinting."

    show h atsu 02
    "On the way, she sees fellow Justiciar Hazel looking worried."

    show h atsu 03
    s "Oh hey Hazel! What's up?"
    h "Hey Sumire... Whoa, what's with the makeup?"
    s "I found this amazing salon yesterday! She gave me this whole makeover for free, and it even lasted all night long!"
    h "Uhh, you're supposed to take makeup off before you go to bed or else your pillow looks like nightmare fuel. But... it did stay on really well."
    s "You have to come with me! The lady who owns the place said they could even use some part-time help!"
    h "Well... I guess I could. OK, can you keep a secret? I've got a date later tonight, and I'm super nervous."
    s "Then you should *definitely* come with me Hazel. They'll help you feel confident and sexy in no time!"
    h "S... sexy!? I'm not sure I need that much before I..."

    show h atsu 04
    "Without another word, Sumire grabs Hazel's hand and starts skipping down the road to the salon."

    jump ch02_saturday_salon

label ch02_saturday_salon:
    scene bg salon
    show h atsu 05
    atsu "Welcome back young miss. And I see you've brought a friend!"
    s "Hello again! This is Hazel, and she told me she has a hot date tonight and needs to look *sexy*! Can we help her!"
    h "W... wait! I... I don't want to look too sexy!"
    atsu "Not a problem, please have a seat right here! Miss Sumire, please follow me."
    s "Sure thing! We'll be right back Hazel, just relax."

    show h atsu 06
    "Hazel sits uncomfortably in the chair waiting for her friend's return. She feels excited, but also uneasy."
    "Hazel's mental fortitude slows down the hypnotizing effect of the salon chair, but she may soon be trapped by it as well."

    show h atsu 07
    s "We're baaack! Look, Hazel! She's going to teach me everything I need to know about this job! And you get to be my first victim, hehe."
    atsu "That's correct. You can relax knowing I have everything under control. Your friend will simply be watching."
    atsu "This is only the first foray into what is surely to become a rewarding career for her."
    h "Career? Sumire, you've already got a job. An *important* job."
    s "Pfft, sure, but it's not nearly as fun as this! Maybe you should join as well!"

    menu:
        "Grab Sumire and get out of here":
            h "Something's wrong about this salon Sumire. I'm taking you out of here!"
            show smoke atsu light zorder 0
            show h atsu 08 zorder 1
            "Before Hazel can even get out of the chair, the beautician sprays a hefty amount of perfume into her face."
            atsu "Now now. This is a place of relaxation! Come Miss Hazel, have a sit and let us do all the work."
        "Wait for now, knowing you'll talk about it later":
            h "I think I'll keep my job, and you should too! We'll talk about this later."
            atsu "A grand choice. Now please, sit back and relax."
            show smoke atsu light zorder 0
            show h atsu 08 zorder 1
            "With that, the beautician gives a ginger spray of the perfume onto Hazel's face"
    show h atsu 09
    "Sitting back in the chair, Hazel has fallen victim to aroma of the perfume. All she can do now is sit back and enjoy the ride."

    hide smoke
    show h atsu 10a
    atsu "Would you like to start with the lipstick?"
    s "*Gasp*! But I thought I was only going to watch?"
    atsu "You need practice if you are truly going to be my apprentice. Besides, I'm sure your friend wants to see you succeed."

    show h atsu 10b
    "Sumire swiftly takes the lipstick and begins to apply it on Hazel's lips."
    atsu "Very good. You're a natural. With your help, we'll be able to service hundreds of customers in a day."
    "Like Sumire, Hazel drifted through her dreamlike state until the job was complete."

    hide h atsu 10b
    atsu "We're all done. Are you ready to see your date-ready makeover?"
    h "I... suppose so..."

    show h atsu 11 with dissolve_2
    "Hazel is sitting at attention, completely entranced by her new look. Just like Sumire, her pale skin and heart-shaped pupils do not even register."
    h "I look... Stunning. And... hot!"
    atsu "We decided your glasses got in the way of your beautiful eyes, so we decided to remove them."
    h "That's fine, I really only need them for reading anyway."

    show h atsu 12
    s "Now don't be mad, but I actually handled your lipstick. What do you think?"
    h "Wow, it looks great. And this is your first time?"
    s "Sure is! Helps that I had a great teacher."
    atsu "And you're quite the receptive student."

    show h atsu 13
    atsu "If you liked our services today, please do recommend us to your friends. Now go enjoy your date. Your friend here will be staying to finish out her shift."
    h "Thank you so much! I'll see you tomorrow, Sumire!"
    s "Let me know how your date goes!"

    show h atsu 14a
    atsu "Great work, my apprentice."
    s "Thank you, mistress."
    atsu "Are you ready to put your learnings to work."

    show h atsu 14b with dissolve_2
    s "Of course mistress."
    hide h atsu 14b with dissolve_2

    jump ch02_saturday_hazel_date

label ch02_saturday_hazel_date:
    scene bg shopping
    show h atsu 15
    "Hazel strolls, no, struts down the street with a newfound confidence. The nervous woman from the morning is gone, replaced by a stunning femme fatale."
    "Hazel can feel the eyes of everyone walking by her, feeling their stunned silence at her beauty."
    "Thinking about her date, she feels an urge deep within. She knows what she wants."

    show h atsu 16
    "Hazel picks up her phone, deciding to send a video message to her date. Before she hits record, the smallest piece of her hesitates. She's never done anything like this. Especially not for a blind date."
    "But the feeling passes as she hits record."
    h "Hey big boy. I've been thinking. How about we have dinner at my place? I'll shoot you my address. I'll give you dinner and a show. Get there fast for a reward."
    "She immediately sends the message without a second thought."

    show h atsu 17
    h "I'd better get back. I need to pick out what to wear, and I know he's going to be rushing."

    scene bg apartment
    "There's a knock at Hazel's door. The knock sounds somewhat rushed, although the person knocking is trying to keep it cool."
    h "It's unlocked. Come in. I'm in the bedroom."

    "Hazel's blind date makes his way to the bedroom, his heart beating out of his chest with excitement. The apartment is small, so it's not hard to find his way to the bedroom."
    "With only one thing on his mind, he is completely oblivious to the smell of perfume throughout Hazel's apartment. The scent only drives him more wild."
    "Turning the corner, he sees exactly what he'd hoped to see."

    show h atsu 18 with dissolve_2
    h "I'm so glad you could make it. You really didn't keep me waiting. I'm afraid I didn't have time to make anything for dinner. But that's OK, I think you're actually going to be eating out anyway."

    show h atsu 19
    "Opening her legs, Hazel motions towards her pussy. Her date finally notices her lack of panties. Nothing is blocking his way, and the perfume has made him into a willing servant to her every command."

    show h atsu 19a
    h "Well, what are you waiting for?"
    "The man wraps his lips around her pussy, enveloping her with his warm breath. His tongue leisurely extends out, and begins to play around."

    show h atsu 20
    "The first wave of pleasure courses through Hazel's body. This isn't Hazel's first time with a man by any means, but the makeover has heightened every part of the experience. She knows this will be the beginning of a long night."
    "Her first orgasm sends a shiver down her spine as she fills her date's mouth with her juices."

    show h atsu 21
    h "Ohhh that was amazing. I think you deserve a reward for that."

    show h atsu 22
    "After stripping her date and slipping a condom on him, Hazel lays on her back."
    h "Let's start out easy. Get on top of me. Now."
    "Hazel's date makes no delay in following this command. He lowers his hips gently but firmly, easily entering Hazel's body."
    h "Good boy. Now, make me cum."

    show h atsu 23
    "Without thinking, as if driven by animal instinct, the man ensures his member rubs past every square inch of Hazel's insides. He is driven not by his own need to orgasm, but by a desire to see hers."

    show h atsu 24
    "Pounding into her, he is able to excite her clit at the end of every deep thrust. Hazel's eyes roll back into her head."
    h "Yes, oh god yes!"
    "With one last convulsion, Hazel claims another orgasm, then relaxes her body with her date still deep within her."

    show h atsu 25
    h "That was exactly what I needed... And we're not done yet."

    show h atsu 26a
    "Without a word, Hazel moves herself out from under her partner. Giving him a coy look, she grabs one of the straps on her nighty."

    show h atsu 26b
    "With a small tug, she pulls the strap down, exposing her gorgeous breasts. Her smile widens as she sees the effect this has on her partner's member."

    show h atsu 26c
    "Without much more effort, Hazel removes the nighty entirely, leaving herself completely in the nude. Her body exudes confidence and sexuality in this pose."
    h "Like what you see? Well, let's continue, shall we?"

    show h atsu 27
    "Hazel and her date continue on for the rest of the evening. Hazel giving instructions, and the man following every one of them."
    "The man enjoys every second. So much so that he never notices that it's impossible for him to orgasm. Unknowingly, Hazel is doing the bidding of the Dark Sisterhood, draining the energy of this man."

    show h atsu 28
    "Of course, she ensures he has enough energy to fulfill her desires still, but she is draining him none the less."
    "With the man all but completely drained, it seems Hazel's appetite has finally been sated."

    show h atsu 29
    h "What a good boy you are. We'll have to do this again. Is tomorrow too soon?"
    "The man can barely muster a groan before falling unconcious."
    h "Heh, fine, you can sleep here tonight. All the better to get to work tomorrow."

label ch02_sunday_hq:
    scene bg hq
    "After a short weekend, the Justiciars returned to work, like any normal day. Although it would end up being anything but normal."

    show z atsu 01
    z "Hey Kaede! How was your weekend?"
    k "Hey Zoe! It was great. I mostly just snuggled up with a good book and some hot tea. How about..."
    "But before she could finish, two familiar faces pass them by, exiting Director Chisato's office."

    show z atsu 02
    s "Hey Kaede! Hey Zoe! You two should come down to the salon!"
    h "That's right! We're giving out free makeovers, so you should come before the line gets long!"

    k "Oh my! Sumire? Hazel? What's gotten into you two?"
    s "Not much. Oh, but we did just quit the Justiciar Force to be full-time makeup artists!"
    h "Yup, we just found our true calling. Anyway, see you two later!"

    show z atsu 03
    "Sumire and Hazel leave as quickly as they arrived. Zoe and Kaede stand in stunned silence for a few moments until the air is cleared by a voice from the next room."
    c "Kaede, Zoe, get in here!"
    "Kaede and Zoe snap out of their stupor and rush into the director's office."

    show z atsu 04
    c "Do either of you know what has gotten into those two? They waltzed in here early, said they both quit to follow their dreams of being makeup artists, then walked right out."
    z "Sorry boss, we're as surprised as you. This is weird. Think we should follow them?"
    c "Yes. You two go first. I'll call Maika and Yukino. They were already in the middle of a call, so they'll meet you there when they wrap up."
    k "Aye aye, captain."

label ch02_sunday_street:
    scene bg street
    show z atsu 05
    m "Hey, Yukino, we've got a message from the director. Says we need to rendezvous with Kaede and Zoe at some salon downtime."
    k "Salon? Are they trying to find new ways to get out of paying us our annual bonus?"
    m "No, she said something about Sumire and Hazel acting weird and... resigning? She sent Kaede and Zoe after them and we're supposed to meet up there."

    show z atsu 06
    k "What? Them? Resigning? That is weird. Alright, lead on."

label ch02_sunday_salon:
    scene bg salon entrance
    "By the time Maika and Yukino arrive, the main room of the salon is empty."
    show z atsu 07
    m "I hear something in the back, let's go, but stay quiet."

    scene bg salon back
    show z atsu 08
    "Sneaking into the back, the two heroines peek around the corner and notice three figures standing, and two seating in chairs."

    show z atsu 09a
    h "Another satisfied customer!"
    s "I'm so glad you two decided to come join us!"
    show z atsu 09b with dissolve_2
    "To Maika and Yukino's shock, they recognize Sumire and Hazel standing in beautician uniforms, and Kaede and Zoe sitting in the chairs wearing gaudy makeup."

    scene bg salon entrance
    show z atsu 10
    y "What the hell? It's like that makeup is hypnotizing them. I'm guessing that woman we don't know is the culprit."
    y "What's the play, cap?"
    menu:
        "Run straight for the beautician and try to defeat her":
            jump ch02_sunday_salon_badend
        "Find the source of the hypnosis":
            jump ch02_sunday_salon_goodend

label ch02_sunday_salon_badend:
    show z atsu 11
    m "We don't have much time. We have to rush in there and incapacitate their leader. It's the only way to save our friends."

    scene bg salon back
    show z atsu bad 01
    "Maika and Yukino rush into the room, ready for a fight."
    m "Stop it right there! You've done enough damage to our friends, now it's time to pay!"
    atsu "Finally, the last two have arrived. As you can see you're too late. Wouldn't you prefer to join your friends instead?"
    h "Yeah Maika! We're having so much fun!"
    s "That's right! Mistress has taught us the joy of makeovers!"

    y "I hate to say it, but I think we may have to fight past Sumire and Hazel."
    m "I think you're right. Oh, I hope they can forgive us!"
    atsu "Fine, if it's come to a fight..."
    show z atsu bad 02 with dissolve_2
    atsu "Then a fight you'll get. Right ladies?"
    show z atsu bad 03 with dissolve_2
    h "Yes mistress!"
    y "Of course, a minion from the Dark Sisterhood. It all makes sense now. Sorry ladies, this is going to hurt you a lot more than it'll hurt me."

    show z atsu bad 04
    "Maika and Yukino are able to make quck work of their hypnotized friends, leaving the beautician vulnerable."

    show z atsu bad 05
    m "It's over. Free our friends and we might let you go."
    atsu "I would, but it seems your friends can't seem to let *you* go."

    jump ch02_sunday_salon_badend_sitdown

label ch02_sunday_salon_badend_sitdown:
    show z atsu bad 06
    "In a moment of complete surprise, Maika and Yukino feel themselves get grabbed by the shoulders and shoved down into one of the salon's couches."
    "Speechless, they can't understand how they were bested."
    show z atsu bad 07
    "Looking up, they see Zoe and Kaede wearing the same outfit as the villain and her converted thralls."
    atsu "I'm afraid you forgot about my most recent employees. I'm glad they finally came to just in time to protect me."

    show z atsu bad 08
    atsu "You two seem to have the strongest wills of any of your comrades. The scent in the salon and the comfort of the couch seem to barely affect you."
    atsu "That's what's going to make this so much fun. I think I'll start with the yellow one. That way Little Miss Leader can watch the consequences of her failure."
    y "Pff, I'd like to see you try."
    atsu "Perfect, then it's time to begin!"

    show z atsu bad 09
    "The beautician jumps into action almost immediately. Yukino serving as another canvas for her to paint."
    m "You get the hell off of her! Yukino!"
    y "Don't worry chief, whatever she's doing here is pointless."
    atsu "Now now, you mustn't talk or things will smudge and this will take twice as long."
    "Maika struggles against her captor, but her energy is now drained by the perfume permeating the salon and the couch she has been firmly sat into."
    "She knows at this point her struggles are pointless as she feels the energy continue to leave her body."

    show z atsu bad 10a
    atsu "All done. Another perfect piece of art, don't you think?"
    show z atsu bad 10b with dissolve_2
    "Maika's jaw drops seeing Yukino's transformation. The beautician was right about one thing. Her body washes over with guilt, knowing she made the wrong call and sealed Yukino to this fate."

    show z atsu bad 11
    atsu "Oh your face is priceless!"
    m "What have you done to her? To all of them?"
    atsu "It's simple really. I've filled them with an adoration of makeup, and the drive to give this gift to others."
    atsu "Along the way, they'll help me drain energy from humans for my Dark Sisters, and we'll be able to take over this world!"

    show z atsu bad 12
    atsu "Now enough exposition, I'm glad I saved the best for last."
    jump ch02_sunday_salon_badend_hq

label ch02_sunday_salon_badend_hq:
    scene bg hq
    "Later, back at HQ."
    show z atsu bad 13
    "*Knock knock knock*"
    c "Come in."
    m "Reporting back, captain!"
    show z atsu bad 14
    c "Great, all good news, I hope?"
    show z atsu bad 15
    m "Yes, in fact, excellent news! We found Sumire and Hazel, and they gave us all makeovers!"
    m "And we were able to convince them to come back to the Justiciars! We were thinking we can still give makeover here. In fact, with your blessing, we wanted to make that our primary business!"
    c "Maika! What, what's gotten into you!"
    show z atsu bad 16
    m "Chill out, Chisato! Mistress said you'd be like this. Luckily everyone is here to help convince you!"
    c "I can't believe what I'm hearing! We need to call for backup."
    m "Good idea. Come on in, ladies!"

    show z atsu bad 17a
    h "Come on captain, please?"
    s "We really want to turn Justiciar HQ into a salon!"
    c "Now now, ladies. We mustn't get hasty."
    m "Don't worry, we've thought this through. We even have new uniforms!"
    show z atsu bad 17b with dissolve_2
    m "Now it's time to get you into your uniform too!"
    show z with dissolve

    scene bg hq outside
    "Later that day..."
    show z atsu bad 18
    c "And that is why the Justiciar Sentai are refocusing our efforts on bringing beauty to the world."
    show z atsu bad 19
    c "I'm sure you can already see how we've brought beauty to our own ranks. And now we want to share it."
    show z atsu bad 20
    c "But do not worry. We are here for you, our citizens. Each one of my Justiciars is ready to pamper you."
    show z atsu bad 21
    c "Their unique skills will bring you unparalleled joy."
    show z atsu bad 22
    c "Their deft hands will make you feel better than you've ever felt before."
    show z atsu bad 23
    c "And of course, all of this is provided to the public, free of charge."
    show z atsu bad 24
    c "And best of all, we're open right now!"
    "The only thing louder than the applause was the thundering of feet as customers rapidly charged the new Justiciar salon."
    "With the Justiciars out of the way, and in fact helping steal energy from the human, it was not long until the Dark Sisterhood took over the world."
    "Chapter 02 Bad End"
    return


label ch02_sunday_salon_goodend:
    show z atsu 11
    m "There's five of them, they'll overpower us. We have to find the source of the hypnosis."
    y "I'm guessing it's whatever is making this smell. Let's track it through the vents."

    show z atsu g 01
    "Yukino and Maika climb up into the spacious vents, following the flow of air further into the building."
    y "The fan is getting pretty loud. We have to be getting close."

    show z atsu g 02
    "Turning one last corner, Yukino spots a glowing pink device."
    y "Eureka, that's it!"

    show z atsu g 03
    m "Great, we found it. But now what?"

    menu:
        "Break it":
            jump ch02_sunday_salon_goodend_break
        "Study it":
            jump ch02_sunday_salon_goodend_study

label ch02_sunday_salon_goodend_break:
    y "We have to break it! With it gone, we'll surely get our friends back."
    show z atsu g 04
    "Grasping the object, Yukino pulls and pushes at every angle, trying to destroy the object in their confined space."
    "Despite her might, Yukino only manages to rattle the ventilation around her."

    show z atsu g 05
    m "Yukino, stop... Do you hear something?"
    y "Yeah, something squeaking?"

    show z atsu g 06
    "With a crash, the vent separates from the section in front of it. Yukino's banging finally did something, albeit not what she expected."
    jump ch02_sunday_salon_goodend_break2

label ch02_sunday_salon_goodend_study:
    y "Let's take a look at it. Everything has a weak spot."
    "Inspecting the object, it seems as tough as steel.  But the heart design does draw some attention."
    m "I'm wondering if that little heart is the key."
    "Suddenly, the two women notice the sound of metal straining beneath them. It was only a matter of time until the vents gave way under their weight."

    show z atsu g 06
    "With a crash, the vent separates from the section in front of it."
    jump ch02_sunday_salon_goodend_break2

label ch02_sunday_salon_goodend_break2:
    y "The device!"
    m "Grab it!"

    show z atsu g 07
    "Yukino reaches out, grabbing the device midair.  Within a split second, she has another idea of what to do."

    scene black
    show z atsu g 08
    "Conveniently, the villainous beautician stood directly below, carousing with Yukino's converted comrades."
    "The villain was the only one with enough mental clarity to notice the ventilation system collapsing, but ultimately she noticed too late."

    scene bg salon
    show z atsu g 09
    y "Boom, bitch!"
    "Not having enough time to think of a better line, Yukino slams the device into the villain's cranium."
    show sparkle z atsu
    "The device and villain both begin glowing, sparking out, then disappear."

    hide sparkle
    show z atsu g 10
    "With the villain defeated, the only thing left to do was fall face-first onto the ground."

label ch02_goodend:
    scene bg hq
    "An hour later, back at HQ."
    show z atsu g 11
    c "Great job you two. That was almost a complete defeat. What was the trick?"
    y "Smashing her in the head."
    m "And I couldn't think of anyone better to do it than Yukino."
    c "Simple. I like it."

    show z atsu g 12
    c "Now, for the rest of you. What did we learn?"

    scene bg hq
    show s shame 01
    s "A cosmetics deal that seems too good to be true probably is."
    show h shame 01
    h "When a teammate looks and acts strange, report it immediately and bring them to HQ."
    show k shame 01
    k "Always wait for backup when entering enemy territory."
    show z shame 01
    z "Don't sit on the comfy couch when inside enemy territory."

    scene bg hq
    show z atsu g 12
    c "Perfect. You all are dismissed."

    show z atsu g 13
    s "Wait, Hazel, what happened on that blind date?"
    h "Oh uh, err, we, uhh. It went well."
    s "Are you going to call him?"
    h "Uhh, yeah, probably."
    show z atsu g 14
    h "Well, I guess he's probably still at my apartment, since he said he couldn't walk after, you know."
    show z atsu g 15
    window hide
    pause
    show z atsu g 15b
    pause
    show z atsu g 16
    s "Hell yeah."
    show z atsu g 16 with dissolve:
        matrixcolor SaturationMatrix(0)
    "End of Chapter 1."
    jump ch03_start
