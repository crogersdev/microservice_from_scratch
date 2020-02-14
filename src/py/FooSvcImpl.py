#!/usr/bin/env python3

"""
file  : api_v1.py
author: Pat Foo
why   : implement business logic of REST endpoint
"""

# python modules

# pip/conda modules

# Foo Inc modules


class FooSvcImpl():
    def __init__(self):
        pass

    def get_foo(self, foo_id):
        print(f"Retriving Foo {foo_id} from database!")
        return f"Foo+{foo_id}"

    def add_foo(self, new_foo):
        pass
