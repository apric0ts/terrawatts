import random

class Climate():
    def __init__(self, sunlight, wind_speed):
        self.sunlight = sunlight # 0 -> 1
        self.wind_speed = wind_speed

class Sunny(Climate):
    def calculate_sun_level() -> float: 
        return random.randint()/100.0

class Windy(Climate):
    def calculate_wind_level() -> float: 
        return random.randint()/100.0

class EnergySource:
    def __init__(self, id: str, cost: int, output: float):
        self.id: str = id
        self.cost: int = cost
        self.output: float = output
        # self.upgrade_level = upgrade_level
    
    def calculate_energy_output(c) -> float:
        pass

    def isValid(terrain: str) -> bool:
        pass
    
class Windmill(EnergySource):
    def calculate_energy_output(self, climate: Climate) -> float:
        return self.output * climate.wind_speed
    
    def isValid(terrain: str) -> bool:
        return (terrain != "Ocean" or terrain != "Swamp")  
    


class SolarPanel(EnergySource):
    def calculate_energy_output(self, climate: Climate) -> float:
        return self.output * climate.sunlight

    def isValid(terrain: str) -> bool:
        return (terrain != "Ocean" or terrain != "Swamp") 


class Turbine(EnergySource):
    def calculate_energy_output(self, climate: Climate) -> float:
        return self.output

    def isValid(terrain: str) -> bool:
        return (terrain == "Ocean")  


class Player():
    def __init__(self, energy_source_dict, balance, revenue):
        self.energy_source_dict = energy_source_dict
        self.balance = balance
        self.revenue = revenue

class Customer(): 
    def __init__(self, happiness): 
        self.happiness = happiness #number from 0 to 1 

class Posn():
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Board():
    def __init__(self, board):
        self.board = board # list of list of tiles
        self.width = len(board[0])
        self.height = len(board)




class Tile():
    def __init__(self, terrain: str, energy_source: EnergySource, image):
        self.terrain = terrain
        self.energy_source = energy_source
        self.image = image






# starting_turbine_01 = Turbine("Turbine1", 100, 30.0)
# starting_tile_01 = Tile("plateau",starting_turbine_01, null)

#creating starting board 
'''
LLOOLL
LLLOSS
SLOLSO
SSLLOS
SLLOOO 
OOSSSL
LLSSOL 
'''

customer = Customer(0.85);  
c = Climate(0.55, 0.10)
balance = 200
plateau_tile = Tile("plateau", None, None) 
ocean_tile = Tile("ocean", None, None) 
swamp_tile = Tile("swamp", None, None)
row_1 = [plateau_tile, plateau_tile, ocean_tile, ocean_tile, plateau_tile, plateau_tile] 
row_2 = [plateau_tile, plateau_tile, plateau_tile, ocean_tile, swamp_tile, swamp_tile]
row_3 = [swamp_tile, plateau_tile, ocean_tile, plateau_tile, swamp_tile, ocean_tile]
row_4 = [swamp_tile, swamp_tile, plateau_tile, plateau_tile, ocean_tile, swamp_tile]
row_5 = [swamp_tile, plateau_tile, plateau_tile, ocean_tile, ocean_tile, ocean_tile]
row_6 = [ocean_tile, ocean_tile, swamp_tile, swamp_tile, swamp_tile, plateau_tile]
row_7 = [plateau_tile, plateau_tile, swamp_tile, swamp_tile, ocean_tile, plateau_tile]

# starting_board_1 = [row_1, row_2, row_3, row_4, row_5, row_6, row_7]
starting_board_1 = Board([row_1, row_2, row_3, row_4, row_5, row_6, row_7])