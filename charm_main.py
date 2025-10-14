import random
from tkinter import *

#Made by Maximilian Jäger - https://github.com/MaximilianLJ
#Thanks to @Dtlnor
#Sheet 1 https://docs.google.com/spreadsheets/d/1QboeJMr66QGL9EZZ5fAmtP8boLVdBzXHk5JbjTJGghE/htmlview#gid=1599248570
#Sheet 2 https://docs.google.com/spreadsheets/u/0/d/1fpkamu1VzEpX8dZqecygW1GflKyvdY2975Y0d9SUt04/htmlview#gid=1054141820

#Updated for TU3

#All possible skill groups
skill_groups = {
    1: [
        {"skill": "Artillery", "level": 1},
        {"skill": "Attack Boost", "level": 1},
        {"skill": "Ballistics", "level": 1},
        {"skill": "Blast Attack", "level": 1},
        {"skill": "Bludgeoner", "level": 1},
        {"skill": "Charge Master", "level": 1},
        {"skill": "Critical Draw", "level": 1},
        {"skill": "Critical Element", "level": 1},
        {"skill": "Critical Eye", "level": 1},
        {"skill": "Critical Status", "level": 1},
        {"skill": "Dragon Attack", "level": 1},
        {"skill": "Fire Attack", "level": 1},
        {"skill": "Focus", "level": 1},
        {"skill": "Guard", "level": 1},
        {"skill": "Guard Up", "level": 1},
        {"skill": "Handicraft", "level": 1},
        {"skill": "Horn Maestro", "level": 1},
        {"skill": "Ice Attack", "level": 1},
        {"skill": "Load Shells", "level": 1},
        {"skill": "Mind's Eye", "level": 1},
        {"skill": "Offensive Guard", "level": 1},
        {"skill": "Opening Shot", "level": 1},
        {"skill": "Paralysis Attack", "level": 1},
        {"skill": "Poison Attack", "level": 1},
        {"skill": "Power Prolonger", "level": 1},
        {"skill": "Protective Polish", "level": 1},
        {"skill": "Punishing Draw", "level": 1},
        {"skill": "Rapid Morph", "level": 1},
        {"skill": "Razor Sharp", "level": 1},
        {"skill": "Sleep Attack", "level": 1},
        {"skill": "Slugger", "level": 1},
        {"skill": "Special Ammo Boost", "level": 1},
        {"skill": "Speed Sharpening", "level": 1},
        {"skill": "Stamina Thief", "level": 1},
        {"skill": "Tetrad Shot", "level": 1},
        {"skill": "Thunder Attack", "level": 1},
        {"skill": "Water Attack", "level": 1},
    ],
    2: [
        {"skill": "Airborne", "level": 1},
        {"skill": "Artillery", "level": 2},
        {"skill": "Attack Boost", "level": 2},
        {"skill": "Ballistics", "level": 2},
        {"skill": "Blast Attack", "level": 2},
        {"skill": "Blast Functionality", "level": 1},
        {"skill": "Bludgeoner", "level": 2},
        {"skill": "Charge Master", "level": 2},
        {"skill": "Charge Up", "level": 1},
        {"skill": "Critical Draw", "level": 2},
        {"skill": "Critical Element", "level": 2},
        {"skill": "Critical Eye", "level": 2},
        {"skill": "Critical Status", "level": 2},
        {"skill": "Dragon Attack", "level": 2},
        {"skill": "Exhaust Functionality", "level": 1},
        {"skill": "Fire Attack", "level": 2},
        {"skill": "Focus", "level": 2},
        {"skill": "Guard", "level": 2},
        {"skill": "Guard Up", "level": 2},
        {"skill": "Handicraft", "level": 2},
        {"skill": "Horn Maestro", "level": 2},
        {"skill": "Ice Attack", "level": 2},
        {"skill": "Load Shells", "level": 2},
        {"skill": "Mind's Eye", "level": 2},
        {"skill": "Offensive Guard", "level": 2},
        {"skill": "Opening Shot", "level": 2},
        {"skill": "Paralysis Attack", "level": 2},
        {"skill": "Poison Attack", "level": 2},
        {"skill": "Poison Duration Up", "level": 2},
        {"skill": "Poison Functionality", "level": 1},
        {"skill": "Power Prolonger", "level": 2},
        {"skill": "Protective Polish", "level": 2},
        {"skill": "Punishing Draw", "level": 2},
        {"skill": "Rapid Morph", "level": 2},
        {"skill": "Razor Sharp", "level": 2},
        {"skill": "Sleep Attack", "level": 2},
        {"skill": "Slugger", "level": 2},
        {"skill": "Special Ammo Boost", "level": 2},
        {"skill": "Speed Sharpening", "level": 2},
        {"skill": "Stamina Thief", "level": 2},
        {"skill": "Tetrad Shot", "level": 2},
        {"skill": "Thunder Attack", "level": 2},
        {"skill": "Water Attack", "level": 2},
    ],
    
    3: [
        {"skill": "Artillery", "level": 3},
        {"skill": "Attack Boost", "level": 3},
        {"skill": "Ballistics", "level": 3},
        {"skill": "Blast Attack", "level": 3},
        {"skill": "Bludgeoner", "level": 3},
        {"skill": "Charge Master", "level": 3},
        {"skill": "Critical Draw", "level": 3},
        {"skill": "Critical Element", "level": 3},
        {"skill": "Critical Eye", "level": 3},
        {"skill": "Critical Status", "level": 3},
        {"skill": "Dragon Attack", "level": 3},
        {"skill": "Fire Attack", "level": 3},
        {"skill": "Focus", "level": 3},
        {"skill": "Guard", "level": 3},
        {"skill": "Guard Up", "level": 3},
        {"skill": "Handicraft", "level": 3},
        {"skill": "Ice Attack", "level": 3},
        {"skill": "Master's Touch", "level": 1},
        {"skill": "Mind's Eye", "level": 3},
        {"skill": "Normal Shots", "level": 1},
        {"skill": "Offensive Guard", "level": 3},
        {"skill": "Opening Shot", "level": 3},
        {"skill": "Para Functionality", "level": 1},
        {"skill": "Paralysis Attack", "level": 3},
        {"skill": "Piercing Shots", "level": 1},
        {"skill": "Poison Attack", "level": 3},
        {"skill": "Power Prolonger", "level": 3},
        {"skill": "Protective Polish", "level": 3},
        {"skill": "Punishing Draw", "level": 3},
        {"skill": "Rapid Fire Up", "level": 1},
        {"skill": "Rapid Morph", "level": 3},
        {"skill": "Razor Sharp", "level": 3},
        {"skill": "Sleep Attack", "level": 3},
        {"skill": "Sleep Functionality", "level": 1},
        {"skill": "Slugger", "level": 3},
        {"skill": "Spread/Power Shots", "level": 1},
        {"skill": "Stamina Thief", "level": 3},
        {"skill": "Tetrad Shot", "level": 3},
        {"skill": "Thunder Attack", "level": 3},
        {"skill": "Water Attack", "level": 3},
    ],
    4: [
        {"skill": "Attack Boost", "level": 2},
        {"skill": "Ballistics", "level": 2},
        {"skill": "Blast Attack", "level": 2},
        {"skill": "Critical Boost", "level": 1},
        {"skill": "Critical Element", "level": 2},
        {"skill": "Critical Eye", "level": 2},
        {"skill": "Dragon Attack", "level": 2},
        {"skill": "Fire Attack", "level": 2},
        {"skill": "Guard", "level": 2},
        {"skill": "Guard Up", "level": 2},
        {"skill": "Handicraft", "level": 2},
        {"skill": "Ice Attack", "level": 2},
        {"skill": "Opening Shot", "level": 2},
        {"skill": "Paralysis Attack", "level": 2},
        {"skill": "Poison Attack", "level": 2},
        {"skill": "Protective Polish", "level": 2},
        {"skill": "Razor Sharp", "level": 2},
        {"skill": "Sleep Attack", "level": 2},
        {"skill": "Tetrad Shot", "level": 2},
        {"skill": "Thunder Attack", "level": 2},
        {"skill": "Water Attack", "level": 2},
    ],
    5: [
        {"skill": "Adaptability", "level": 1},
        {"skill": "Antivirus", "level": 1},
        {"skill": "Aquatic/Oilsilt Mobility", "level": 1},
        {"skill": "Bind Resistance", "level": 1},
        {"skill": "Blast Resistance", "level": 1},
        {"skill": "Bleeding Resistance", "level": 1},
        {"skill": "Bombardier", "level": 1},
        {"skill": "Botanist", "level": 1},
        {"skill": "Constitution", "level": 2},
        {"skill": "Defense Boost", "level": 2},
        {"skill": "Divine Blessing", "level": 1},
        {"skill": "Dragon Resistance", "level": 1},
        {"skill": "Fire Resistance", "level": 1},
        {"skill": "Flinch Free", "level": 1},
        {"skill": "Free Meal", "level": 1},
        {"skill": "Geologist", "level": 1},
        {"skill": "Hunger Resistance", "level": 1},
        {"skill": "Ice Resistance", "level": 1},
        {"skill": "Intimidator", "level": 1},
        {"skill": "Iron Skin", "level": 1},
        {"skill": "Item Prolonger", "level": 1},
        {"skill": "Marathon Runner", "level": 1},
        {"skill": "Paralysis Resistance", "level": 1},
        {"skill": "Poison Resistance", "level": 1},
        {"skill": "Quick Sheathe", "level": 1},
        {"skill": "Recovery Speed", "level": 1},
        {"skill": "Recovery Up", "level": 1},
        {"skill": "Sleep Resistance", "level": 1},
        {"skill": "Speed Eating", "level": 1},
        {"skill": "Stench Resistance", "level": 1},
        {"skill": "Stun Resistance", "level": 1},
        {"skill": "Survival Expert", "level": 1},
        {"skill": "Thunder Resistance", "level": 1},
        {"skill": "Tremor Resistance", "level": 1},
        {"skill": "Water Resistance", "level": 1},
        {"skill": "Wide-Range", "level": 2},
        {"skill": "Windproof", "level": 1},
    ],
    6: [
        {"skill": "Adaptability", "level": 2},
        {"skill": "Antivirus", "level": 2},
        {"skill": "Aquatic/Oilsilt Mobility", "level": 2},
        {"skill": "Bind Resistance", "level": 2},
        {"skill": "Blast Resistance", "level": 2},
        {"skill": "Bleeding Resistance", "level": 2},
        {"skill": "Bombardier", "level": 2},
        {"skill": "Botanist", "level": 2},
        {"skill": "Constitution", "level": 3},
        {"skill": "Defense Boost", "level": 3},
        {"skill": "Divine Blessing", "level": 2},
        {"skill": "Dragon Resistance", "level": 2},
        {"skill": "Fire Resistance", "level": 2},
        {"skill": "Flinch Free", "level": 2},
        {"skill": "Free Meal", "level": 2},
        {"skill": "Geologist", "level": 2},
        {"skill": "Hunger Resistance", "level": 2},
        {"skill": "Ice Resistance", "level": 2},
        {"skill": "Intimidator", "level": 2},
        {"skill": "Iron Skin", "level": 2},
        {"skill": "Item Prolonger", "level": 2},
        {"skill": "Marathon Runner", "level": 2},
        {"skill": "Paralysis Resistance", "level": 2},
        {"skill": "Poison Resistance", "level": 2},
        {"skill": "Quick Sheathe", "level": 2},
        {"skill": "Recovery Speed", "level": 2},
        {"skill": "Recovery Up", "level": 2},
        {"skill": "Sleep Resistance", "level": 2},
        {"skill": "Speed Eating", "level": 2},
        {"skill": "Stench Resistance", "level": 2},
        {"skill": "Stun Resistance", "level": 2},
        {"skill": "Survival Expert", "level": 2},
        {"skill": "Thunder Resistance", "level": 2},
        {"skill": "Tremor Resistance", "level": 2},
        {"skill": "Water Resistance", "level": 2},
        {"skill": "Wide-Range", "level": 3},
        {"skill": "Windproof", "level": 2},
    ],
    7: [
        {"skill": "Antivirus", "level": 3},
        {"skill": "Bind Resistance", "level": 3},
        {"skill": "Blast Resistance", "level": 3},
        {"skill": "Bleeding Resistance", "level": 3},
        {"skill": "Bombardier", "level": 3},
        {"skill": "Botanist", "level": 4},
        {"skill": "Constitution", "level": 4},
        {"skill": "Defense Boost", "level": 4},
        {"skill": "Divine Blessing", "level": 3},
        {"skill": "Dragon Resistance", "level": 3},
        {"skill": "Fire Resistance", "level": 3},
        {"skill": "Flinch Free", "level": 3},
        {"skill": "Free Meal", "level": 3},
        {"skill": "Geologist", "level": 3},
        {"skill": "Hunger Resistance", "level": 3},
        {"skill": "Ice Resistance", "level": 3},
        {"skill": "Intimidator", "level": 3},
        {"skill": "Iron Skin", "level": 3},
        {"skill": "Item Prolonger", "level": 3},
        {"skill": "Marathon Runner", "level": 3},
        {"skill": "Paralysis Resistance", "level": 3},
        {"skill": "Poison Resistance", "level": 3},
        {"skill": "Quick Sheathe", "level": 3},
        {"skill": "Recovery Speed", "level": 3},
        {"skill": "Recovery Up", "level": 3},
        {"skill": "Sleep Resistance", "level": 3},
        {"skill": "Speed Eating", "level": 3},
        {"skill": "Stun Resistance", "level": 3},
        {"skill": "Survival Expert", "level": 3},
        {"skill": "Thunder Resistance", "level": 3},
        {"skill": "Tremor Resistance", "level": 3},
        {"skill": "Water Resistance", "level": 3},
        {"skill": "Wide-Range", "level": 4},
        {"skill": "Windproof", "level": 3},
    ],
    8: [
        {"skill": "Ambush", "level": 1},
        {"skill": "Blight Resistance", "level": 1},
        {"skill": "Coalescence", "level": 1},
        {"skill": "Counterstrike", "level": 1},
        {"skill": "Earplugs", "level": 1},
        {"skill": "Evade Extender", "level": 1},
        {"skill": "Evade Window", "level": 2},
        {"skill": "Heroics", "level": 2},
        {"skill": "Maximum Might", "level": 1},
        {"skill": "Mushroomancer", "level": 1},
        {"skill": "Partbreaker", "level": 1},
        {"skill": "Peak Performance", "level": 1},
        {"skill": "Resentment", "level": 1},
        {"skill": "Stamina Surge", "level": 1},
        {"skill": "Tool Specialist", "level": 2},
    ],
    9: [
        {"skill": "Ambush", "level": 2},
        {"skill": "Blight Resistance", "level": 2},
        {"skill": "Coalescence", "level": 2},
        {"skill": "Counterstrike", "level": 2},
        {"skill": "Earplugs", "level": 2},
        {"skill": "Evade Extender", "level": 2},
        {"skill": "Evade Window", "level": 3},
        {"skill": "Heroics", "level": 3},
        {"skill": "Maximum Might", "level": 2},
        {"skill": "Mushroomancer", "level": 2},
        {"skill": "Partbreaker", "level": 2},
        {"skill": "Peak Performance", "level": 2},
        {"skill": "Resentment", "level": 2},
        {"skill": "Stamina Surge", "level": 2},
        {"skill": "Tool Specialist", "level": 3},
    ],
    10: [
        {"skill": "Adrenaline Rush", "level": 1},
        {"skill": "Agitator", "level": 1},
        {"skill": "Burst", "level": 1},
        {"skill": "Convert Element", "level": 1},
        {"skill": "Elemental Absorption", "level": 1},
        {"skill": "Flayer", "level": 1},
        {"skill": "Foray", "level": 1},
        {"skill": "Latent Power", "level": 1},
        {"skill": "Weakness Exploit", "level": 1},
    ]
}

