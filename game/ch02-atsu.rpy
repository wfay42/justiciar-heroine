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
            show h atsu 08
            "Before Hazel can even get out of the chair, the beautician sprays a hefty amount of perfume into her face."
            atsu "Now now. This is a place of relaxation! Come Miss Hazel, have a sit and let us do all the work."
        "Wait for now, knowing you'll talk about it later":
            h "I think I'll keep my job, and you should too! We'll talk about this later."
            atsu "A grand choice. Now please, sit back and relax."
            show h atsu 08
            "With that, the beautician gives a ginger spray of the perfume onto Hazel's face"
    show h atsu 09
    "Sitting back in the chair, Hazel has fallen victim to aroma of the perfume. All she can do now is sit back and enjoy the ride."

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
    scene bg street
    show h atsu 15
    "Hazel strolls, no, structs down the street with a newfound confidence. The nervous woman from the morning is gone, replaced by a stunning femme fatale."
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
    "After a short weekend, the Justiciars returned to work. Although it ended up being a strange day."
    z "Hey Kaede! How was your weekend?"
    k "Hey Zoe! It was great. I mostly just snuggled up with a good book and some hot tea. How about..."
    "But before she could finish, two familiar faces pass them by, exiting Director Chisato's office."

    s "Hey Kaede! Hey Zoe! You two should come down to the salon!"
    h "That's right! We're giving out free makeovers, so you should come before the line gets long!"

    k "Oh my! Sumire? Hazel? What's gotten into you two?"
    s "Not much. Oh, but we did just quit the Justiciar Force to be full-time makeup artists!"
    h "Yup, we just found our true calling. Anyway, see you two later!"
    "Sumire and Hazel leave as quickly as they arrived. Zoe and Kaede stand in stunned silence for a few moments until the air is cleared by a voice from the next room."

    c "Kaede, Zoe, get in here!"
    "Kaede and Zoe snap out of their stupor and rush into the director's office."
    c "Do either of you know what has gotten into those two? They waltzed in here early, said they both quit to follow their dreams of being makeup artists, then walked right out."
    z "Sorry boss, this is weird. Think we should follow them?"
    c "Yes. You two go first. I'll call Maika and Yukino. They were already in the middle of a call, so they'll meet you there when they wrap up."
    k "Aye aye, captain."

label ch02_sunday_street:
    scene bg street
    m "Hey, Yukino, we've got a message from the director. Says we need to rendezvous with Kaede and Zoe at some salon downtime."
    k "Salon? Are they trying to find new ways to get out of paying us our annual bonus?"
    m "No, she said something about Sumire and Hazel acting weird and... resigning? She sent Kaede and Zoe after them and we're supposed to meet up there."
    k "Alright, lead on."

label ch02_sunday_salon:
    scene bg salon
    "By the time Maika and Yukino arrive, the main room of the salon is empty."
    m "I hear something in the back, let's go, but stay quiet."

    "Sneaking into the back, the two heroines peek around the corner and notice three figures standing, and two seating in chairs."

    h "Another satisfied customer!"
    s "I'm so glad you two decided to come join us!"
    "To Maika and Yukino's shock, they recognize Sumire and Hazel standing in beautician uniforms, and Kaede and Zoe sitting in the chairs."




