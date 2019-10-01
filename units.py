## file for SI units and physical constants

## fundamental units
meter = 1;
sec =   1;
mol =   1;
amp =   1;  # Fix later, should use Coulomb
volt=   1;
kelvin= 1;

## derived units
cm     = 10**-2 * meter;
mm     = 10**-3 * meter;
micron = 10**-6 * meter;
nm     = 10**-9 * meter;
liter  = 1000 * cm**3;

mA     = 10**-3 * amp;
mV     = 10**-3 * volt;

minute = 60 * sec;
hour   = 3600  * sec;

molar  = mol/liter;
mM     = 10**-3 * molar;

## Physical constants
F      = 96485.3;        # Faraday constant
R      = 8.3144598;      # in SI units, J mol-1 K-1