#All Possible Slot combinations
slots = {
    1: "A1-0-0",
    2: "A1-A1-0",
    3: "A1-A1-A1",
    4: "A2-0-0",
    5: "A2-A1-0",
    6: "A3-0-0",
    11:"W1-0-0",
    12:"W1-A1-0",
    13:"W1-A1-A1"
}

#Drop rates by rarity
drop_rates = {
    "rarity5": 0.59,
    "rarity6": 0.27,
    "rarity7": 0.11,
    "rarity8": 0.03
}

#Tuples of all possible skill_group combos
possible_combos = {
    5: [(1,6,6), (1,7), (1,8,6), (1,8,8), (1,9), (1,10)],
    6: [(1,1,7), (1,1,10), (2,6,6), (2,8,6), (2,9), (2,10)],
    7: [(2,1,7), (2,1,8), (2,1,10), (3,6,5), (3,7), (3,8,5), (3,10), (4,1,1)],
    8: [(2,1,7), (2,1,8), (2,1,10), (3,6,5), (3,7), (3,8,5), (3,10), (4,1,1)],
}

def slot_assign(combo):
    #Assigns a random slot to the charm dependent on the skill combo
    if combo in [(1,6,6), (1,7), (1,8,6), (1,8,8), (1,9), (1,10)]: #Checks the tuple of the Charm
        possible_slots = [2, 4, 5, 6] #All possible slot IDs for that tuple
        return slots[random.choice(possible_slots)] #Chooses a random slot out of the possible ones
    
    elif combo in [(1,1,7), (1,1,10), (2,6,6), (2,8,6), (2,9), (2,10)]:
        possible_slots = [1, 2, 4, 5]
        return slots[random.choice(possible_slots)]
    
    elif combo == (2,1,8):
        possible_slots = [2, 4, 6]
        return slots[random.choice(possible_slots)]
    
    elif combo in [(2,1,7), (2,1,10), (3,6,5), (3,7), (3,8,5), (3,10), (4,1,1)]:
        possible_slots = [11, 12, 13]
        possible_slots_rarity = [0.5, 0.33, 0.17]
        return slots[random.choices(possible_slots, weights=possible_slots_rarity, k=1)[0]]
    
    else:
        raise ValueError(f"Unknown combo {combo}") 

