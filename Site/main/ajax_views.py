from django.contrib.auth.models import User
from django.http import JsonResponse
from main.models import *

"""Кнопки добавления тайтла в списки"""


def content_list_exists(list_type, content, user):
    return ContentList.objects.filter(list_type=ListType.objects.get(title=list_type), content=content,
                                      user=user).exists()


def content_list_add(list_type, content, user):
    obj = ContentList(list_type=ListType.objects.get(title=list_type), content=content, user=user)
    obj.save()


def content_list_delete(list_type, content, user):
    ContentList.objects.get(list_type=ListType.objects.get(title=list_type), content=content, user=user).delete()


def button_handler(button, list_type, content, user):
    if button == 'true':
        if not content_list_exists(list_type, content, user):
            content_list_add(list_type, content, user)
            return True
    else:
        if content_list_exists(list_type, content, user):
            content_list_delete(list_type, content, user)
            return False


def item_ajax_buttons(request):
    user = User.objects.get(username=request.GET.get('user_nickname', None))
    content = Content.objects.get(slug=request.GET.get('content_slug', None))
    like = request.GET.get('like_bool', None)
    watching = request.GET.get('watching_bool', None)
    will_be_watching = request.GET.get('will_be_watching_bool', None)
    abandoned = request.GET.get('abandoned_bool', None)
    response = {
        'like_bool': button_handler(like, 'Любимые', content, user),
        'watching_bool': button_handler(watching, 'Смотрю', content, user),
        'will_be_watching_bool': button_handler(will_be_watching, 'Буду смотреть', content, user),
        'abandoned_bool': button_handler(abandoned, 'Брошено', content, user),
    }
    return JsonResponse(response)


def item_ajax_buttons_validate(request):
    user_name = request.GET.get('user_nickname', None)
    response = {'like_bool': False,
                'watching_bool': False,
                'will_be_watching_bool': False,
                'abandoned_bool': False}
    if not user_name == '':
        user = User.objects.get(username=user_name)
        content = Content.objects.get(slug=request.GET.get('content_slug', None))

        response['like_bool'] = True if content_list_exists('Любимые', content, user) else False
        response['watching_bool'] = True if content_list_exists('Смотрю', content, user) else False
        response['will_be_watching_bool'] = True if content_list_exists('Буду смотреть', content, user) else False
        response['abandoned_bool'] = True if content_list_exists('Брошено', content, user) else False

    return JsonResponse(response)


"""Проверка введённых данных на странице регистрации"""


def registration_form_validate(request):
    user_nickname = request.GET.get('user_nickname', None)
    user_email = request.GET.get('user_email', None)
    response = dict()

    response['user_nickname'] = User.objects.filter(username=user_nickname).exists()
    response['user_email'] = User.objects.filter(email=user_email).exists()

    return JsonResponse(response)


"""Сохранение комментария"""


def create_comment(request):
    user = User.objects.get(username=request.GET.get('user_nickname', None))
    content = Content.objects.get(slug=request.GET.get('content_slug', None))
    comment_text = request.GET.get('comment_text', None)
    reply_to_nickname = request.GET.get('reply_to_nickname', None)
    obj = None

    try:
        response_to_comment = Comments.objects.get(id=request.GET.get('reply_to_comment_id', None))
        obj = Comments(user_commentator=user,
                       content=content,
                       comment_text=comment_text,
                       response_to_comment=response_to_comment)
    except:
        obj = Comments(user_commentator=user, content=content, comment_text=comment_text)
        print("Shit code")

    response = dict()

    obj.save()
    comment = {
        "user_commentator": obj.user_commentator.username,
        "comment_text": obj.comment_text,
        "created_at": obj.created_at,
        "reply_to_nickname": reply_to_nickname,
        "id": obj.id
    }
    response['comment'] = comment

    return JsonResponse(response)


"""Вывод комментариев"""


def view_comment(request):
    user = User.objects.get(username=request.GET.get('user_nickname', None))
    content = Content.objects.get(slug=request.GET.get('content_slug', None))
    c_num = int(request.GET.get('comments_number', None))
    c_num_next7 = c_num + 7
    response = dict()
    comments = list()

    objs = Comments.objects.filter(user_commentator=user, content=content, response_to_comment__isnull=True).order_by('-created_at')[c_num:c_num_next7]
    for obj in objs:
        responses = list()
        if Comments.objects.filter(response_to_comment=obj.id).exists:
            for el in Comments.objects.filter(response_to_comment=obj.id):
                child = {
                    "user_commentator": el.user_commentator.username,
                    "comment_text": el.comment_text,
                    "created_at": el.created_at,
                    "id": el.id,
                }
                responses.append(child)
        comment = {
            "user_commentator": obj.user_commentator.username,
            "comment_text": obj.comment_text,
            "created_at": obj.created_at,
            "id": obj.id,
            "responses": responses
        }
        comments.append(comment)

    response["comments"] = comments

    return JsonResponse(response)


"""Вывод ответтов на комментарий"""


def view_response_comment(request):
    response = dict()

    return JsonResponse(response)
