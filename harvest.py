############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""
    species = 'Melon'

    def __init__(self, code, name, first_harvest, color, is_seedless, best_seller):
        """Initialize a melon."""

        self.pairings = []

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.best_seller = best_seller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk","Muskmelon", 1998,"green",True, True )
    cas = MelonType("cas","Casaba", 2003,"orange",False, False)
    cren = MelonType("cren","Crenshaw", 1996,"green",False, False)
    yw = MelonType("yw","Yellow Watermelon", 2013,"yellow",False, True)
    all_melon_types.extend([musk, cas, cren, yw])

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs well with {melon.pairings}.')

    
def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dic = {}
    for melon in melon_types:
        melon_dic[melon.name] = [melon.code]

    return melon_dic






############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    species = "Melon"
    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvested_by):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvested_by = harvested_by

    def is_sellable(self, shape_rating, color_rating, harvest_field):
        if self.shape_rating and self.color_rating > 5:
            if self.harvest_field != 3:
                return True
        else:
            return False
    


def make_melons():
    """Returns a list of Melon objects."""
    all_melons = []

    melon1 = Melon('yw', 8, 7, 2, 'Shelia')
    melon2 = Melon('yw', 3, 4, 2, 'Shelia')
    melon3 = Melon('yw', 9, 8, 3, 'Shelia')
    melon4 = Melon('cas', 10, 6, 35, 'Shelia')
    melon5 = Melon('cren', 8, 9, 35, 'Michael')
    melon6 = Melon('cren', 8, 2, 35, 'Michael')
    melon7 = Melon('cren', 2, 3, 4, 'Michael')
    melon8 = Melon('musk', 6, 7, 4, 'Michael')
    melon9 = Melon('yw', 7, 10, 3, 'Shelia')

    all_melons.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9])

    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable(melon.shape_rating, melon.color_rating, melon.harvest_field) == True:
            sellable_ = '(CAN BE SOLD)'
            print(f'Harvested by {melon.harvested_by} from Field {melon.harvest_field}', sellable_)
        else:
            sellable_ = '(NOT SELLABLE)'
            print(f'Harvested by {melon.harvested_by} from Field {melon.harvest_field}', sellable_)

get_sellability_report(make_melons())

