


def raise_exception_if_param_invalid(param, valid_param_l):
    if param not in valid_param_l:
        raise Exception("ERROR:  Invalid Param.:  " + str(param) + ", must be one of: " + str(valid_param_l))