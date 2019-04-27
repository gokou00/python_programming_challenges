def willYou(young, beautiful, loved):
    if young and beautiful and not loved:
        return True
    elif loved and (not young or not beautiful):
        return True
    else:
        return False
    