from basic import Siedler, Soldier
import config

inputRace = None
myRace = None

# for key, value in config.race_dict.items():
#     print(key,":", value)

# allRaces = None
# for key, value in config.race_dict.items():
#     allRaces += str(key)+":"+value
# print(allRaces)allRaces

# print("races dict, keys   : {}".format(", ".join(str(list(config.race_dict.items())))))
# print("races dict, values : {}".format(", ".join(list(config.race_dict.values()))))

while (inputRace != 'end'):
    while True:
        inputRace = input("Chose a race : ")

        try:
            if inputRace.isnumeric():
                myRace = list(config.race_dict.values())[list(config.race_dict.keys()).index(int(inputRace))]
            else:
                myRace = list(config.race_dict.values())[list(config.race_dict.values()).index(inputRace)]

            # print("inputRace : {}, myRace : {}".format(inputRace,myRace))

        except:
            if inputRace == 'end':
                break
            if inputRace.isnumeric():
                # print("Valid races are: {} Your key {} is not available!"
                #       .format(", ".join(list(config.race_dict())), inputRace))
                # print("Valid keys are: {}!"
                #      .format(", ".join(list(config.race_dict.keys())),inputRace))
                print("Valid races are: {} Your key {} is not available!"
                      .format(", ".join(list(config.race_dict.values())), inputRace))
                # print("Valid races are: {} Your key {} is not available!"
                #       .format(", ".join(list(config.race_dict.keys())),": ".join(list(config.race_dict.values()))
                #               , inputRace)
                #       )
            else:
                print("Valid races are: {} Your value '{}' is not available!"
                      .format(", ".join(list(config.race_dict.values())), inputRace))

            continue
        else:
            print("Congratulation! {} : {}"
                  .format(list(config.race_dict.keys())[list(config.race_dict.values()).index(myRace)]
                         ,list(config.race_dict.values())[list(config.race_dict.values()).index(myRace)]
                  )      )
            break
