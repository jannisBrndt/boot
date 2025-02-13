def meditate(mana, max_mana, energy, energy_drinks):
    # as long as mana is not maxed, meditate and convert
    while mana < max_mana:
        # check if energy is zero
        if (energy == 0):
            # check if energy_drinks are available
            if (energy_drinks >= 1):
                energy_drinks -= 1
                energy += 50
            else:
                return mana, energy, energy_drinks
        mana += 1
        energy -= 1
        
    return mana, energy, energy_drinks

def main():
    mana = 0
    max_mana = 10
    energy = 9
    energy_drinks = 0

    meditate(mana, max_mana, energy, energy_drinks)

main()
