from hyperspy.component import Component
from traits.api import CBool
from hyperspy.ui_registry import add_gui_method


@add_gui_method(toolkey="hspy_ext.eps_factorized")
class EpsFactorized(Component):
    '''
    Factorized dielectric component.
    
    Input:
    eps_inf: float, int
        The high frequency dielectric constant.
    wLO, wTO: float
        The LO and TO mode energies (default units are eV).
    gLO, gTO: float
        The LO and TO mode lifetime (default units are eV).
    '''
    
    test_gui = CBool(True)
    
    def __init__(self, eps_inf=1, wLO=171., gLO=1.1, wTO=93., gTO=20.):
        # Define the parameters
        Component.__init__(self, ('eps_inf', 'wLO', 'gLO', 'wTO', 'gTO'))
        self._id_name = 'd56098f3-cb7a-4313-8aca-9862344be0d0'
        
        #Set the initial values
        self.eps_inf.value = eps_inf
        self.wLo.value = wLO
        self.gLO.value = gLO
        self.wTO.value = wTO
        self.gTO.value = gTO
        
        #Set the units
        self.eps_inf.units = None
        self.wLo.units = 'eV'
        self.gLO.units = 'eV'
        self.wTO.units = 'eV'
        self.gTO.units = 'eV'
        
        #Set the bounds
        self.eps_inf.bmin = 1.
        self.wLo.bmin = 0.
        self.gLO.bmin = 0.
        self.wTO.bmin = 0.
        self.gTO.bmin = 0. 
        
        self.eps_inf.bmax = None 
        self.wLo.bmax = None 
        self.gLO.bmax = None 
        self.wTO.bmax = None  
        self.gTO.bmax = None 
        
        # Define the function as a function of the already defined parameters,
        # x being the independent variable value
        def function(self, x):
            ei = self.eps_inf.value
            wL = self.wLo.value
            gL = self.gLO.value
            wT = self.wTO.value
            gT = self.gTO.value
            return ei * (wL**2 - E**2 - 1j*gL*x) / (wT**2 - E**2 - 1j*gT*x)