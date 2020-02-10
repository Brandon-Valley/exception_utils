

# test commit 0
def error_if_param_invalid(param, valid_param_l, custom_msg = None):
    if custom_msg == None:
        msg = "ERROR:  Invalid Param.:  " + str(param) + ", must be one of: " + str(valid_param_l)
    else:
        msg = custom_msg
    
    if param not in valid_param_l:
        raise Exception(msg)