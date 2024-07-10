# SELBSTRECHERCHIERT
# L:\Projekte\SG-UBT\2024\Kch48_Wasserstoff_Testbetrieb\Thermodynamik\Kh_48_BenötigteParameterThermodynamik.xlsx

        # THERMREG DATEN
# material_data['steel']['rhocp'] = 3.600
# material_data['rrsf']['rhocp'] = 4.200
# material_data['cement']['rhocp'] = 1.600
# material_data['unt_buntsandstein']['rhocp'] = 1.92
# material_data['stasfurt']['rhocp'] = 1.95

# material_data['steel']['lambda'] = 50
# material_data['rrsf']['lambda'] = 0.5
# material_data['cement']['lambda'] = 1.0
# material_data['unt_buntsandstein']['lambda'] = 2.3
# material_data['stasfurt']['lambda'] = 5.5

class MaterialProperties():
    def __init__(self):
        
        self.material_data = {
            'cement': {'rho': 1900, 'cp': 850,'lambda': 0.80},
            'steel':  {'rho': 7850, 'cp': 460,'lambda': 48},
            'rrsf':  {'rho': 1000, 'cp': 4180,'lambda': 0.6},
            'quartar':  {'rho': 1800, 'cp': 950,'lambda': 2.3},
            'unt_buntsandstein':  {'rho': 2500, 'cp': 760,'lambda': 2.6},
            'muschelkalk':  {'rho': 2620, 'cp': 675,'lambda': 2.5},
            'hauptanhydrit':  {'rho': 2900, 'cp': 864,'lambda': 4.0},
            'stasfurt':  {'rho': 2160, 'cp': 860,'lambda': 5.91},
            'anhydrit':  {'rho': 3000, 'cp': 860,'lambda': 4.2},
            'leine': {'rho': 2160, 'cp': 860,'lambda': 5.23},
            'keuper': {'rho': 2600, 'cp': 731, 'lambda': 2.5},
        }