def skill_assign(combo):
    #Assigns the skills for the combo tuple in the way that it can't have the same skill twice
    while True:
        skills = []
        seen = set()
        
        for skill in combo:
            #Check that prevents an example 1-6-6 Charm to roll the same skill from skill_group 6 twice
            pick = random.choice(skill_groups[skill])
            if pick["skill"] in seen:
                break
            skills.append(pick)
            seen.add(pick["skill"])
        
        else:
            return skills

def format_skills(skills):
    #Format -> "Agitator" : 1, "xyz" : int, [...]
    return ", ".join(f"{s['skill']} : {s['level']}" for s in skills)

def generate_charm():
    #Generates a random Charm
    
    charms_options = [5, 6, 7, 8] #Rarity
    charms_weights = [0.59, 0.27, 0.11, 0.03] #Odds

    charm_rarity = random.choices(charms_options, weights=charms_weights, k=1)[0] #Decides the rarity of the Charm
    
    charm_combo = random.choice(possible_combos[charm_rarity]) #Takes one of the possible_combo tuples for the assigned rarity
    
    charm_skills = skill_assign(charm_combo) #Assigns the skills from the skill_groups
    
    charm_slots = slot_assign(charm_combo) #Assigns a slot from the slots
    
    skills_str = format_skills(charm_skills) #Formats the Skills -> Agitator : 1, [...]
        
    return charm_rarity, skills_str, charm_slots

