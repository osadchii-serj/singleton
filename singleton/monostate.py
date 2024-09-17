class MonostateMeta:

    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(MonostateMeta, cls).__new__(cls)
        obj.__dict__ = cls.__shared_state
        return obj
