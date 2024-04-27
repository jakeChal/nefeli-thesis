from geomeppy import IDF
from eppy import modeleditor
import sys
import pandas as pd
import esoreader
import eppy
import os



#TODO: MAKE LOOPS AND DATAFRAME, SIMULATE ALL SCENARIOS, ADD ACTUAL MATERIAL DATA, CHECK THE WINDOWS, CHECK THE HVAC
#material properties from "https://help.iesve.com/ve2021/table_6_thermal_conductivity__specific_heat_capacity_and_density.htm"


#Iterate through all possible combinations
# insulation conductivity = [0.1,0.2,0.3]

#create all possible scenarios
#roof insulation, wall insulation, floor insulation 
#apply these scenarios to the insulation 
#save the results 



########################################CONFIGURATION######################################
# Set the idd file and idf file path
iddfile = 'C:\EnergyPlusV23-2-0\Energy+.idd'
fname1 = 'C:\EnergyPlusV23-2-0\Toy_files\Minimal_1 - Copy (2).idf'
IDF.setiddname(iddfile)

# idf1 now holds all the data to your in you idf file.
idf = IDF(fname1)

# Import epw data
idf.epw = (r"C:\Users\Nefeli\Desktop\thesis_work\Codes\Thesis_Project\Weather_files\NLD_Amsterdam.062400_IWEC"
        r"\NLD_Amsterdam.062400_IWEC.epw")

# Clean objects
# idf.idfobjects.clear()
block = idf.block
del block
# idf.view_model()
# # Geometry
idf.add_block(
    name='House',
    coordinates=[(0, 0), (5.40,0), (5.40, 8.25), (0, 8.25)],
    height=6,
    num_stories=3,
    # below_ground_stories=1,
    # below_ground_storey_height=2.5,
    zoning='by_storey')
idf.intersect_match()
print(idf.getsurfaces())

#windows position and wwr
idf.set_wwr(wwr=0.40, orientation= 'south', wwr_map={0:0} )
idf.set_wwr(wwr=0.40,orientation= 'north', wwr_map={0:0} )
idf.set_wwr(wwr=0.40,orientation= 'west', wwr_map={0:0} )

# Show 3D model
# idf.view_model()

##############Change info about the house
#######Windows
window_materials =  idf.idfobjects['WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM']
window_percentage = 0
# print(window_materials)
Original_U_factor = 2.8
new_ufactor = str((Original_U_factor*window_percentage)+Original_U_factor)
window_material = idf.newidfobject('WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM', Name = "Glazings", UFactor=new_ufactor, Solar_Heat_Gain_Coefficient = 0.3,Visible_Transmittance = 0.8 )
idf.newidfobject("CONSTRUCTION", Name = "Glazing_System",Outside_Layer = 'Glazings')
# del window_materials[0]
# print(window_materials)

#######Add Insulation Material 
original_conductivity =  0.35
r_new_conductivity = 0
w_new_conductivity =0 
f_new_conductivity = 0
roof_conductivity = (original_conductivity*r_new_conductivity)+original_conductivity
wall_conductivity = (original_conductivity*w_new_conductivity)+original_conductivity
floor_conductivity = (original_conductivity*f_new_conductivity)+ original_conductivity
roof_insulation_material = idf.newidfobject('MATERIAL',  Name = "ExteriorRoofInsulation", Thickness = 0.2,Specific_Heat = 1400, Conductivity = roof_conductivity, Density = 25, Roughness = 'Smooth')
wall_insulation_material = idf.newidfobject('MATERIAL',  Name = "ExteriorWallInsulation", Thickness = 0.2,Specific_Heat = 1400, Conductivity = wall_conductivity, Density = 25, Roughness = 'Smooth')
groundfloor_insulation_material = idf.newidfobject('MATERIAL',  Name = "ExteriorFloorInsulation", Thickness = 0.2,Specific_Heat = 1400, Conductivity = floor_conductivity, Density = 25, Roughness = 'Smooth')
# roof_insulation_material = idf.newidfobject('MATERIAL',  Name = "ExteriorRoofInsulation", Thickness = 0.05,Specific_Heat = 1400, Conductivity = original_conductivity, Density = 25, Roughness = 'Smooth')
# wall_insulation_material = idf.newidfobject('MATERIAL',  Name = "ExteriorWallInsulation", Thickness = 0.05,Specific_Heat = 1400, Conductivity = original_conductivity, Density = 25, Roughness = 'Smooth')
# groundfloor_insulation_material = idf.newidfobject('MATERIAL',  Name = "ExteriorFloorInsulation", Thickness = 0.05,Specific_Heat = 1400, Conductivity = original_conductivity, Density = 25, Roughness = 'Smooth')



