from django.shortcuts import get_object_or_404
from rest_framework import generics, parsers, response, status

from brightcore.insurance.models import RiskType
from brightcore.insurance.serializers import RiskTypeSerializer
# Create your views here.


class RiskTypeAPIView(generics.ListAPIView, generics.RetrieveAPIView):
    authentication_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser, parsers.FileUploadParser, )

    serializer_class = RiskTypeSerializer

    def get_queryset(self):
        return RiskType.objects.filter(is_active=True)

    def get(self, *args, **kwargs):
        slug = kwargs.get("slug", "")

        if not slug:
            return super(RiskTypeAPIView, self).get(*args, **kwargs)
        else:
            return response.Response(
                data=RiskTypeSerializer(get_object_or_404(RiskType, slug=slug, is_active=True)).data,
                status=status.HTTP_200_OK
            )
