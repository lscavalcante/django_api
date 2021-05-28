from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from drf_yasg import openapi
from rest_framework import generics, views
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from drf_yasg.utils import swagger_auto_schema

from apps.example_model.models import ExampleModel
from apps.example_model.serializer import ExampleModelSerializer, ExampleModelCreateTestSerializer


class ExampleModelViewSet(ModelViewSet):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

    # esse me gera o link do endpoint que nāo aparece na doc do swagger
    @action(methods=['post'], detail=False, serializer_class=ExampleModelCreateTestSerializer)
    def follow(self, request, *args, **kwargs):
        current_side = get_current_site(request=request).domain
        relativeLink = reverse('examplemodel-follow-params', kwargs={'id': 2})

        base_url = 'http://' + current_side + relativeLink
        data = {
            'link': base_url,
            'status': True
        }
        return Response(data)

    @swagger_auto_schema(auto_schema=None)
    @action(methods=['post'], detail=False, serializer_class=ExampleModelCreateTestSerializer, url_path='follow-params/(?P<id>\d+)')
    def follow_params(self, request, id=None):
        print(id)
        data = {
            'link': 'BLZ',
            'status': True
        }
        return Response(data)

# sera gerado automaticamente o endpoint de listagem e criaçāo
class ExampleModelListApi(ListCreateAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

# ele nāo herda nenhum metodo
# nāo será gerado automaticamente nenhum endpoint
class ExampleGenericApi(GenericViewSet):
    serializer_class = ExampleModelSerializer
    queryset = ExampleModel.objects.all()

    @action(methods=['post'], detail=False, serializer_class=ExampleModelCreateTestSerializer)
    def genericviewset_1(self, request, *args, **kwargs):
        data = {
            'generic': True
        }
        return Response(data)

    @action(methods=['post'], detail=False, serializer_class=ExampleModelCreateTestSerializer)
    def genericviewset_2(self, request, *args, **kwargs):
        data = {
            'generic': True
        }
        return Response(data)

# ele nāo herda nenhum metodo
# nāo será gerado automaticamente nenhum endpoint caso vc envie o basename no arquivo de url nāo será solicitado queryset
class ExampleViewSet(ViewSet):
    serializer_class = ExampleModelSerializer

    @action(methods=['post'], detail=False, serializer_class=ExampleModelCreateTestSerializer)
    def viewset_1(self, request, *args, **kwargs):
        data = {
            'viewset': True
        }
        return Response(data)

    @action(methods=['post'], detail=False, serializer_class=ExampleModelCreateTestSerializer)
    def viewset_2(self, request, *args, **kwargs):
        data = {
            'viewset': True
        }
        return Response(data)

    # usado apenas para adicionar um query string na hora de realizar a busca exemplo http://127.0.0.1:8000/example-model/v3/viewset_3/?token=1
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    @action(methods=['get'], detail=False, serializer_class=ExampleModelCreateTestSerializer)
    def viewset_3(self, request, *args, **kwargs):
        # para recuperar o dado
        request.GET.get('token')
        data = {
            'viewset': True,
            'parames': request.GET.get('token')
        }
        return Response(data)

# este n funciona o metodo @action apenas as classes padrao get, post e etc...
class ExampleApiView(views.APIView):
    serializer_class = ExampleModelSerializer

    def get(self, request):

        return Response({'cotent': 'ok'})

    def post(self, request):
        return Response({'cotent': 'ok'})