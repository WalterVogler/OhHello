def blabla():
    print("hoi papi")

def check_dict(option, dict, dict_key=-100, dict_value="n/a"):

    if option == "add" and ( dict_key == -100 or dict_key in dict):
        raise ValueError("Key: " + str(dict_key) + " - Existing values are: " + str(list(dict.keys())) + " from " + str(dict))

    if option == "add" and ( dict_value == "n/a" or dict_value in list(dict.values())):
        raise ValueError("Value: " + dict_value + " - Possible values are: " + str(list(dict.values())) + " from " + str(dict))

    if option != "add" and dict_key != -100 and dict_key not in dict:
        raise ValueError("Key: " + str(dict_key) + " - Possible values are: " + str(list(dict.keys())) + " from " + str(dict))

    if option != "add" and dict_value != "n/a" and dict_value not in list(dict.values()):
        raise ValueError("Value: " + dict_value + " - Possible values are: " + str(list(dict.values())) + " from " + str(dict))
