#banners.py
#example of 1 system
tiers = {
    '9s': {
        'chance': 0.01,
        'chars': {
            'Sukuna': {'desc': "The Main Antagonist of Jujutsu Kaisen. He is from the Heian Era"},
            'Gojo Satoru': {'desc': "The strongest Jujutsu Sorcerer. Wields Limitless and the Six Eyes"},
            'Satella': {'desc': "The Witch of Envy from Re:Zero. Her shadow looms over everything"},
            'Flugel': {'desc': "The Great Sage of Re:Zero. A legend whose legacy still shapes the world"}
        }
    },
    '7s': {
        'chance': 0.2,
        'chars': {
            'Subaru': {'desc': 'The Main Character from Re:Zero. Main Ability is Return By Death'},
            'Reinhard': {'desc': "The Sword Saint of Re:Zero. Blessed with the Divine Protections of countless gods"},
            'Itachi Uchiha': {'desc': "The prodigy of the Uchiha clan in Naruto. Carried a burden no one else knew"},
            'Goku': {'desc': "The Saiyan raised on Earth in Dragon Ball. Never stops chasing a stronger opponent"}
        }
    },
    '5s': {
        'chance': 1,
        'chars': {
            'Rudeus': {'desc': 'The Main Character from Mushoku Tensei. Questionable character but his growth is quite well-written'},
            'Emilia': {'desc': "The half-elf candidate for the throne in Re:Zero. Kind to a fault"},
            'Levi Ackerman': {'desc': "Humanity's strongest soldier in Attack on Titan. Obsessed with cleanliness"},
            'Anya Forger': {'desc': "The telepath of SpyXFamily. Loves peanuts and has no idea how much she knows"}
        }
    },
    '3s': {
        'chance': 10,
        'chars': {
            'Loid': {'desc': "Anya's Father in SpyXFamily. The greatest spy from Westalis. Works for WISE."},
            'Julius': {'desc': "A knight and spirit user from Re:Zero. Polished, proud and dangerous"},
            'Rem': {'desc': "The devoted maid from Re:Zero. Famous for her morning star and her loyalty"}
        }
    },
    '2s': {
        'chance': 30,
        'chars': {
            'Yor': {'desc': "Anya's Mother in SpyXFamily. An Assassin who works for the GARDEN"},
            'Ram': {'desc': "The sharp-tongued maid from Re:Zero. Rem's older twin"},
            'Bond': {'desc': "The Forger family dog in SpyXFamily. A very good boy with a very big secret"}
        }
    },
    '1s': {
        'chance': 60,
        'chars': {
            'Piccolo': {'desc': 'The true Aura Farmer'},
            'Krillin': {'desc': "Goku's best friend in Dragon Ball. Has been through more than anyone gives him credit for"},
            'Yamcha': {'desc': "A former desert bandit in Dragon Ball. Legendary for one very specific reason"}
        }
    }
}

if __name__ == '__main__':

    print(list(tiers[i]['chance'] for i in tiers))
