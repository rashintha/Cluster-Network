import psutil
import json

def get_used_mem():
    return psutil.virtual_memory().used

def get_total_mem():
    return psutil.virtual_memory().total

def get_user_mem_percentage():
    return psutil.virtual_memory().percent

def get_data():
    return json.dumps({"RAM_USED": str("{0:.2f}".format(get_used_mem() / (1024 * 1024 * 1024))),
        "RAM_TOTAL": str("{0:.2f}".format(get_total_mem() / (1024 * 1024 * 1024))),
        "RAM_PERCENT": str("{0:.2f}".format(get_used_mem_percentage()))
        })
