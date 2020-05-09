''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line

util_submodule_l = ['custom_exceptions', 'util_tools__eu']  # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules

# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l

''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''

import custom_exceptions as ce                                         ; util_submodule_import_check_count += 1
import util_tools__eu    as ut                                         ; util_submodule_import_check_count += 1

''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''




        

def error_if_param_type_not_in_whitelist(param, param_type_whitelist, custom_msg = None):
    type_str = str(type(param)).split("'")[1]
    if type_str not in param_type_whitelist:
                    
        default_msg = "ERROR:  Invalid Param Type:  " + str(param) + " is type: " + str(type(param)) + ", must be one of: " + str(param_type_whitelist)            
        msg = ut.get_msg(custom_msg, default_msg)
            
        raise ce.ParamTypeNotInWhitelistError(msg)



def error_if_param_key_not_in_whitelist(param, param_key_whitelist, custom_msg = None):
    if param not in param_key_whitelist:
        
        default_msg = "ERROR:  Invalid Param:  " + str(param) + ", must be one of: " + str(param_key_whitelist)        
        msg = ut.get_msg(custom_msg, default_msg)
         
        raise ce.ParamKeyNotInWhitelistError(msg)   
    

def error_if_path_ext_not_in_whitelist(path, path_ext_whitelist, custom_msg = None):
    '''
        ex:  path_ext_whitelist = [".git", ".png", ...]   
        will treat no extension the same as a wrong extension 
    '''
    extension = ut.get_extension(path)
     
    if extension not in path_ext_whitelist:
     
        default_msg = "ERROR:  Invalid Path Extension:  " + str(path) + ", must end with one of: " + str(path_ext_whitelist)        
        msg = ut.get_msg(custom_msg, default_msg)
        
        raise ce.PathExtensionNotInWhitelistError(msg)
    
    
def error_if_not_is_dir(path, custom_msg = None):
    '''
        No need to check for type
    '''
    if not ut.is_dir(path):
        
        default_msg = 'ERROR:  Directory Does Not Exist:  "' + str(path) + '" must point to an existing directory.'        
        msg = ut.get_msg(custom_msg, default_msg)
         
        raise ce.DirNotExistError(msg)     
    
    
def error_if_not_is_file(path, custom_msg = None):
    '''
        No need to check for type
    '''    
    if not ut.is_file(path):
        
        default_msg = 'ERROR:  File Does Not Exist:  "' + str(path) + '" must point to an existing file.'        
        msg = ut.get_msg(custom_msg, default_msg)
         
        raise ce.FileNotExistError(msg)    
    

def error_if_not_is_file_or_is_dir(path, custom_msg = None):
    '''
        No need to check for type
    '''
    if not (ut.exists(path)):
        
        default_msg = 'ERROR:  FSU Object Does Not Exist:  "' + str(path) + '" must point to an existing file or directory."'        
        msg = ut.get_msg(custom_msg, default_msg)
         
        raise ce.FsuObjNotExistError(msg)      
    
    
def error_if_not_is_abs(path, custom_msg = None):


    
    if not ut.is_abs(path):
        default_msg = 'ERROR:  Path is Not ABS:  "' + str(path) + '" must point to an existing file or directory."'        
        msg = ut.get_msg(custom_msg, default_msg)
         
        raise ce.FsuObjNotExistError(msg)     
        
     
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
#     error_if_not_is_file(44)
    error_if_not_is_abs("C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\version_control_scripts\\CE\\submodules\\exception_utils\\custom_exceptfions.py")
#     error_if_not_is_abs("custom_exceptions.py")
    print('End of Main:  exception_utils')