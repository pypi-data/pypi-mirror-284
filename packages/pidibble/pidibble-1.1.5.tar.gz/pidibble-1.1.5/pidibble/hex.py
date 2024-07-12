__hex_tripped__=False
def str2atomSerial(arg,force=False):
    global __hex_tripped__
    if type(arg)==int and not force: 
        return_object=arg
    # assert type(arg)==str
    # if force or __hex_tripped__ or any([(x in arg) for x in 'abcdef']):
    if force or any([(x in arg) for x in 'abcdef']):
        return_object=int(arg,16)
    else:
        return_object=int(arg)
    if return_object>99999 and not __hex_tripped__:
        __hex_tripped__=True
    return return_object

def hex_reset():
    global __hex_tripped__
    __hex_tripped__=False
