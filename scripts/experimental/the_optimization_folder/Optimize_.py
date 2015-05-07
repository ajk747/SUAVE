# Optimize.py
# 
# Created:  May 2015, E. Botero
# Modified: 

# ----------------------------------------------------------------------        
#   Imports
# ----------------------------------------------------------------------    

import SUAVE
from SUAVE.Core import Units

# ----------------------------------------------------------------------        
#   Run the whole thing
# ----------------------------------------------------------------------  
def main():
   
   problem = setup_problem()


   return

# ----------------------------------------------------------------------        
#   Inputs, Objective, & Constraints
# ----------------------------------------------------------------------  

def setup_problem():
   
   problem = Data() # Change me
    
   # -------------------------------------------------------------------
   # Inputs
   # -------------------------------------------------------------------
   
   # [ tag , initial, [lb,ub], scaling, units ]
   problem.inputs = [
      [ 'aspect_ratio'    ,   10.    , (     5.    ,    20.   ) ,    10.  ,    Units.less], 
      [ 'reference_area'  ,   125.   , (    70.    ,   200.   ) ,   125.  , Units.meter^2],
      [ 'sweep'           ,    25.   , (     0.    ,    60.   ) ,    25.  , Units.degrees],
      [ 'design_thrust'   , 24000.   , ( 10000.    , 35000.   ) , 24000.  , Units.Newtons],
      [ 'wing_thickness'  ,     0.11 , (     0.07  ,     0.20 ) ,      .11,    Units.less],
      [ 'MTOW'            , 79000.   , ( 60000.    ,100000.   ) , 79000.  ,      Units.kg],
      [ 'MZFW'            , 59250.   , ( 30000.    ,100000.   ) , 59250.  ,    Units.less], 
   ]
   
   # -------------------------------------------------------------------
   # Objective
   # -------------------------------------------------------------------

   # throw an error if the user isn't specific about wildcards
   # [ tag, scaling, units ]
   problem.objective = [
      [ 'fuel_burn', 10000, Units.kg ]
   ]
   
   # -------------------------------------------------------------------
   # Constraints
   # -------------------------------------------------------------------

   # [ tag, sense, edge, scaling, units ]
   problem.constraints =[
      [ 'takeoff_field_length' , '<',  2180., 5000.,    Units.m],
      [ 'range_short_field'    , '>',   650.,  500.,  Units.nmi],
      [ 'range_max_nmi'        , '>',  2725., 1000.,  Units.nmi],
      [ 'max_zero_fuel_margin' , '>',     0.,    1., Units.less],
      [ 'available_fuel_margin', '>'  ,   0.,        Units.less],
   ]
 
   return problem

if __name__ == '__main__':
   main()