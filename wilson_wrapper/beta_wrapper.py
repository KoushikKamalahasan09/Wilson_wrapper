import wilson.run.smeft.beta as betamodule
import functools

new_value=0
key_var=""

def configure_patch(key, value):
    global key_var, new_value
    key_var = key
    new_value = value

def beta_editor(key,value):
    
    return new_value

def beta_wrapper(originalbeta):
    @functools.wraps(originalbeta)
    def wrapped_beta(C,Highscale=1,newphys=True):
        Beta=originalbeta(C,Highscale=Highscale,newphys=newphys)
        
        requiredkey=key_var
        
        if requiredkey in Beta:
            Beta[requiredkey]=beta_editor(requiredkey,Beta[requiredkey])
        return Beta
    return wrapped_beta

betamodule.beta=beta_wrapper(betamodule.beta)