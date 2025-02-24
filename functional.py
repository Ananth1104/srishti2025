groups = {
    'A': range(1, 12),
    'B': range(12, 23),
    'C': range(23, 34),
    'D': range(34, 45),
    'E': range(45, 57)
}


paths = {
    1: [9, 8, 4, 3, 5, 6, 7, 1, 2, 10],
    2: [2, 6, 7, 1, 8, 4, 9, 5, 3, 10],
    3: [8, 5, 6, 3, 2, 1, 4, 7, 9, 10],
    4: [5, 9, 7, 6, 2, 1, 4, 3, 8, 10],
    5: [3, 6, 7, 4, 2, 9, 8, 1, 5, 10],
    6: [4, 1, 8, 2, 3, 6, 7, 5, 9, 10],
    7: [3, 2, 1, 6, 5, 7, 4, 9, 8, 10],
    8: [2, 6, 4, 5, 9, 3, 7, 1, 8, 10],
    9: [3, 5, 6, 9, 4, 2, 1, 7, 8, 10],
    10: [5, 2, 6, 1, 8, 7, 4, 3, 9, 10],
    11: [1, 9, 4, 5, 6, 3, 2, 8, 7, 10],
    12: [6, 3, 1, 5, 9, 2, 4, 7, 8, 10]
}

hints = {
    'A': [
        "Spotify’s steel butterfly.",  
        "The best place for those who can spring—beware, or you'll get a pulled hamstring.",  
        "Motoamrita's vehicle in 2000 BCE.",  
        "This angry widower rests on ignorance; the world trembles in his turbulence.",  
        "The best student guides the best of our students.",  
        "Profits off of your insecurities.",  
        "The iconic duo nests with grace, but alas, you must walk with haste.",  
        "Green metal does not lead to a green dot.",  
        "Mitochondria of the campus.",  
        "Onion on top and onion in the belly—come for all talks, serious or silly."
    ],
    'B': [
        "Spotify’s steel butterfly QR.",  
        "No one likes a hit to the elbow—if you do it, I'll think you're a foul fellow.",  
        "I was an instrument in Karna's hamartia, but now I've long retired from militia.",  
        "Sagan may have convinced y'all that my twin is the coolest, but hey, you know I am the hottest ;)",  
        "A twisted time led to a dire resort; my beloved friend became my son's consort.",  
        "You look like a broom facing certain doom. Come to my cool room, and there will be no more gloom.",  
        "I’m not a flower, yet I glide with ease; on waters calm, I dance with the breeze.",  
        "Here's your clue: The sea is blue, for omega-3 you must queue.",  
        "Painted silver, caging power. Find the danger sign on me within the hour.",  
        "You see a faceless embrace—enter, and your money has no interface."
    ],
    'C': [
        "Spotify Steel Butterfly.",  
        "In cricket if you do this, it would be tampering with the ball, but in this sport, you can pocket them all.",  
        "Over powered uber with 4HP.",  
        "Now I'm also near France cause a white man loved my dance.",  
        "A warrior torn between duty and kin, A hero to some, a doubt within. In the battle for what is right, I struggle between fate and fight.",  
        "I am hidden away, in a corner I am nestled. To reach me, you must not be crippled. You enter looking disheveled, you leave looking leveled.",  
        "I'm not a flower, yet I flit and flutter, in the water my wings do shudder with kicks. What am I?",  
        "I am neither the largest nor the smallest of my kind, but if you want the lifeless children of Gallus, I may come to mind.",  
        "Danger! Danger! Be aware of me. A 'shocking' revelation you shall feel!",  
        "12 hours I toil, an hour to breathe, at night's beckoning I open with ease."
    ],
    'D': [
        "Spotify Steel Butterfly.",  
        "A grave sin it is to be fake, but here it is a fair shot to make.",  
        "I am every warrior's prized possession, my pilots are offended if not appointed by succession. I protected a son of god and killed another, the saddest part was they had the same mother.",  
        "Metal rods that sing and rhyme, comes a gust of wind they chime.",  
        "I lost my son, a warrior, smart, strong, and fair. I then unleashed my wrath with a god as my charioteer.",  
        "When they want to be in a couple, the lads often try to build some muscle. Then they go visit 'purple' and walk out rather humble.",  
        "I share colour with a famous limit, but for you, I am off-limits.",  
        "Visit me and see the subjects of Triton, your tiring day will brighten.",  
        "I hum right across to Raaga. Touch me and your last words will be AAaaaHHHaaaAAAAAA.",  
        "Looks like a hut, closest thing to home. Friends, colleagues, lovers all under its dome."
    ],
    'E': [
        "Spotify Steel Butterfly.",  
        "A 'thin stream' of saliva incites disgust, but here it means your skills are robust.",  
        "These little caballī they can only dream, of what I was then ask brothers of Bheem.",  
        "Surrounded by silos of harvest, three steps to my raging tempest. You know me better for protection I offer with a divine downpour, but absolute destruction is also my chore.",  
        "This teacher took a very 'handy' payment. Find his star student, whose aim caused his enemies' bereavement.",  
        "You have probably seen me before, Chennai Mumbai and Mysore. With high expectations, you walk through my door. Once you're out, your look they shall adore.",  
        "My name is Lakshmi but I host the vessels of Saraswati.",  
        "Heated conversations under a shed, swirling turbine vents to cool your head.",  
        "I'm caged in painted silver, for your safety. Do not get too close, well you can but maintain distance plenty.",  
        "A little pink bud that looks typical, under its shelter exist layers; one private, another congregational."
    ]
}


def get_next_location(chest_number: str, current_location: int):
    chest_number = chest_number.upper()
    group = chest_number[0]
    if group not in "ABCDE":
        return "Invalid group!"
    
    try:
        team_index = int(chest_number[1:])  
    except ValueError:
        return "Invalid team number!"

    if group in "ABCD":
        team_num = ((team_index - 1) % 11) + 1  
    else:  
        if team_index < 1 or team_index > 12:
            return "Invalid team number!"
        team_num = team_index  
    
    path = paths.get(team_num, [])
    if not path:
        return "Invalid path for this team!"

    if current_location == 0:
        next_location = path[0]
    else:
        try:
            current_index = path.index(current_location)
            next_location = path[current_index + 1]
        except (ValueError, IndexError):
            return "No next location. You might have reached the end!"
    
    try:
        hint = hints[group][next_location - 1]  
    except IndexError:
        return "No hint available for this location!"
    
    return f"Hint: {hint}"

if __name__ == "__main__":
    chest_number = input("Enter chest number (e.g., A7): ")
    try:
        current_location = int(input("Enter current location (0-9): "))
    except ValueError:
        print("Invalid location input! Must be a number between 0 and 9.")
    else:
        result = get_next_location(chest_number, current_location)
        print(result)