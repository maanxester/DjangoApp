
from .models import User
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_users(request):
    try:
        users = User.objects.all()
        data = {"users": [x.serialized for x in users]}
        if not data:
            return HttpResponseBadRequest
        return JsonResponse(data, status=200)
    except Exception as e:
        return str(e)


@api_view(['POST'])
def create_user(request):
    data = request.data
    if not data:
        return HttpResponseBadRequest(status=400, content_type="json", content="No data provided.")
    user = User(name=data["name"], password=data["password"], admin=data["admin"])
    user.save()
    return Response(user.serialized, status=201)


@api_view(["GET"])
def get_user(request, id):
    user = User.objects.all().filter(id=id)[0]
    if not user:
        return HttpResponseNotFound(status=404, content_type="json", content="User not found.")
    data = {"user": user.serialized}
    if not data:
        return HttpResponseBadRequest(status=400, content_type="json", content="No data provided.")
    return JsonResponse(data, status=200)


@api_view(["DELETE"])
def delete_user(request, id):
    user = User.objects.all().filter(id=id)[0]
    if not user:
        return HttpResponseNotFound(status=404, content_type="json", content="User not found.")
    user.delete()
    return JsonResponse({"status": True})


@api_view(["PUT"])
def update_user(request, id):
    data = request.data
    if not data:
        return HttpResponseBadRequest(status=400, content_type="json", content="No data provided.")
    name = data.get("name")
    if not name:
        return HttpResponseBadRequest(status=400, content_type="json", content="Required to enter valid name")
    password = data.get("password")
    admin = data.get("admin")
    user = User.objects.all().filter(id=id)[0]
    if not user:
        return HttpResponseNotFound(status=404, content_type="json", content="User not found.")

    if name:
        user.name = name
    if password:
        user.password = password
    user.admin = admin

    user.save()
    return JsonResponse(user.serialized)




