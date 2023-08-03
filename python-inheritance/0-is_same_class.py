def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a class

    Args:
        obj: An object instance
        a_class: A class

    Returns:
        True: If object is exactly an instance of the class
        False: If object is not exactly an instance of the class
    """
    return type(obj) is a_class
