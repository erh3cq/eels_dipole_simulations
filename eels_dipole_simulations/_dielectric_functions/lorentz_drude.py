from hyperspy.component import Component
from traits.api import CBool
from hyperspy.ui_registry import add_gui_method


@add_gui_method(toolkey="eels_dipole_simulations.eps_factorized")
class EpsLorentzDrude(Component):
    '''
    Lorentz-Drude dielectric component.
    
    Input:
    eps_inf: float, int
        The high frequency dielectric constant.
    wLO, wTO: float
        The LO and TO mode energies (default units are eV).
    gamma: float
        The lifetime (default units are eV).
    '''
    
    test_gui = CBool(True)
    
    def __init__(self, eps_inf=1, wLO=171., wTO=93., gamma=1.1):
        # Define the parameters
        Component.__init__(self, ('eps_inf', 'wLO', 'wTO', 'gamma'))
        self._id_name = '838abcb5-0a09-4e8c-b5dd-1f28e77fc475'
        
        #Set the initial values
        self.eps_inf.value = eps_inf
        self.wLo.value = wLO
        self.wTO.value = wTO
        self.gamma.value = gamma
        
        #Set the units
        self.eps_inf.units = None
        self.wLo.units = 'eV'
        self.wTO.units = 'eV'
        self.gamma.units = 'eV'
        
        #Set the bounds
        self.eps_inf.bmin = 1.
        self.wLo.bmin = 0.
        self.wTO.bmin = 0.
        self.gamma.bmin = 0. 
        
        self.eps_inf.bmax = None 
        self.wLo.bmax = None 
        self.wTO.bmax = None  
        self.gamma.bmax = None 
        
        # Define the function as a function of the already defined parameters,
        # x being the independent variable value
        def function(self, x):
            ei = self.eps_inf.value
            wL = self.wLo.value
            wT = self.wTO.value
            g = self.gamma.value
            return ei * (1 + (wL**2 - wT**2) / (wT**2 - E**2 - 1j*g*x)