

# use when you have a function that has a set of incompatible 
# parameter options you would like to protect against
class ForbiddenParamValComboError(Exception): pass


class ParamKeyNotInWhitelistError(Exception): pass

class ParamTypeNotInWhitelistError(Exception): pass