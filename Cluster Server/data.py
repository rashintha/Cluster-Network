import psutil

def get_used_mem():
    return psutil.virtual_memory().used

def get_data():
    return str("{0:.2f}".format(get_used_mem() / (1024 * 1024 * 1024))) + " GB"
