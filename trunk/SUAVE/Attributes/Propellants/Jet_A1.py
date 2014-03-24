""" Jet_A1.py: Physical properties of Jet A-1 hydrocarbon propellant """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from Propellant import Propellant

# ----------------------------------------------------------------------
#  Class
# ----------------------------------------------------------------------

class Jet_A1(Propellant):

    """ Physical properties of Jet A-1; reactant = O2 """

    def __defaults__(self):

        self.tag = 'Jet A'
        self.reactant = 'O2'
        self.density = 804.0                                    # kg/m^3 (15 C, 1 atm)
        self.specific_energy = 43.15e6                          # J/kg
        self.energy_density = 34692.6e6                         # J/m^3
        self.max_mass_fraction = {'Air' : 0.0633, 'O2' : 0.3022}# kg propellant / kg oxidizer
        self.temperatures = Data()
        self.temperatures.flash = 311.15                        # K
        self.temperatures.autoignition = 483.15                 # K
        self.temperatures.freeze = 226.15                       # K
        self.temperatures.boiling = 0.0                         # K