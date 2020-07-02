
def list_category(parents):
    sorted_category = []

    def recursion(list_parents):
        for obj in list_parents:
            sorted_category.append(obj)

            try:
                children = obj.children.all()
                recursion(children)
            except AttributeError:
                return None

    recursion(parents)
    return sorted_category


def get_tree(category):
    list_parents = []

    def recursions(obj):
        list_parents.append(obj.slug)

        while obj.parent is not None:
            return recursions(obj.parent)

    recursions(category)
    return list_parents[::-1]


def count_spaces(category):
    spaces = []

    slug = category.get_slug()
    for _ in range(slug.count('/')):
        spaces.append('')

    return spaces


def get_dict(sorted_category):
    dict_category = {}

    for category in sorted_category:
        dict_category[category] = count_spaces(category)

    return dict_category

