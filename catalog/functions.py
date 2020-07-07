from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_pages(request, objects, count_pages):
    paginator = Paginator(objects, count_pages)
    page = request.GET.get('page')

    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    return page, product


def recursion(obj_parent, all_categories, tree):
    if obj_parent not in tree:
        tree.append(obj_parent)

    for cat in all_categories:
        if cat.parent_id == obj_parent.id:
            recursion(cat, all_categories, tree)


def all_children(parents, categories):
    tree = []

    for parent in parents:
        recursion(parent, categories, tree)
    return tree


def get_tree(categories):
    tree = []
    
    for parent in categories:
        if not parent.parent_id:
            recursion(parent, categories, tree)

    return tree


def all_parents(selected, categories, type_list='obj'):
    list_parents = []

    def search(obj_child, all_categories, list_p):
        if obj_child not in list_p:
            if type_list == 'obj':
                list_p.append(obj_child)
            else:
                list_p.append(obj_child.slug)

        for category in all_categories:
            if category.id == obj_child.parent_id:
                search(category, all_categories, list_p)

    search(selected, categories, list_parents)
    return list_parents[::-1]

