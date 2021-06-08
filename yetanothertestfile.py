#
import random
#
random.seed()

#
def ObT6():
    # 
    pref_range = input("ObT6 range?:")
    # 
    ObT6_list = [random.randint(1, 6) for nr in range(int(pref_range))]
    #
    print(ObT6_list)
    #   
    print(sum(ObT6_list))
ObT6()