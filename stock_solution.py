'''
Scott Clemens
This program calculates the water volume based on the mass of each stock solution
'''

# molecular mass in grams per mole (g/mol)
molmass = {"H": 1.00784,
           "C": 12.0107,
           "N": 14.0067,
           "O": 15.9994,
           "Na": 22.9897,
           "Cl": 35.453,
           "Ag": 107.868,
           "Pt": 195.084,
           "Au": 196.966          
}

# metal salts:
AgNO3 = molmass["Ag"] + molmass["N"] + 3*molmass["O"]
AuCl = molmass["Au"] + molmass["Cl"]
NH4_2PtCl4 = 2*molmass["N"] + 8*molmass["H"] + molmass["Pt"] + 4*molmass["Cl"]
# reducing agent:
NaCit = 9*molmass["H"] + 9*molmass["O"] + 6*molmass["C"] + 3*molmass["Na"]
# photoinitiator:
Irgacure = 16*molmass["H"] + 12*molmass["C"] + 4*molmass["O"]

Aam = 7*molmass["H"] + 3*molmass["C"] + molmass["N"]


def water_volume(mass, chemical, molarity):
    mol = mass/chemical
    volume = mol/molarity
    water_percent = (volume*1000)/(volume*1000 + mass)
    chemical_percent = mass/(volume*1000 + mass)
    return volume, water_percent, chemical_percent

def print_chemicals():
    print("Metal Salts")
    print("AgNO3 [Silver Nitrate]\nMW:", round(AgNO3, 3), "g/mol \t", round((100*molmass["Ag"]/AgNO3), 2), "% Silver by weight.")
    print("AuCl [Gold (I) Chloride]\nMW:", round(AuCl, 3), "g/mol \t", round((100*molmass["Au"]/AuCl), 2), "% Gold by weight.")
    print("(NH4)2PtCl4 [Platinum(II)-Ammonium Chloride]\nMW:", round(NH4_2PtCl4, 3), "g/mol \t", round((100*(molmass["Pt"])/NH4_2PtCl4), 2), "% Platinum by weight.")
    print("\nReducing Agents")
    print("NaCit (Sodium Citrate)\nMW:", round(NaCit, 3), "g/mol")
    print("\nOther")
    print("Aam [Allylamine]\nMW:", Aam, "g/mol")
    print("[Irgacure]\nMW:", Irgacure, "g/mol")
    print()

def metal_type(metal):
    if metal == 1:
        # prompt user for silver nitrate and sodium citrate masses

        Ag_mass = float(input("Enter AgNO3 mass in grams: "))
        Ag_molarity = float(input("Enter molarity: "))
        NaCit_mass = float(input("Enter NaCit mass in grams: "))
        NaCit_molarity = float(input("Enter molarity: "))
        
        Ag_volume, Ag_water, Ag_percent = water_volume(Ag_mass, AgNO3, Ag_molarity)
        NaCit_volume, NaCit_water, NaCit_percent = water_volume(NaCit_mass, NaCit, NaCit_molarity)
    
        print("\nAgNO3 with", Ag_mass, "g needs", round((Ag_volume*1000), 3), "mL water.\nWater is", round((Ag_water*100), 2), "% and AgNO3 is", round((Ag_percent*100), 2), "%")
        print("NaCit with", NaCit_mass, "g needs", round((NaCit_volume*1000), 3), "mL water.\nWater is", round((NaCit_water*100), 2), "% and NaCit is", round((NaCit_percent*100), 2), "%")
    elif metal == 2:
        # Gold
        pass
    elif metal == 3:
        # Platinum
        pass

if __name__ == "__main__":
    print_chemicals()
    metal = int(input("Which metal are you using?\n1 - Silver Nitrate\n2 - Gold (I) Chloride\n3 - Platinum (II) Ammonium Chloride\n"))
    metal_type(metal)
    
    
