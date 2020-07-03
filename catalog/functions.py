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


def get_parents(category):
    list_parents = []
    categories = category.objects.all()

    for category in categories:
        if category.parent is None:
            list_parents.append(category)

    return list_parents


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

    def recursion(obj):
        list_parents.append(obj.slug)

        while obj.parent is not None:
            return recursion(obj.parent)

    recursion(category)
    return list_parents[::-1]


