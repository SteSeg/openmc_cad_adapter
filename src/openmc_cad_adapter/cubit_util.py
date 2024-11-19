_CUBIT_ID = 1


def reset_cubit_ids():
    """Reset the cubit id counter to 1.
    """
    global _CUBIT_ID
    _CUBIT_ID = 1


def lastid():
    """Get the last cubit id and increment the counter by 1.

    Returns
    -------
    int
        The last cubit id incremented by 1.
    """
    global _CUBIT_ID
    id_out = _CUBIT_ID
    _CUBIT_ID += 1
    return id_out


def new_variable():
    idn = lastid()
    return f"id{idn}"


def emit_get_last_id(type="body", cmds=None):
    idn = lastid()
    ids = f"id{idn}"
    if cmds is not None:
        # double {{}} means it is code relevant to a preprocessing step
        cmds.append(f'#{{ {ids} = Id("{type}") }}')
    else:
        print('Warning: cmds is None')
    return ids
