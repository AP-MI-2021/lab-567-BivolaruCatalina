def do_undo(list_versions: list, current_version: int):
    """
    Daca a fost efectuata o schimbare in lista de vanzari aceasta o anuleaza.
    :param list_versions: lista de versiuni ale listei de vanzari
    :param current_version: numarul de modificari aduse listei
    :return: versiunea neschimbata a ultimei modificari aduse listei de vanzari si numarul de modificari aduse acesteia
    """
    if current_version < 1:
        print("Nu se mai poate face undo!")
        return
    current_version -= 1
    return list_versions[current_version], current_version


def do_redo(list_versions, current_version):
    """
    Daca a fost anulata o schimbare a listei de vanzari, aceasta o efectueaza din nou.
    :param list_versions:  lista de versiuni ale listei de vanzari
    :param current_version:  numarul de modificari aduse listei
    :return: versiunea modificata a listei de vanzari efectuata inainte de anulare si numarul de modificari aduse acesteia
    """
    if current_version == len(list_versions) - 1:
        print("Nu se mai poate face redo!")
        return
    current_version += 1
    return list_versions[current_version], current_version
