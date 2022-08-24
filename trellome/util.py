#!/usr/bin/env python3

def chain_or(*fn_args):
    for func in fn_args:
        if func():
            return True

    return False

def regex_match_with_prop(prop_name: str, rgx, dic_val):
    return lambda: prop_name in dic_val and \
                None != rgx.match(dic_val[prop_name] or "")
