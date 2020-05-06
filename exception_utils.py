''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line

util_submodule_l = ['custom_exceptions']  # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules

# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l

''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''

import custom_exceptions as ce                                         ; util_submodule_import_check_count += 1

''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''

''' Internal '''
def get_msg(custom_msg, default_msg):    
    if custom_msg == None:
        return default_msg
    else:
        return custom_msg
        

def error_if_param_type_not_in_whitelist(param, param_type_whitelist, custom_msg = None):
    type_str = str(type(param)).split("'")[1]
    if type_str not in param_type_whitelist:
                    
        default_msg = "ERROR:  Invalid Param Type:  " + str(param) + " is type: " + str(type(param)) + ", must be one of: " + str(param_type_whitelist)            
        msg = get_msg(custom_msg, default_msg)
            
        raise ce.ParamTypeNotInWhitelistError(msg)



def error_if_param_key_not_in_whitelist(param, param_key_whitelist, custom_msg = None):
    if param not in param_key_whitelist:
        
        default_msg = "ERROR:  Invalid Param:  " + str(param) + ", must be one of: " + str(param_key_whitelist)        
        msg = get_msg(custom_msg, default_msg)
         
        raise ce.ParamKeyNotInWhitelistError(msg)
    

# ex:  path_ext_whitelist = [".git", ".png", ...]   
# will treat no extension the same as a wrong extension 
def error_if_path_ext_not_in_whitelist(path, path_ext_whitelist, custom_msg = None):
    extension = os.path.splitext(path)[1]
     
    if extension not in path_ext_whitelist:
     
        default_msg = "ERROR:  Invalid Path Extension:  " + str(path) + ", must end with one of: " + str(path_ext_whitelist)        
        msg = get_msg(custom_msg, default_msg)
        
        raise ce.PathExtensionNotInWhitelistError(msg)
    
     
# raises exception if all keys == their values in param_combo_d    
# {log_file_path : None, print_output : False}
def error_if_forbidden_param_val_combo(param_combo_d, reason = None, custom_msg = None):
    raise_error = True
     
    for param, value in param_combo_d.items():
        if param != value:
            raise_error = False
            break
         
    if raise_error:
        if custom_msg == None:
            msg = 'Param Combo Forbidden.'
                 
            if reason != None:
                msg += '\nForbidden Because:  ' + reason
        else:
            msg = custom_msg
        raise ce.ForbiddenParamValComboError(msg)
         
     
     
     
     
     
     
     
     
''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Footer -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
sys.modules = og_sys_modules
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if __name__ == '__main__':
    print('In Main:  exception_utils')
    print('End of Main:  exception_utils')