from .questAgents import quest_brainstormer

def generate_quest(template_info, objective_info, location_info):
    return quest_brainstormer.generate_quest(template_info, objective_info, location_info)