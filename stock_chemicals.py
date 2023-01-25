
# Molecular mass in g/mol from the periodic table
periodic = {"H": 1.00784,
           "C": 12.0107,
           "N": 14.0067,
           "O": 15.9994,
           "Na": 22.9897,
           "Cl": 35.453,
           "Fe": 55.845,
           "Ag": 107.868,
           "Pt": 195.084,
           "Au": 196.966          
}

class msalt:
    """ Metal salt """

    def __init__(self, name, molmass):
        self.name = " "
        self.molmass = 0.0
