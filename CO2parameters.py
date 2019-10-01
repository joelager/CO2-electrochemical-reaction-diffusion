## Constants for the CO2 reduction problem
from units import *    # make sure these are in place

## Equibrium constants
# Water dissociation
Kw = 10**-14 * molar**2

# Henry's law
KHenry = 2.63 * 10**-3;                   # Not used by GGM

# bicarbonate for acid (a) and base (b)
K1a    = 4.44 * 10**-7 * molar;           # CO2(aq) + H2O <-> HCO3- + H+
K1b    = 4.44 *10**7 * molar**-1;         # CO2(aq) + OH- <-> HCO3-
                                          # K1b = K1a/Kw
# bicarbonate- carbonate for acid (a) and base (b)
K2a     = 4.66 * 10**-11 * molar;       # HCO3- <-> H+ + CO3--
K2b     = 4.66 * 10**3 * molar**-1;       # HCO3- + OH- <-> CO3-- + H20
                                          # K2b = K2a/Kw
# Overall 
K3     = 9.52 * 10**3;                    # CO2(aq) + CO3-- + H2O <-> 2HCO3-

## Kinetics
factor1 = 10**0;                                      # slow down for stability
factor2 = 1;
# CO2-bicarbonate
k1f    = factor1 * 5.93 * 10**3  * molar**-1 * sec**-1;  # CO2(aq) + OH- -> HCO3-
k1r    = factor1 * 1.34 * 10**-4 * sec**-1;              # HCO3- ->  CO2(aq) + OH- 
# bicarbonate-carbonate, k2f is assumed to be fast
k2f    = factor2 * 1.00 * 10**8 * molar**-1 * sec**-1;   # HCO3- + OH- -> CO2-- + H20
k2r    = factor2 * 2.15 * 10**4 * sec**-1;               # CO3-- + H20 -> HCO3- + OH

T = 300*kelvin;
## Diffusion coefficients from Table 2 of GGM
DCO2     = 1.91 * 10**-9  * meter**2 * sec**-1;
DOH      = 5.27 * 10**-9 * meter**2 * sec**-1;
DHCO3    = 1.19 * 10**-9  * meter**2 * sec**-1;
DCO3     = 9.23 * 10**-10 * meter**2 * sec**-1;

## Faradaic efficiencies for Cu, GGM
# FEmethane      = 0.25;
# FEethylene     = 0.20;
# FECO           = 0.05;
# FEformate      = 0.10;
# FEH2           = 0.40;

## Faradaic efficiencies for Cu foil, Zhong
# FEH2           = 0.50;
# FEmethane      = 0.24;
# FEethylene     = 0.28;
# FECO           = 0.03;
# FEformate      = 0.05;

## ## Faradaic efficiencies for Ag
# FEmethane      = 0.00;
# FEethylene     = 0.00;
# FECO           = 0.80;
# FEformate      = 0.00;
# FEH2           = 0.20;

#100% CO
# FEmethane      = 0.00;
# FEethylene     = 0.00;
# FECO           = 1.00;
# FEformate      = 0.00;
# FEH2           = 0.00;

## 100% formate.  pH is not as high.  
FEmethane      = 0.00;
FEethylene     = 0.00;
FECO           = 0.00;
FEformate      = 1.00;
FEH2           = 0.00;

## Electrons exchanged
zMethane       =  8;
zEthylene      = 12;
zCO            =  2;
zFormate       =  2;
zH2            =  2;

## charges - not used
zHCO3          = -1;
zCO3           = -2;
zOH            = -1;