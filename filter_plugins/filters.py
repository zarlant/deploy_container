def ends_in_slash(arg):
    if arg is not None and arg != "":
        if arg[::1] != "/":
            return "%s/" % arg
    return ""

class FilterModule(object):
    def filters(self):
        return {'ends_in_slash': ends_in_slash}