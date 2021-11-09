def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    :param undo_list:
    :param redo_list:
    :return:
    """
    if undo_list:
        top_undo = undo_list.pop()  # top_undo[0] = f_lambda
        redo_list.append(top_undo)
        return top_undo[0](current_list)  # return f_lambda()

    return None