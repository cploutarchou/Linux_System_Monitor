from app.helper import *


class Memory:

    def __init__(self):
        info = self.get_memory_details()
        for k, v in info.items():
            print(k,v)
            self.k = v

    @staticmethod
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