#######Roofs
#Plywood roof
roof_material = idf.newidfobject('MATERIAL', Name = "Wooden_Roof", Thickness = 0.1,Specific_Heat = 1460, Conductivity = 0.15, Density = 700, Roughness = 'Rough'  )
idf.newidfobject("CONSTRUCTION", Name = "Roof_Structure",Outside_Layer = 'Wooden_Roof', Layer_2 = "ExteriorRoofInsulation")

#######Walls 
brick_material = idf.newidfobject('MATERIAL', Name = "Brick_Wall", Thickness = 0.1,Specific_Heat = 800, Conductivity = 0.84, Density = 1700, Roughness = 'Rough'  )
idf.newidfobject("CONSTRUCTION", Name = "Wall_Structure",Outside_Layer = 'Brick_wall', Layer_2 = "ExteriorWallInsulation",Layer_3 = 'Brick_wall')
# Change surfaces
#Surface types
surfaces = idf.idfobjects['BUILDINGSURFACE:DETAILED']
s_types = [surface.Surface_Type for surface in surfaces]
# print(s_types)

materials =  idf.idfobjects["MATERIAL"]
# print(materials)

#Ceilings
false_ceiling = idf.newidfobject('MATERIAL', Name = "False_Ceiling", Thickness = 0.2,Specific_Heat = 1000, Conductivity = 0.5, Density = 600, Roughness = 'Rough'  )
idf.newidfobject("CONSTRUCTION", Name = "Ceiling_Structure",Outside_Layer = 'False_Ceiling')

#######Floors
brick_material = idf.newidfobject('MATERIAL', Name = "Concrete_Floor", Thickness = 0.2,Specific_Heat = 1000, Conductivity = 0.5, Density = 600, Roughness = 'Rough'  )
idf.newidfobject("CONSTRUCTION", Name = "Floor_Structure",Outside_Layer = 'Concrete_Floor', Layer_2 = "ExteriorFloorInsulation")

# Change surfaces
#Surface types
surfaces = idf.idfobjects['BUILDINGSURFACE:DETAILED']
s_types = [surface.Surface_Type for surface in surfaces]

#Fenestration surfaces
fenestration = idf.idfobjects['FENESTRATIONSURFACE:DETAILED']
del fenestration[2]
del fenestration[-1]


#Surface Boundary Conditions
s_bcs = [surface.Outside_Boundary_Condition for surface in surfaces]
ext_walls = [surface for surface in surfaces if surface.Surface_Type =='wall']
floors = [surface for surface in surfaces if surface.Surface_Type =='floor']
ceilings = [surface for surface in surfaces if surface.Surface_Type =='ceiling']
roofs = [surface for surface in surfaces if surface.Surface_Type =='roof']
#set to adiabatic if interior wall or wall adjacent to another house
windows = [window for window in fenestration]


#Assign Constructions to Surfaces
for floor in floors:
    floor.Construction_Name = "Floor_Structure" # have to create separate floor constructions if multiple storeys
for roof in roofs:
    roof.Construction_Name = "Roof_Structure"
for window in windows: 
    window.Construction_Name = "Glazing_System"
for ceiling in ceilings: 
    ceiling.Construction_Name = "Ceiling_Structure"

# Filter out walls without windows and make them adiabatic
surfaces = idf.idfobjects['BUILDINGSURFACE:DETAILED']
fenestration = idf.idfobjects['FENESTRATIONSURFACE:DETAILED']  # Assuming you have fenestration surfaces defined

for surface in surfaces:
    if surface.Surface_Type == "wall":
        windw = 'window'
        surface_name = surface.Name + ' ' + windw
        # print(surface_name)
        #HEre check if the fenestration and the surface have similar
        for fen in fenestration: 
            if fen.Building_Surface_Name == surface_name :
                surface.Construction_Name = "Wall_Structure"
                surface.Outside_Boundary_Condition = "Adiabatic"
            else :
                surface.Construction_Name = "Wall_Structure"

# Input Site information
site_info = idf.idfobjects['SITE:LOCATION'][0]
# print(site_info)
site_info.Name = 'Amsterdam.Port'
site_info.Latitude = 52.372049
site_info.Longitude = 4.880162
site_info.Time_Zone = +2
site_info.Elevation = 0

# Simulation Control
simulation = idf.idfobjects['SIMULATIONCONTROL']
SimC = idf.idfobjects['SIMULATIONCONTROL'][0]
SimC.Do_Zone_Sizing_Calculation = 'Yes'
SimC.Do_System_Sizing_Calculation = 'No'
SimC.Do_Plant_Sizing_Calculation = 'No'
SimC.Run_Simulation_for_Weather_File_Run_Periods = 'Yes'

stat = idf.newidfobject("HVACTEMPLATE:THERMOSTAT",Name="Zone Stat", Constant_Heating_Setpoint=20,Constant_Cooling_Setpoint=25,)