def generate_charm_window():
    #Generates the Charms in TKinter according to the number slider
    n = count_var.get()
    output_box.config(state="normal") #Let's it edit the output
    
    #Define rarity colours
    output_box.tag_config("5", background="#15af86", foreground="white", font="Helvetica") 
    output_box.tag_config("6", background="#3399ff", foreground="white", font="Helvetica") 
    output_box.tag_config("7", background="#6666ff", foreground="white", font="Helvetica")
    output_box.tag_config("8", background="#f09712", foreground="white", font="Helvetica")  
    
    for i in range(n):
        rarity, skills, slots = generate_charm()
        output_box.insert(f"end",f"Charm:\nRarity: {rarity}\nSkills: {skills}\nSlots: {slots}\n\n", rarity)
        output_box.see("end")
    output_box.config(state="disabled") #Closes the edit

def clear_output():
    #Clears the output
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.config(state="disabled")
    
def set_dark_theme(widget, bg="#1e1e1e", fg="white"):
    try:
        widget.configure(bg=bg, fg=fg)
    except:
        #For Widgets that dont support Background
        try:
            widget.configure(bg=bg)
        except:
            pass

    #Apply to all children
    for child in widget.winfo_children():
        set_dark_theme(child, bg, fg)


#Tkinter window
root = Tk()
root.geometry("720x500")
root.title("Wilds Charm Generator")
frame1 = Frame(root, padx=5)
frame1.pack()


Label(frame1, text="How many charms:").grid(row=0, column=0, padx=2, sticky="w")
#Spinbox -> how many Charms generated
count_var = IntVar(value=1)
count_entry = Spinbox(frame1, from_=1, to=999, textvariable=count_var, width=5)
count_entry.grid(row=0, column=1, padx=2, sticky="w")

#Button -> Generate Charm
generate_charm_button = Button(frame1, text="Generate Charm", command=generate_charm_window)
generate_charm_button.grid(row=0, column=2, padx=2, sticky="w")

#Button -> Clear output
clear_output_button = Button(frame1, text="Clear Output", command=clear_output)
clear_output_button.grid(row=0, column=3, padx=2, sticky="w")

frame2 = Frame(root, padx=5)
frame2.pack(fill="both", expand=True)

#Text -> read-only output
output_box = Text(frame2, wrap="word")
output_box.pack(fill="both", expand=True, padx=10, pady=2)
output_box.config(state="disabled")

set_dark_theme(root)
root.mainloop()