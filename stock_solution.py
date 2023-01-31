'''
by Scott Clemens
This program calculates the water volume based on the mass of each stock solution
and tracks total material usage.
'''
import csv

# molecular mass in grams per mole (g/mol)
molmass = {"H": 1.00784,
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

# metal salts:
AgNO3 = molmass["Ag"] + molmass["N"] + 3*molmass["O"]
AuCl = molmass["Au"] + molmass["Cl"]
NH4_2PtCl4 = 2*molmass["N"] + 8*molmass["H"] + molmass["Pt"] + 4*molmass["Cl"]
C6FeN3O12_3H2O = 6*molmass["C"] + 15*molmass["O"] + 18*molmass["H"] + molmass["Fe"] + 3*molmass['N'] #FIXME: wrong MW
# reducing agent:
NaCit = 9*molmass["H"] + 9*molmass["O"] + 6*molmass["C"] + 3*molmass["Na"]
# photoinitiator:
Irgacure = 16*molmass["H"] + 12*molmass["C"] + 4*molmass["O"]

Aam = 7*molmass["H"] + 3*molmass["C"] + molmass["N"]

chemicals = {"AgNO3": AgNO3,
             "AuCl": AuCl,
             "(NH4)2PtCl4": NH4_2PtCl4,
             "C6Fe2O12(H2O)6": C6FeN3O12_3H2O
}

def water_volume(mass, chemical, molarity):
    mol = mass/chemical
    volume = mol/molarity
    water_percent = (volume*1000)/(volume*1000 + mass)
    chemical_percent = mass/(volume*1000 + mass)
    return volume, water_percent, chemical_percent

def print_details():
    print("Metal Salts")
    print("C6FeN3O12*3H2O [Iron(III) Oxalate Trihydrate]\nMW:", round(C6FeN3O12_3H2O, 3), "g/mol \t", round((100*molmass["Fe"]/C6FeN3O12_3H2O), 2), "% Iron by weight.")
    print("AgNO3 [Silver Nitrate]\nMW:", round(AgNO3, 3), "g/mol \t", round((100*molmass["Ag"]/AgNO3), 2), "% Silver by weight.")
    print("AuCl [Gold (I) Chloride]\nMW:", round(AuCl, 3), "g/mol \t", round((100*molmass["Au"]/AuCl), 2), "% Gold by weight.")
    print("(NH4)2PtCl4 [Platinum(II)-Ammonium Chloride]\nMW:", round(NH4_2PtCl4, 3), "g/mol \t", round((100*(molmass["Pt"])/NH4_2PtCl4), 2), "% Platinum by weight.")
    print("\nReducing Agents")
    print("NaCit (Sodium Citrate)\nMW:", round(NaCit, 3), "g/mol")
    print("\nOther")
    print("Aam [Allylamine]\nMW:", Aam, "g/mol")
    print("[Irgacure]\nMW:", Irgacure, "g/mol")
    print()

def molarity(mol_mass, name, experiment):
    mass = float(input(f"Enter experiment {experiment} mass in grams:\t"))
    mol_choice = 0.001*float(input(f"Enter experiment {experiment} molarity in mM:\t"))
    mol = mass/mol_mass
    volume = mol/mol_choice
    volume = volume*1000
    print(name, "with", mass, "g needs", round(volume, 3), "mL water.")
    return mass, mol_choice, volume

if __name__ == "__main__":
    # print out all information on chemicals and MW of each
    print_details()
        
    choice = int(input("Which material are you using?\n1 - Iron(III) Oxalate Trihydrate\n2 - Silver Nitrate\n3 - Gold (I) Chloride\n4 - Platinum (II) Ammonium Chloride\n5 - Sodium Citrate\n"))
    if choice == 1:
        chemical = C6FeN3O12_3H2O
        name = "Iron(III) Oxalate Trihydrate"
    elif choice == 2:
        chemical = AgNO3
        name = "Silver Nitrate"
    elif choice == 3:
        chemical = AuCl
        name = "Gold (I) Chloride"
    elif choice == 4:
        chemical = NH4_2PtCl4
        name = "Platinum (II) Ammonium Chloride"
    elif choice == 5:
        chemical = NaCit
        name = "Sodium Citrate"
    else:
        quit()

    with open(name + " Experiment Plan.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel', delimiter=',')
        writer.writerow(["Experiment", "Molarity [mM]", "Mass [g]", "Remaining [g]", "Water [mL]"])

        try:
            mass_initial = float(input(f"Enter total available (starting) mass of {name} in grams: "))
            mass_used  = 0.0
            experiment = 1
            
            while mass_used <= mass_initial:
                mass_used, mol_choice, water = molarity(chemical, name, experiment)
                writer.writerow([experiment, (mol_choice*1000), mass_used, mass_initial, round(water, 3)])
                mass_initial -= mass_used
                print()
                print(f"Experiment {experiment} mass used: {mass_used} g, total remaining: {mass_initial} g")
                experiment += 1
        except:
            quit()
    # FIXME: Iron salts MW incorrect; should be 428 g/mol

    # FIXME: Calculate the final concentration of chemicals in the precursor solution

    # FIXME: Export data to a .csv file to import into excel

