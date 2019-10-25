from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Inventory.models import ItemType
from Inventory.serializers import ItemTypeSerializer


class JSONResponse(HttpResponse):
    """
    HttpResponse, который отображает его содержимое в JSON
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def item_type_list(request):
    """
    Отобразить все коды ItemTypes, или создать новый ItemType.
    """
    if request.method == 'GET':
        snippets = ItemType.objects.all()
        serializer = ItemTypeSerializer(snippets, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def item_type_detail(request, pk):
    """
    Извлечение, обновление или удаление фрагмента кода.
    """
    try:
        item_type = ItemType.objects.get(pk=pk)
    except ItemType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemTypeSerializer(item_type)
        return HttpResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemTypeSerializer(item_type, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item_type.delete()
        return HttpResponse(status=204)
