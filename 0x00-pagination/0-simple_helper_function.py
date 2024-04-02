#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
    """ returns a tuple """
    new_list = []
    new_list.append((page_size * page) - page_size)
    new_list.append(page_size * page)
    return tuple(new_list)
