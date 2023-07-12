from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.cache import cache

from core import models, serializers, utils


class CustomerAPIView(views.APIView):
    serializer_class = serializers.Customer
    queryset = models.Customer.objects.prefetch_related('deals').annotate(
        spent_money=Sum('deals__total')).order_by('-spent_money')[:5]
    permission_classes = (AllowAny,)

    def get(self, request: Request) -> Response:
        if data := cache.get('customer'):
            return Response({'response': data})

        common_gems = utils.get_common_gems(queryset=self.queryset)
        data = self.serializer_class(
            self.queryset.all(), many=True, context={'common_gems': common_gems}
        ).data

        cache.set('customer', data, None)
        return Response({'response': data})


class DealFileUploadAPIView(views.APIView):
    serializer_class = serializers.DealFile
    parser_classes = (MultiPartParser,)
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        utils.parse_csv(file=serializer.validated_data['deals'])
        return Response({'Status': 'OK'})
