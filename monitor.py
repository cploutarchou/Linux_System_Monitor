#!/usr/bin/env python

import app.memory as mem


def get_statistics():
    mem.memory()


statistics = get_statistics()

# Here we can send the statistics to a server or even locally store the statistics in a database.
