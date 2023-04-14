from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def Paginations(request, posts):
    page = request.GET.get("page")
    results = 5
    paginator = Paginator(posts, results)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    leftIndex = (int(page)-4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page)+5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1

    custom_range = range(leftIndex, rightIndex)

    return posts, custom_range