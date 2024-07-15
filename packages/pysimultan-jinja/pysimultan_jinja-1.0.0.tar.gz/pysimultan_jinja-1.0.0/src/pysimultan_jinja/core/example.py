

class Example(object):

    def __init__(self, *args, **kwargs):

        self.val_a = kwargs.get('val_a', None)
        self.val_b = kwargs.get('val_b', None)
        self.val_c = kwargs.get('val_c', None)
