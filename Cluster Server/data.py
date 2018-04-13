import psutil
import json

def get_used_mem():
    return psutil.virtual_memory().used

def get_total_mem():
    return psutil.virtual_memory().total

def get_used_mem_percentage():
    return psutil.virtual_memory().percent

def get_current_cpu_freq():
    return psutil.cpu_freq().current

def get_max_cpu_freq():
    return psutil.cpu_freq().max

def get_cpu_percentage(current_cpu, max_cpu):
    return current_cpu * 100 / max_cpu

def get_data():

    ram_used = get_used_mem() / (1024 * 1024 * 1024)
    ram_total = get_total_mem() / (1024 * 1024 * 1024)
    ram_percent = get_used_mem_percentage()

    cpu_current = get_current_cpu_freq() / 1000
    cpu_max = get_max_cpu_freq() / 1000
    cpu_percent = get_cpu_percentage(cpu_current - 0.8, cpu_max - 0.8)

    json_obj = json.dumps({"RAM_USED": str("{0:.2f}".format(ram_used)),
        "RAM_TOTAL": str("{0:.2f}".format(ram_total)),
        "RAM_PERCENT": str("{0:.2f}".format(ram_percent)),
        "CPU_CURRENT": str("{0:.2f}".format(cpu_current)),
        "CPU_MAX": str("{0:.2f}".format(cpu_max)),
        "CPU_PERCENT": str("{0:.2f}".format(cpu_percent))
        })

    return json_obj 
