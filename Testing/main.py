def calc_pow(a=0, b=0):
    try:
        if a and b:
            return int(a) ** int(b)
        else:
            return 'Both need to be a number'
    except ValueError as err:
        return err
    except TypeError as err:
        return err
