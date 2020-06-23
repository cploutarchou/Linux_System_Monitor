#!/usr/bin/env python

import app.memory as mem

details = mem.get_memory_details()
print(details)

# Here we can send the statistics to a server or even locally store the statistics in a database.
