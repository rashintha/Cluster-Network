import psutil

def get_used_mem():
    return psutil.virtual_memory().used

def get_data():
    return str(get_used_mem())
