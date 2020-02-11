''' [======- - - - -=================- All Utilities Standard -=================- - - - -======] '''
# to allow for relative imports
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__))))
''' [======- - - - - - -=============- - - - -========- - - - -=============- - - - - - -======] '''



# test commit 0
def error_if_param_invalid(param, valid_param_l, custom_msg = None):
    if custom_msg == None:
        msg = "ERROR:  Invalid Param.:  " + str(param) + ", must be one of: " + str(valid_param_l)
    else:
        msg = custom_msg
    
    if param not in valid_param_l:
        raise Exception(msg)
    
    
    
if __name__ == '__main__':
    print('In Main:  exception_utils')
    print('End of Main:  exception_utils')