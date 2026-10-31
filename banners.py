#banners.py
# 'chance' values are WEIGHTS, not strict percentages. random.choices() normalizes them.
# Right now they add up to 100, so they also read as percentages.
tiers = {
    '9s': {
        'chance': 0.6,
        'chars': {
            'Sukuna': {'desc': "The Main Antagonist of Jujutsu Kaisen. He is from the Heian Era"},
            'Gojo Satoru': {'desc': "The strongest Jujutsu Sorcerer. Wields Limitless and the Six Eyes"},
            'Satella': {'desc': "The Witch of Envy from Re:Zero. Her shadow looms over everything"},
            'Flugel': {'desc': "The Great Sage of Re:Zero. A legend whose legacy still shapes the world"},
            'Saitama': {'desc': "The hero of One Punch Man. Ends every fight with a single punch and is bored by it"},
            'Rimuru Tempest': {'desc': "A reincarnated slime from That Time I Got Reincarnated as a Slime. Founded a nation of monsters"},
            'Ainz Ooal Gown': {'desc': "The undead overlord of Overlord. Rules the Great Tomb of Nazarick"},
            'Madara Uchiha': {'desc': "A legendary Uchiha from Naruto. Rival of the First Hokage and wielder of the Rinnegan"}
        }
    },
    '7s': {
        'chance': 1.4,
        'chars': {
            'Subaru': {'desc': 'The Main Character from Re:Zero. Main Ability is Return By Death'},
            'Reinhard': {'desc': "The Sword Saint of Re:Zero. Blessed with the Divine Protections of countless gods"},
            'Itachi Uchiha': {'desc': "The prodigy of the Uchiha clan in Naruto. Carried a burden no one else knew"},
            'Goku': {'desc': "The Saiyan raised on Earth in Dragon Ball. Never stops chasing a stronger opponent"},
            'Monkey D. Luffy': {'desc': "The rubber-bodied captain of the Straw Hat Pirates in One Piece. Wants to be Pirate King"},
            'Roronoa Zoro': {'desc': "The three-sword fighter of the Straw Hat Pirates. Famously terrible with directions"},
            'Naruto Uzumaki': {'desc': "The Hokage-dreaming ninja of Naruto. Carries the Nine-Tails inside him"},
            'Light Yagami': {'desc': "The student from Death Note who finds a notebook that kills. Believes he can build a new world"},
            'Lelouch vi Britannia': {'desc': "The exiled prince of Code Geass. Commands people with the power of Geass"},
            'Edward Elric': {'desc': "The Fullmetal Alchemist. Lost an arm and a leg to alchemy and keeps going"},
            'Vegeta': {'desc': "The Prince of all Saiyans in Dragon Ball. Pride is both his strength and his weakness"},
            'Spike Spiegel': {'desc': "The laid-back bounty hunter of Cowboy Bebop. Always looks like he has nowhere to be"}
        }
    },
    '5s': {
        'chance': 4,
        'chars': {
            'Rudeus': {'desc': 'The Main Character from Mushoku Tensei. Questionable character but his growth is quite well-written'},
            'Emilia': {'desc': "The half-elf candidate for the throne in Re:Zero. Kind to a fault"},
            'Levi Ackerman': {'desc': "Humanity's strongest soldier in Attack on Titan. Obsessed with cleanliness"},
            'Anya Forger': {'desc': "The telepath of SpyXFamily. Loves peanuts and has no idea how much she knows"},
            'Mikasa Ackerman': {'desc': "A skilled soldier in Attack on Titan. Fiercely protective of the people she cares about"},
            'Eren Yeager': {'desc': "The protagonist of Attack on Titan. Driven by an unrelenting desire for freedom"},
            'Tanjiro Kamado': {'desc': "The kind-hearted demon slayer of Demon Slayer. Fights to cure his sister"},
            'Nezuko Kamado': {'desc': "Tanjiro's younger sister in Demon Slayer. A demon who still protects humans"},
            'Zenitsu Agatsuma': {'desc': "A demon slayer in Demon Slayer. Cowardly when awake, terrifying when asleep"},
            'Inosuke Hashibira': {'desc': "A boar-masked demon slayer in Demon Slayer. Fights with two jagged blades and endless confidence"},
            'Izuku Midoriya': {'desc': "The protagonist of My Hero Academia. Inherited One For All from All Might"},
            'Katsuki Bakugo': {'desc': "The explosive classmate in My Hero Academia. Never settles for second place"},
            'Shoto Todoroki': {'desc': "A My Hero Academia student with fire and ice powers. Learned to accept both halves of himself"},
            'Yuji Itadori': {'desc': "The protagonist of Jujutsu Kaisen. Swallowed Sukuna's finger and became his vessel"},
            'Megumi Fushiguro': {'desc': "A Jujutsu Kaisen sorcerer who summons shikigami through the Ten Shadows technique"},
            'Nobara Kugisaki': {'desc': "A Jujutsu Kaisen sorcerer who fights with a hammer, nails and a straw doll"},
            'Kakashi Hatake': {'desc': "The copy ninja of Naruto. Team 7's teacher and owner of the Sharingan"},
            'Sasuke Uchiha': {'desc': "The Uchiha survivor of Naruto. Naruto's closest rival"}
        }
    },
    '4s': {
        'chance': 10,
        'chars': {
            'Denji': {'desc': "The chainsaw-powered hero of Chainsaw Man. Dreams of a simple, normal life"},
            'Power': {'desc': "The Blood Fiend of Chainsaw Man. Loud, selfish and strangely loyal"},
            'Aki Hayakawa': {'desc': "A devil hunter in Chainsaw Man. Calm on the surface, driven underneath"},
            'Makima': {'desc': "The Public Safety agent of Chainsaw Man. Polite, powerful and never what she seems"},
            'Asta': {'desc': "The magic-less protagonist of Black Clover. Trains relentlessly to become Wizard King"},
            'Yuno': {'desc': "Asta's rival in Black Clover. Gifted with a four-leaf clover grimoire"},
            'Natsu Dragneel': {'desc': "The Fire Dragon Slayer of Fairy Tail. Motion sickness is his true enemy"},
            'Lucy Heartfilia': {'desc': "The celestial spirit mage of Fairy Tail. Opens gates to summon her spirits"},
            'Erza Scarlet': {'desc': "The armored mage of Fairy Tail known as Titania. Feared by friends and foes alike"},
            'Gray Fullbuster': {'desc': "The ice-make mage of Fairy Tail. Has a habit of losing his clothes"},
            'Killua Zoldyck': {'desc': "A former assassin in Hunter x Hunter. Gon's best friend"},
            'Gon Freecss': {'desc': "The cheerful hunter-in-training of Hunter x Hunter. Searches for his father"},
            'Kurapika': {'desc': "The last of the Kurta clan in Hunter x Hunter. Hunts the Phantom Troupe"},
            'Hisoka': {'desc': "The unpredictable magician of Hunter x Hunter. Fights for the thrill of it"},
            'Rei Ayanami': {'desc': "The quiet pilot of Neon Genesis Evangelion. Pilots Unit-00"},
            'Asuka Langley': {'desc': "The fiery pilot of Neon Genesis Evangelion. Pilots Unit-02 and refuses to lose"},
            'Shinji Ikari': {'desc': "The reluctant pilot of Neon Genesis Evangelion. Pilots Unit-01"},
            'Mob': {'desc': "The psychic middle schooler of Mob Psycho 100. Holds enormous power and tries to stay calm"},
            'Violet Evergarden': {'desc': "The former soldier of Violet Evergarden. Writes letters while learning what feelings mean"},
            'Misato Katsuragi': {'desc': "The operations director of NERV in Neon Genesis Evangelion. Loves her beer"}
        }
    },
    '3s': {
        'chance': 18,
        'chars': {
            'Loid': {'desc': "Anya's Father in SpyXFamily. The greatest spy from Westalis. Works for WISE."},
            'Julius': {'desc': "A knight and spirit user from Re:Zero. Polished, proud and dangerous"},
            'Rem': {'desc': "The devoted maid from Re:Zero. Famous for her morning star and her loyalty"},
            'Armin Arlert': {'desc': "A strategist in Attack on Titan. Wins with ideas more than strength"},
            'Erwin Smith': {'desc': "The Survey Corps commander in Attack on Titan. Asks others to give their hearts"},
            'Hange Zoe': {'desc': "A Survey Corps squad leader in Attack on Titan. Obsessed with Titans"},
            'Sakura Haruno': {'desc': "A medical ninja of Naruto. Packs a monstrous punch"},
            'Hinata Hyuga': {'desc': "The Byakugan-wielding kunoichi of Naruto. Admired Naruto for years"},
            'Rock Lee': {'desc': "The taijutsu specialist of Naruto. Cannot use ninjutsu and outworks everyone anyway"},
            'Shikamaru Nara': {'desc': "The genius strategist of Naruto. Finds everything troublesome"},
            'Might Guy': {'desc': "The green-clad taijutsu master of Naruto. Rock Lee's sensei"},
            'Jiraiya': {'desc': "The Toad Sage of Naruto. Naruto's teacher and a legendary Sannin"},
            'Tsunade': {'desc': "The Fifth Hokage of Naruto. A legendary Sannin and medical ninja"},
            'Nami': {'desc': "The navigator of the Straw Hat Pirates. Loves treasure and reads the weather like a book"},
            'Usopp': {'desc': "The sniper of the Straw Hat Pirates. A proud, anxious storyteller"},
            'Sanji': {'desc': "The cook of the Straw Hat Pirates. Fights using only his legs"},
            'Nico Robin': {'desc': "The archaeologist of the Straw Hat Pirates. Can sprout limbs anywhere"},
            'Tony Tony Chopper': {'desc': "The doctor of the Straw Hat Pirates. A reindeer who ate a Devil Fruit"},
            'Franky': {'desc': "The shipwright of the Straw Hat Pirates. Rebuilt himself as a cyborg"},
            'Brook': {'desc': "The musician of the Straw Hat Pirates. A living skeleton with a love for music"},
            'Portgas D. Ace': {'desc': "Luffy's older brother in One Piece. Wields fire"}
        }
    },
    '2s': {
        'chance': 26,
        'chars': {
            'Yor': {'desc': "Anya's Mother in SpyXFamily. An Assassin who works for the GARDEN"},
            'Ram': {'desc': "The sharp-tongued maid from Re:Zero. Rem's older twin"},
            'Bond': {'desc': "The Forger family dog in SpyXFamily. A very good boy with a very big secret"},
            'Beatrice': {'desc': "The guardian of the Forbidden Library in Re:Zero. A spirit with a sharp attitude"},
            'Puck': {'desc': "Emilia's cat-shaped great spirit in Re:Zero. Far stronger than he looks"},
            'Roswaal': {'desc': "The eccentric master of the mansion in Re:Zero. Rarely says what he really means"},
            'Otto Suwen': {'desc': "A merchant in Re:Zero. Can speak with animals"},
            'Garfiel Tinsel': {'desc': "A hot-headed fighter in Re:Zero. Guarded the Sanctuary"},
            'Crusch Karsten': {'desc': "A royal candidate in Re:Zero. A noble leader admired for her honor"},
            'Felt': {'desc': "A royal candidate in Re:Zero. A street kid with a sharp eye"},
            'Priscilla Barielle': {'desc': "A royal candidate in Re:Zero. Sees the world as bending to her will"},
            'Anastasia Hoshin': {'desc': "A royal candidate in Re:Zero. A merchant who counts every coin"},
            'Petra Leyte': {'desc': "A young maid in Re:Zero. Learns to be brave"},
            'Kazuma Satou': {'desc': "The adventurer of Konosuba. Gets by on luck and cunning"},
            'Aqua': {'desc': "The goddess of Konosuba. Very useful, very loud"},
            'Megumin': {'desc': "The arch-wizard of Konosuba. Can only cast Explosion"},
            'Darkness': {'desc': "The crusader of Konosuba. Takes every hit gladly"},
            'Kirito': {'desc': "The black swordsman of Sword Art Online. Wields two swords"},
            'Asuna Yuuki': {'desc': "The Flash of Sword Art Online. One of the best swordswomen in the game"},
            'Damian Desmond': {'desc': "Anya's classmate in SpyXFamily. Son of a powerful politician"},
            'Becky Blackbell': {'desc': "Anya's friend in SpyXFamily. Dreams of marrying rich"}
        }
    },
    '1s': {
        'chance': 40,
        'chars': {
            'Piccolo': {'desc': 'The true Aura Farmer'},
            'Krillin': {'desc': "Goku's best friend in Dragon Ball. Has been through more than anyone gives him credit for"},
            'Yamcha': {'desc': "A former desert bandit in Dragon Ball. Legendary for one very specific reason"},
            'Tien Shinhan': {'desc': "A three-eyed warrior in Dragon Ball. Often overshadowed by Saiyans"},
            'Chiaotzu': {'desc': "Tien's tiny friend in Dragon Ball. Has psychic powers"},
            'Master Roshi': {'desc': "The Turtle Hermit of Dragon Ball. A legendary martial arts teacher with questionable habits"},
            'Bulma': {'desc': "The genius inventor of Dragon Ball. Built the Dragon Radar"},
            'Chi-Chi': {'desc': "Goku's wife in Dragon Ball. Takes her son's studies very seriously"},
            'Yajirobe': {'desc': "A swordsman in Dragon Ball. Mostly cares about food"},
            'Oolong': {'desc': "A shapeshifting pig in Dragon Ball. Not very brave"},
            'Puar': {'desc': "A shapeshifting cat in Dragon Ball. Yamcha's loyal companion"},
            'Mr. Satan': {'desc': "The world champion of Dragon Ball. Believed by everyone to have beaten Cell"},
            'Konohamaru': {'desc': "The Third Hokage's grandson in Naruto. Looks up to Naruto"},
            'Choji Akimichi': {'desc': "A loyal ninja in Naruto. Powers up through his clan's techniques and snacks"},
            'Kiba Inuzuka': {'desc': "A ninja in Naruto who fights alongside his dog Akamaru"},
            'Shino Aburame': {'desc': "A bug-using ninja in Naruto. Quiet and analytical"},
            'Buggy the Clown': {'desc': "A pirate captain in One Piece. Fears nothing but gets lucky"},
            'Koby': {'desc': "A young marine in One Piece. Starts as a cabin boy and grows from there"},
            'Panda': {'desc': "A Jujutsu Kaisen student who is a mutated cursed corpse. Fights as a panda"},
            'Toge Inumaki': {'desc': "A Jujutsu Kaisen student who speaks in cursed speech. Mostly talks in rice ball ingredients"},
            'Maki Zenin': {'desc': "A Jujutsu Kaisen student. Excels with cursed tools despite having little cursed energy"}
        }
    }
}

if __name__ == '__main__':

    print(list(tiers[i]['chance'] for i in tiers))
