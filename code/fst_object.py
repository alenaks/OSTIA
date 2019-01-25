from copy import deepcopy


class FST():
    ''' Generic container class for the FST-related objects.
    * Q: list of states;
    * Sigma: input alphabet;
    * Gamma: output alphabet;
    * qe: initial state (usually "");
    * E: list of transitions;
    * stout: state output dictionary.
    '''
    def __init__(self, Sigma=None, Gamma=None):
        self.Q = None
        self.Sigma = Sigma
        self.Gamma = Gamma
        self.qe = ""
        self.E = None
        self.stout = None
        
        
        
def copy_fst(T_orig):
    ''' We need to be able to do a deep copy of FST in order to backtrack
        efficiently when testing if one subtree can be folded into another.
    '''
    T = FST()
    T.Q = deepcopy(T_orig.Q)
    T.Sigma = deepcopy(T_orig.Sigma)
    T.Gamma = deepcopy(T_orig.Gamma)
    T.E = deepcopy(T_orig.E)
    T.stout = deepcopy(T_orig.stout)
    
    return T
