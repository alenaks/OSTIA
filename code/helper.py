def prefix(w):
    ''' Returns a list os prefixes of a word. '''
    
    return [w[:i] for i in range(len(w)+1)]



def lcp(*args):
    ''' Finds longest common prefix of unbounded number of strings strings. '''
    
    w = list(set(i for i in args if i != "*"))
    if not w: raise IndexError("At least one non-unknown string needs to be provided.")
    
    result = ""
    n = min([len(x) for x in w])
    for i in range(n):
        if len(set(x[i] for x in w)) == 1: result += w[0][i]
        else: break
    
    return result



def remove_from_prefix(w, pref):
    ''' Removes a substring from the prefix position of another string. '''
    
    if w.startswith(pref): return w[len(pref):]
    elif w == "*": return w
    else: raise ValueError(pref + " is not a prefix of " + w)
