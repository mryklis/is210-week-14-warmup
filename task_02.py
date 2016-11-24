#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""this module creates a shopping list"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """set key in shoplist from FRUIT dic

    Args:
        shoplist (dic): dictionary of items

    Returns:
        dictionary of keys and values

    Example:
        >>>get_cost_per_item({'Lime': 12, 'Red Pear': 4,
        'Peach': 24, 'Beet': 1})
        {'Lime': 0.34809999999999997,
        'Peach': 15.920100000000001, 'Red Pear': 6.200100000000001}

    """
    dic = FRUIT
    return {key: FRUIT[key] * dic[key] for key,
            value in shoplist.iteritems() if key in FRUIT}


def get_total_cost(shoplist):
    """cost per item function

    Args:
        shoplist (dic): dic with items

    Returns:
        sum of all values

    Example:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4,
        'Peach': 24, 'Beet': 1})
        22.4683

    """

    shop_list = get_cost_per_item(shoplist)
    return sum([val for val in shop_list.itervalues()])
