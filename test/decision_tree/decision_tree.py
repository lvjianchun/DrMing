class mock_tree_node():

    def __init__(self, is_terminated, question, yes=None, no=None):
        self.is_terminated = is_terminated
        self.question = question
        self.yes = yes
        self.no = no

    def to_string(self):
        return "%s, %s, (%s), (%s)" % (self.is_terminated, self.question, self.yes.question if self.yes is not None else "0", self.no.question if self.no is not None else "0")
