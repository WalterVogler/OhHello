import random
import config
import functions

class Siedler:
    def __init__(self, race):
        self.race = config.race_dict.get(race)
        self.id = random.randint(100000, 999999)

    @classmethod
    def add_race(cls,race_key, race_name):
        functions.check_dict("add",config8.race_dict, dict_key=race_key, dict_value=race_name)
        # if race_key not in cls.race_dict and race_name not in cls.race_dict.values():
        config.race_dict[race_key] = race_name
        # else:
        #     raise ValueError(str(race_key) + " or " + race_name + "exitiert bereits")

class Arbeiter(Siedler):
    def __init__(self, race, beruf):
        super().__init__(race)
        # functions.check_dict("init", Arbeiter.beruf_dict, dict_key=Arbeiter.beruf_dict.beruf_key, dict_value=Arbeiter.beruf_valaue)
        # if beruf not in list(Arbeiter.beruf_dict.keys()):
        #     raise ValueError("Mögliche Werte sind", Arbeiter.beruf_dict)
        self.beruf = config.beruf_dict.get(beruf)
        #self.beruf = Arbeiter.beruf_dict.get(beruf,Arbeiter.beruf_dict.get(beruf) == "None",raise ValueError("Beruf nicht in", Arbeiter.beruf_dict))


    def changeBeruf(self, newProfession):
        if newProfession in Arbeiter.beruf_dict:
            self.beruf = Arbeiter.beruf_dict.get(newProfession)
        else:
            raise ValueError("New profession not existent")


class Soldier(Siedler):

    weapon_dict = {
        1:  "Schwertkämpfer",
        2:  "Speerkämpfer",
        3:  "Bogenschütze"
    }
    rank_dict = {
        1:  "Füsilier",
        2:  "Korporal",
        3:  "Leutnant",
        4:  "General"
    }

    def __init__(self, race, weapon_type, rank):
        super().__init__(race)
        if weapon_type not in Soldier.weapon_dict:
            raise ValueError("Mögliche Werte sind", Soldier.weapon_dict)
        self.weapon_type = Soldier.weapon_dict.get(weapon_type)
        if rank not in Soldier.rank_dict:
            raise ValueError("Mögliche Werte sind", Soldier.rank_dict)
        self.rank = Soldier.rank_dict.get(rank)
    def __repr__(self):
        return "Soldier({}, {}, {})".format(self.race, self.weapon_type, self.rank)
    def __str__(self):
        return '{}, {}, {}'.format(self.race, self.weapon_type, self.rank)

obj1 = Arbeiter(2,2)
print(obj1.race, obj1.beruf)
# obj1.changeBeruf(4)
# print(obj1.race, obj1.beruf)
# Siedler.add_race(4,"Amazone")
# # print(Siedler.race(1))
# # print(str(lst(Siedler.race_dict())))
# obj2 = Arbeiter(4,3)
#
# print(obj1.id)
# print(obj2.id)
#
# sold1 = Soldier(1,2,1)
# print(sold1.race, sold1.weapon_type, sold1.rank)

