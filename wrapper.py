import wilson.run.smeft.beta as betamodule
import functools
from collections import OrderedDict

def beta_editor(key,value):
    
    return 0

def beta_wrapper(originalbeta):
    @functools.wraps(originalbeta)
    def wrapped_beta(C,Highscale=1,newphys=True):
        Beta=originalbeta(C,Highscale=Highscale,newphys=newphys)
        
        requiredkey='required key name'
        
        if requiredkey in Beta:
            Beta[requiredkey]=beta_editor(requiredkey,Beta[requiredkey])
        return Beta
    return wrapped_beta

betamodule.beta=beta_wrapper(betamodule.beta)