"""
Section: 2.1.1.2

Estimated time: 30-45 minutes

Level of difficulty: Medium

Objectives
Learn how to:

    use the json module and its basic facilities;
    encode and decode JSON strings from/to Python objects.

Scenario
Take a look at these two screenshots. They present two different use cases of the same program:

Command prompt -- python 01.py

Command prompt -- python 02.py

Your task is to write a code which has exactly the same conversation with the user and:

    defines a class named Vehicle, whose objects can carry the vehicle data shown above (the structure of the class should be deducted from the above dialog — call it "reverse engineering" if you want)
    defines a class able to encode the Vehicle object into an equivalent JSON string;
    defines a class able to decode the JSON string into the newly created Vehicle object.

Of course, some basic data validity checks should be done, too. We're sure you're careful enough to protect your code from reckless users.

"""

import json


class Vehicle:
    def __init__(self, reg_num, prod_year, is_passenger, vechile_mass):
        self.reg_num = reg_num
        self.prod_year = prod_year
        self.is_passenger = is_passenger
        self.vechile_mass = vechile_mass


class VehicleEncoder(json.JSONEncoder):
    def default(self, v):
        if isinstance(v, Vehicle):
            return v.__dict__
        else:
            return super().default(self, z)


class VehicleDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, v):
        return Vehicle(**v)
    
def enter_regnum():
    while True:
        regnum = input("Registration number (alphanumeric and the max length is 8): ")
        if len(regnum) <= 8 or regnum.isalnum():
            break
        else:
            print("Invalid registration number. Enter again.")

    return regnum

def enter_prodyear():
    while True:
        prodyear = input("Production year (yyyy): ")
        if len(prodyear) <= 8 or prodyear.isdigit():
            try:
                year = int(prodyear)
                if year > 1900 and year < 2030:
                    break
            except:
                pass
        else:
            print("Invalid production year. Enter again.")

    return prodyear

def enter_passenger():
    while True:
        passenger = input("Passenger [y/n]: ")
        if passenger == "y" or passenger == "n":
            break
        else:
            print("Invalid passenger type. Enter again.")

    return passenger

def enter_carmass():
    while True:
        carmass = input("Vechile mass (kgs): ")
        try:
            value = int(carmass)
            break
        except:
            print("Invalid vechile mass. Enter again.")

    return carmass

def get_user_inputs():
    regnum = enter_regnum()
    prodyear = enter_prodyear()
    passenger = enter_passenger()
    carmass = enter_carmass()

    return Vehicle(regnum, prodyear, passenger, carmass)

# Main routine
print("What can I do for you?")
print("1 - produce a JSON string describing a vehicle")
print("2 - decode a JSON string into a vehicle data")

while True:
    choice = input("Your choice: ")
    if not (choice == "1" or choice == "2"):
        print("Invalid choice. Try again.")
    else:
        break

if choice == "1":
    vehicle = get_user_inputs()
    json_str = json.dumps(vehicle, cls=VehicleEncoder)
    print(f"Result JSON string is:\n{json_str}")
else:
    json_input = input("Enter vehicle JSON string: ")
    while True:
        try:
            new_vechile = json.loads(json_input, cls=VehicleDecoder)
            print("\nThe object info:")
            print(type(new_vechile))
            print(new_vechile.__dict__)
            break
        except Exception as e:
            print("Invalid JSON string. Try again.", e)