for zone in idf.idfobjects["ZONE"]:
        idf.newidfobject("HVACTEMPLATE:ZONE:IDEALLOADSAIRSYSTEM",Zone_Name=zone.Name,Template_Thermostat_Name=stat.Name,)

# heatpump = idf.newidfobject("HVACTEMPLATE:ZONE:WATERTOAIRHEATPUMP")
# heatpump.Heat_Pump_Heating_Coil_Gross_Rated_COP =3 
# heatpump.Template_Thermostat_Name = 'Zone Stat'


heating = idf.newidfobject('COIL:HEATING:FUEL')
heating.Name = 'Block 1'
heating.Availability_Schedule_Name = 'AvailSched'
heating.Fuel_Type = 'NaturalGas'
heating.Burner_Efficiency = 0.9
heating.Air_Inlet_Node_Name = 'Block House Storey 0'
heating.Air_Outlet_Node_Name = 'Block House Storey 1'

print(heating)


hotwater = idf.newidfobject('BOILER:HOTWATER')
hotwater.Name = 'Central Boiler'
hotwater.Fuel_Type = 'NaturalGas'
hotwater.Nominal_Capacity = 'autosize'
hotwater.Nominal_Thermal_Efficiency = 0.8
hotwater.Efficiency_Curve_Temperature_Evaluation_Variable = 'LeavingBoiler'
hotwater.Normalized_Boiler_Efficiency_Curve_Name =  'BoilerEfficiency'
hotwater.Design_Water_Flow_Rate = 'autosize'
hotwater.Minimum_Part_Load_Ratio = 0.0
hotwater.Maximum_Part_Load_Ratio = 1.2
hotwater.Optimum_Part_Load_Ratio = 1.0
hotwater.Boiler_Water_Inlet_Node_Name = 'Central Boiler Inlet Node'
hotwater.Boiler_Water_Outlet_Node_Name = 'Central Boiler Outlet Node'
hotwater.Water_Outlet_Upper_Temperature_Limit = 100
hotwater.Boiler_Flow_Mode = 'LeavingSetpointModulated'

airtightness = idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:DETAILEDOPENING')
print(airtightness)
airtightness.Name = 'Window 1'
airtightness.Air_Mass_Flow_Coefficient_When_Opening_is_Closed = 0.01
airtightness.Air_Mass_Flow_Exponent_When_Opening_is_Closed = 0.65
airtightness.Number_of_Sets_of_Opening_Factor_Data = 2
airtightness.Opening_Factor_2 = 1

airtightness_zone =  idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:ZONE')
airtightness_zone.Zone_Name = 'Block House Storey 0'
airtightness_zone.Ventilation_Control_Mode = 'Temperature'

airtightness_surface = idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE')
print(airtightness_surface)
airtightness_surface.Surface_Name = 'Block House Storey 0 Wall 0001'
airtightness_surface.Leakage_Component_Name = 'Crack 1'






#    ** Severe  ** <root>[AirflowNetwork:MultiZone:Component:DetailedOpening][Window 1] - Missing required property 'number_of_sets_of_opening_factor_data'.
#    ** Severe  ** <root>[AirflowNetwork:MultiZone:Component:DetailedOpening][Window 1] - Missing required property 'opening_factor_2'.


idf.newidfobject("OUTPUT:VARIABLE", Key_Value ="Block House Storey 0",Variable_Name = 'Zone Air Infiltration Rate', Reporting_Frequency="Hourly")
idf.newidfobject("OUTPUT:VARIABLE", Key_Value ="Central Boiler", Variable_Name = 'Boiler Gas Rate', Reporting_Frequency="Hourly")
idf.newidfobject("OUTPUT:VARIABLE", Variable_Name="Heating Coil Heating Energy", Reporting_Frequency="Hourly")
idf.newidfobject("OUTPUT:VARIABLE", Variable_Name="Utility Use Per Conditioned Floor Area")
idf.newidfobject("OUTPUT:VARIABLE", Variable_Name="Zone Ideal Loads Supply Air Total Heating Energy",
                Reporting_Frequency="Hourly")
idf.newidfobject("OUTPUT:VARIABLE", Variable_Name="Zone Ideal Loads Supply Air Total Cooling Energy",
                Reporting_Frequency="Hourly")


# idf.view_model()
idf.run()
# import os
# from eppy.results import readhtml

# output_dir = r'C:\Users\Nefeli\Desktop\thesis_work\Codes\Thesis_Project\TrialFiles\Output'
# simulations_dir = os.path.join(output_dir, "simulations")
# file_name = f"roof({r_new_conductivity})_wall({w_new_conductivity})_floor({f_new_conductivity})_window({window_percentage})"
# trial_simulations_dir = os.path.join(output_dir, "trial_simulation")

# # Run simulation
# idf.run(output_directory=trial_simulations_dir, output_prefix=file_name, expandobjects=True, annual=True)