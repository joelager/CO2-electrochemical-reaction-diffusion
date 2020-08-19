# CO2-electrochemical-reaction-diffusion
Author: Joel W. Ager (jwager@lbl.gov)

Different approaches to solve the reaction-diffusion equations for the CO<sub>2</sub>-bicarbonate-carbonate-hydroxide system in 1D and in 2D using Python packages. 
 
After Gattrell and co-workers:  
>Gupta, N.; Gattrell, M.; MacDougall, B. Calculation for the Cathode Surface Concentrations in the Electrochemical Reduction of CO<sub>2</sub> in KHCO<sub>3</sub> Solutions. [J. Appl. Electrochem. **2006**, *36*, 161–172](http://link.springer.com/10.1007/s10800-005-9058-y).

* `1D CO2 reaction diffusion-SciPy.ipynb` solves the 1D, time-independent problem using using `solve_bvp` from the `scipy` package.  
* `1D CO2 reaction diffusion FEniCS.ipynb` solves the 1D, time-dependent problem using using the Newton's method non-linear solver the `FEniCS` finite element package.  
* `2D CO2 reaction diffusion FEniCS.ipynb` solves the 2D,  time-independent and time-dependent problems using `FEniCS`. The solution is on a simple rectangular domain but it would be possible to generate more complex geometries with `GMSH` and import the mesh via the `meshio` package. 
