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
    # Frågar användaren om skillen vilkens värde ska hittas
    request = input("Which skill value are you looking for?: ")
        # Om det användaren söker hittas i nested dictionary printar den värdet för skillen
    if request in skill_dict: 
        skill_value = skill_dict.get(str(request))
        print("Skill value: " + str(skill_value))
GetSkill()