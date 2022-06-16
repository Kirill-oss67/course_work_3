class ItemNotFound(Exception):
    ...


class UserNotFound(ItemNotFound):
    pass

class WrongPassword(ItemNotFound):
    pass