
def get_memory_details():
    memory_details = {}
    with open("/proc/meminfo", "r") as file:
        lines = file.readlines()
        for row in lines:
            row = row.strip()
            row = row.split()
            row = {row[0]: row[1]}
            memory_details.update(row)
    return memory_details
