def list_get(input_list, index, default=None):
    """_summary_
    A simple method similar to dict.get(), but for lists ->
        It either returns the element of the input_list (first arg) at index (second arg), if index exists, or None.
        That means: The IndexError exception is handled within this method.
        A different default can be set with the kwarg default=[new default]

    Args:
        input_list (list): _description_
        index (int): _description_
        default (optional): _description_. Defaults to None.

    Returns:
        element of list, if index exists, or None: _description_
    """
    try:
        return input_list[index]
    except IndexError:
        return default
