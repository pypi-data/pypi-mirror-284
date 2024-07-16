import ollama

def generate_quest(template_info, objective_info, location_info):
    brainstorming_system_prompt = (f"You are a Quest Designer at a Game studio.\n"
    f"You have been tasked with creating compelling Side-Quests for a Role-Playing Game.\n"
    f"The game is set in a Fantasy setting.\n"
    f"Create engaging and creative questlines that enhance the player's experience and provide meaningful content.\n"
    f"You should create multi-part questlines.\n"
    f"Try to compelling narratives that deviate from the norms.\n"

    f"\n###\n"

    f"The questline generated should follow the \"template\" given below:\n"

    f"{template_info}\n"

    f"\n###\n"

    f"Each quest of the questline should be of a type otlined in the \"quest_objectives\" below:\n"

    f"{objective_info}\n"
    
    f"\n###\n"

    f"\nGive a name to the questline as a whole.\n"

    f"\nDescribe each quest in the format given:\n"
    f"Name:\nType:\nGoal:\nDescription:\n")
    
    brainstorming_user_prompt = (f"You are a Quest Designer at a Game studio.\n"
        
    f"\n###\n"
    
    f"Outlined below are the primary locations available for the questline:\n"
    
    f"{location_info}\n"
        
    f"\n###\n"

    f"Consider the \"theme tags\" given below and generate a questline according to the system instructions.\n"

    f"Archetype Tag:\n"
    f"Breaking the Cycle - The characters must find a way to break a repeating cycle of destruction or misfortune.\n"
    f"Character Tags:\n"
    f"Werewolves\n"
    f"Tone Tags:\n"
    f"Comedy\n"
    
    f"\n###\n"

    f"Remember to adhere to the system instructions.\n")

    response = ollama.chat(model="llama3", messages=[
        {
            "role": "system",
            "content": brainstorming_system_prompt
        },
        {
            "role": "user",
            "content": brainstorming_user_prompt
        }
    ], options={"temperature": 2})

    return response["message"]["content"]