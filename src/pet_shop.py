# WRITE YOUR FUNCTIONS HERE
#1
def get_pet_shop_name(shop_name):
    return shop_name["name"]
#2
def get_total_cash(dollah_sum):
    return dollah_sum ["admin"]["total_cash"]

#didnt work
#  def add_or_remove_cash(pet_shop, cash_added):
#     moneys = pet_shop["admin"]["total_cash"] + cash_added
#     return moneys

#3
def add_or_remove_cash(pet_shop, cash_added):
    pet_shop["admin"]["total_cash"] = pet_shop ["admin"]["total_cash"] + cash_added
    print(pet_shop["admin"]["total_cash"])
    # return pet_shop["admin"]["total_cash"]
#4
def add_or_remove_cash(pet_shop, cash_added):
    pet_shop["admin"]["total_cash"] = pet_shop ["admin"]["total_cash"] + cash_added
    print(pet_shop["admin"]["total_cash"])

#5
def get_pets_sold(shahp):
    print(shahp["admin"]["pets_sold"])
    return shahp["admin"]["pets_sold"]
    
    
#6
def increase_pets_sold(pet_shahp, more_sold):
    pet_shahp["admin"]["pets_sold"] = pet_shahp["admin"]["pets_sold"] + more_sold
    print(pet_shahp["admin"]["pets_sold"])


#7
# (some failed attempts below before getting help - im overcomplicating things)

# def get_stock_count(shop_count):
#     shop_count = len(cc_pet_shop["pets"])#---------not sure why variable not working??
#     return shop_count

# def get_stock_count(stock_number):
#     stock_number = 0
#     pet_shop = stock_number
#     for pet in stock_number["pets"]:
#         if pet["name"] > 0:
#             count += 1

# def get_stock_count(stock_num):
#     cc_pet_shop = ["pets"]["name"]
#     for stock in cc_pet_shop:
#         return sum


def get_stock_count(stock):
    return len(stock["pets"])

#8
# pet = 0
# def get_pets_by_breed(pet_shop, breed):
#     for pet in breed:
#         if breed == "British Shorthair":
#             pet += 1

#             print(pet)

# def get_pets_by_breed(pet_shop, breed):
#     count = 0
#     count = breed
#     for pet in pet_shop["pets"]:
#         if pet == breed:
#             count += 1
#             return count


# def get_pets_by_breed(pet_shop, breed):
#     count = 0
#     for pet in pet_shop:
#         if pet == breed["British Shorthair"]:
#             count.append()
#             return count


# def get_pets_by_breed(pet_shop, breed):
#     pets = pet_shop['pets']
#     count = 0
#     for pet in pets:
#         if pet['breed'] == breed:
#             count += 1
#     return count

def get_pets_by_breed(pet_shop_dict, breed):
    pets = pet_shop_dict['pets']
    matching_pets = [pet for pet in pets if pet['breed'] == breed]
    return matching_pets


# def get_pets_by_breed(pet_shop_dict, breed):
#     matching_pets = 1
#     for i in range(len(pet_shop_dict)):
#         matching_pets[pet_shop_dict[i]] = breed
#     return matching_pets

def get_pets_by_breed(pet_shop_dict, breed):
    pets = pet_shop_dict["pets"]
    matched_pets = [pet for pet in pets if pet["breed"] == breed]
    return matched_pets

# def find_pet_by_name(pet_shop_d, name):
#     pets = pet_shop_d["pets"]
#     pet_name = [pet for pet in pets if pet ["name"] == name]
#     return pet_name


# def find_pet_by_name(pet_shop_dict, name):
#     pet_names = pet_shop_dict["pets"]
#     matched_name = [petname for petname in pet_names if petname["name"] == name]
#     return matched_name

def find_pet_by_name(pet_shop_dict, name):
    pet_names = pet_shop_dict["pets"]
    matched_pets = [pet for pet in pet_names if pet["name"] == name]
    if matched_pets:
        return matched_pets[0]


def find_pet_by_name(pet_shop_dict, name):
    pet_names = pet_shop_dict["pets"]
    matched_pets = [pet for pet in pet_names if pet["name"] == name]
    if matched_pets:
        return matched_pets[0]
    else:
        return None
    
# def remove_pet_by_name(pet_shop_dict, name):
#     pet_names = pet_shop_dict["pets"]
#     matched_pets = [pet for pet in pet_names if pet["name"] == name]
#     matched_pets.remove[0]


# def remove_pet_by_name(pet_shop_dict, name):
#     pet_names = pet_shop_dict["pets"]
#     # matched_pets = [pet for pet in pet_names if pet["name"] == name]
#     if name in pet_names:
#         del name

def remove_pet_by_name(pet_shop_dict, name):
    pet_names = pet_shop_dict["pets"]
    pets_with_name = [pet for pet in pet_names if pet["name"] == name]
    if len(pets_with_name) > 0:
        pet_names.remove(pets_with_name[0])


#________Last few were hugely from the help of others/chat gbt.