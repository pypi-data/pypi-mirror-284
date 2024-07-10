# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:09:12 2023

@author: atakan
"""

import os
# from time import time
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
import numpy as np
# import CoolProp.CoolProp as CP
import carbatpy
if carbatpy._TREND["USE_TREND"]:
    try:
        import fluid as tr_fl  # TREND fluids
    except ImportError as e:
        print(f"Import error for 'fluid': {e}")
    


# os.environ['RPPREFIX'] = r'C:/Program Files (x86)/REFPROP'
# os.environ['RPPREFIXs'] = r'C:/Program Files (x86)/REFPROP/secondCopyREFPROP'
_PROPS = "REFPROP"  # or "CoolProp"

_fl_properties_names = ("Temperature", "Pressure", "spec_Enthalpy",
                        "spec_Volume", "spec_Entropy", "quality",
                        "spec_internal_Energy",
                        "viscosity", "thermal_conductivity",
                        "Prandtl_number", "k_viscosity", "molecular_mass",
                        "speed_of_sound")
_THERMO_STRING = "T;P;H;V;S;QMASS;E"
_THERMO_TREND = request = ["T","P","H" "D", "S", "Q","U"] # careful density not volume
_TRANS_STRING = _THERMO_STRING + ";VIS;TCX;PRANDTL;KV;M;W"
_TRANS_TREND = _THERMO_TREND.extend([ "ETA","TCX", "WS"])
_TV_STRING = "T;V"
_T_SURROUNDING = 288.15 # K
_MODEL_ARGS = {}

# order for coolprop,alle_0:[_temp, p,  h, 1/ rho, s,x,cp, mu,  lambda_s,
# prandtl, phase]"
_UNITS = 21
rp_instance = ""
if _PROPS == "REFPROP":
    try:
        rp_instance = REFPROPFunctionLibrary(os.environ['RPPREFIX'])
        # be careful pressure is in Pa!
        _UNITS = rp_instance.GETENUMdll(0, "MASS BASE SI").iEnum
    except:
        print("print refprop not installed!")
elif _PROPS == "TREND":
    pass
else:
    print(f"_PROPS value not unstalled {_PROPS}")



class FluidModel:

    def __init__(self, fluid, units=_UNITS, props=_PROPS, rp_inst=rp_instance,
                 args=_MODEL_ARGS):
        """
        For Class Fluidmodell a fluid (mixture) must be defined, the evaluation
        takes place with props, units can be set and an instance can be set,
        the latter is important, if more than one fluid is used.

        Parameters
        ----------
        fluid : String
            as defined in the props (Model), for RefProp it is
            "fluid1 * fluid2 * fluid3".
        units : integer, optional
            units, normally SI wuth MASS base, see props(RefProp).
            The default is _UNITS.
        props : string, optional
            select the property model. The default is _PROPS.
        rp_inst : RefProp-Instance, optional
            where Refprop is installed, for two fluids, as in heat exchangers,
            two installations/instances are needed. The default is rp_instance.

        Returns
        -------
        None.

        """
        self.fluid = fluid
        self.props = props
        self.units = units
        self.args = args
        if props == "REFPROP":
            self.rp_instance = rp_inst
            self.set_rp_fluid()
        elif props == "TREND":
            self.set_tr_fluid()

    def set_rp_fluid(self, modwf=REFPROPFunctionLibrary, name='RPPREFIX'):
        """
        A new instance of Refpropdll for the given fluid. It can then be called
        using fluid =""

        Parameters
        ----------
        fluid : string
            fluid (mixture) name, as described in REFPROP.

        Returns
        -------
        self.rp_instance : REFPROP Instance
            for further usage.

        """

        self.rp_instance = modwf(os.environ[name])
        self.rp_instance.SETPATHdll(os.environ[name])
        ierr = self.rp_instance.SETFLUIDSdll(self.fluid)
        if ierr != 0:
            print(f"Fehler in setfluid {ierr}")
            print(self.rp_instance.ERRMSGdll(ierr))
        return self.rp_instance
    
    def set_tr_fluid(self):
        self.fluid = self.fluid_to_list()
        """
        in_states, 
        fld = fluid.Fluid(self.args["input"],
                          self.args['output'],
                          species,
                          self.["composition"],
                          self.
            'TP','H',['water'],[1],[1],1,path,'specific',dll_path)

        
        """
        
        
    def fluid_to_list(self):
        no_blank = self.fluid.replace(" ","")
        return no_blank.split("*")
        
        


class FluidState:
    def __init__(self, state):
        self.temperature = state.Output[0]
        self.pressure = state.Output[1]
        self.sp_volume = state.Output[3]
        self.enthalpy = state.Output[2]
        self.entropy = state.Output[4]
        self.quality = state.Output[5]
        self.int_energy = state.Output[6]
        self.state = state.Output[:7]
        self.prop_names = _fl_properties_names


class FluidStateTV:
    def __init__(self, state):
        self.temperature = state.Output[0]
        self.sp_volume = state.Output[1]
        self.state = state.Output[:1]


class FluidStateTransport(FluidState):
    def __init__(self, state):
        super().__init__(state)
        # ";VIS;TCX;PRANDTL;KV;M;W"
        self.viscosity = state.Output[7]
        self.thermal_conductivity = state.Output[8]
        self.prandtl = state.Output[9]
        self.kin_viscosity = state.Output[10]
        self.molecular_mass = state.Output[11]
        self.speed_of_sound =state.Output[12]
        self.transport = state.Output[7:13]
        self.state = state.Output[:13]


class Fluid:
    """ 
    The Fluid class is used to set, get, and print states of  a fluid with a given
    
    model (e.g. RefProp). The compounds are set in the fluidmodel, while the
    composition is also set here.
    
    """

    def __init__(self, fluidmodel, composition=[1.0],
                 option=1):
        self.fluidmodel = fluidmodel
        self.composition = composition
        self.option = option
        self.no_compounds = len(composition)
        self.herr = 0

    def set_composition(self, composition):
        self.composition = composition
        if self.fluidmodel.props == "TREND":
            # self.comp
            pass # here the mass fraction to internal mol fraction conversion
        
    

    def set_state(self, values, given="TP",
                  wanted=_THERMO_STRING,
                  composition=[]):
        if composition == []:
            composition = self.composition
        else:
            self.composition = composition

        if self.fluidmodel.props == "REFPROP":
            state = self.fluidmodel.rp_instance.REFPROP2dll(
                self.fluidmodel.fluid, given, wanted,
                self.fluidmodel.units,
                0, values[0], values[1],
                composition)

            if state.ierr == 0:
                if wanted == _THERMO_STRING:
                    # print(state)
                    self.properties = FluidState(state)
                elif wanted == _TRANS_STRING:
                    self.properties = FluidStateTransport(state)
                elif wanted == _TV_STRING:
                    self.properties = FluidStateTV(state)
                else:

                    raise Exception(f"properties{wanted} not implemented yet!")
            else:
                self.herr = state.herr
                raise Exception(f"Property-Refprop problem: {state.herr}!")
        else:
            raise Exception(
                f"Property model {self.fluidmodel.props} not implemented yet!")
        return np.array([*self.properties.state])

    def set_state_v(self, values, given="TP", wanted=_THERMO_STRING):
        dimension = np.shape(values)
        number_wanted = wanted.count(";")+1
        output = np.zeros((dimension[0], number_wanted))
        for count, value in enumerate(values):
            output[count, :] = self.set_state(value, given, wanted)
        self.state_v = output
        return output

    def print_state(self):
        pr = self.properties
        flm = self.fluidmodel
        print(f"\n{flm.fluid}, composition: {self.composition}")
        print(f"T:{pr.temperature:.2f} K, p: {pr.pressure/1e5 :.2f} bar,  h: {pr.enthalpy/1000: .2f} kJ/kg, s: {pr.entropy/1000:.3f} kJ/kg K\n")
        if pr.quality >= 0:
            print(f"Quality: {pr.quality :.3f}")
            
    def calc_temp_mean(self, h_final):
        """
        Calculate the thermodynamic mean temperature between the actual state
        
        and the final enthalpy along an isobaric (Delta h /Delta s)

        Parameters
        ----------
        h_final : float
            enthalpy of he final stat.

        Returns
        -------
        temp_mean : float
            the thermodynamic mean temperature.

        """
        actual_props = self.properties.state
        final_props = self.set_state([h_final, actual_props[1]], "HP")
        temp_mean = (final_props[2] - actual_props[2]) \
            / (final_props[4] - actual_props[4]) 
        return temp_mean
    
    
def init_fluid(fluid, composition, **keywords):
    """
    short way to define a Fluid and a FluidModel

    Parameters
    ----------
    fluid : string
        The species within the fluid.
    composition : List
        mole fraction for each fluid.
    **keywords : TYPE
        all keywords needed for the FluidModel, if non-defults shall be set.

    Returns
    -------
    actual_fluid : Fluid
        Instance of the actually set Fluid.

    """
    flm = FluidModel(fluid, **keywords)
    actual_fluid = Fluid(flm, composition)
    return actual_fluid

if __name__ == "__main__":
    FLUID = "Propane * Pentane"
    comp = [.50, 0.5]
    flm = FluidModel(FLUID)
    myFluid = Fluid(flm, comp)
    st0 = myFluid.set_state([300., 1e5], "TP")
    st1 = myFluid.set_state([300., 1e5], "TP",
                            _TRANS_STRING)
    print(st0, st1)
    myFluid.print_state()
    myFluid.set_composition([.2, .8])
    st0 = myFluid.set_state([300., 1e5], "TP", composition=[.35, .65])
    myFluid.print_state()
    
    mean_temp_act = myFluid.calc_temp_mean(st0[2]+1e5)
    print(f"Mean Temperature {mean_temp_act} K")

    # value_vec = np.array([[300, 1e5], [400, 1e5], [500, 1e5]])
    # stv = myFluid.set_state_v(value_vec, "TP")

    # print(myFluid.set_state_v(value_vec, "TP"))
    # print(myFluid.set_state([300., 1.], "TQ"))
    
    # New simple way to get an instance of Fluid
    myFluid2 = init_fluid( FLUID, comp)
