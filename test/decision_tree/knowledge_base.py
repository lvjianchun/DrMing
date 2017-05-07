from . import decision_tree

def get_decision_tree(sympton='EverythingIsAwsome'):

    root = decision_tree.mock_tree_node(False, "Do you drink yesterday?", \
                                        decision_tree.mock_tree_node(True, "ha...ha..ha..I wonder why?"), \
                                        decision_tree.mock_tree_node(False, "Do you have chest pain?", \
                                                                     decision_tree.mock_tree_node(True, "You have a cold. Drink more water and you will be fine."), \
                                                                     decision_tree.mock_tree_node(True, "I dont know what's wrong with you. Maybe you should use Dr.Ming instead")), \
                          )

    tree = {
        'EverythingIsAwsome' : root
    }

    return tree[sympton]