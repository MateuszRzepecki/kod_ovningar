# Definierar funktion
def GetSkill():
    # Nested dictionary för skills och deras värden
    skill_dict = {
        "fireball": {
            "value": 5
        },
        "frostbolt": {
            "value": 27
        },
        "lightningbolt": {
            "value": 14    
        }
    }
    #
    request = input("Which skill value are you looking for?: ")
    for x in skill_dict:
        if request in skill_dict: 
            skill_value = skill_dict.get("value")
            print("Skill value " + str(skill_value))
            break
GetSkill()