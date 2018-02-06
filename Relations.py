class Relations:

    def __init__(self, parent, child):
        self.__parent = parent
        self.__child = child

    def get_parent(self):
        return self.__parent

    def get_child(self):
        return self.__child

    @staticmethod
    def get_all_children( relationships, parent_name):
        rel_dict = {}
        for rel in relationships:
            if( rel.get_parent() == parent_name):
                rel_dict[ rel.get_child() ] = parent_name
        return rel_dict