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


    def rewrite(self, w):
        ''' Rewrites the string w with respect to the transducer. '''
        
        if self.Q == None:
            raise ValueError("The transducer needs to be constructed.")
        
        # move through the transducer and write the output
        result = ""
        current_state = ""
        moved = False
        for i in range(len(w)):
            for tr in self.E:
                if tr[0] == current_state and tr[1] == w[i]:
                    result += tr[2]
                    current_state, moved = tr[3], True
                    break
            if moved == False:
                raise ValueError("This string cannot be read by the current transducer.")
                
        # add the final state output
        if self.stout[current_state] != "*":
            result += self.stout[current_state]
            
        return result
        
        
        
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
