from rest_framework import serializers

from britecore.insurance.models import RiskType, FieldImplementation, FieldChoice, FIELD_TYPE_ENUM


class FieldChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldChoice
        fields = ("id", "title")


class FieldImplementationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldImplementation
        fields = ("id", "title", "type")


class EnumFieldImplementationSerializer(FieldImplementationSerializer):
    fieldchoice_set = FieldChoiceSerializer(many=True)

    class Meta:
        model = FieldImplementationSerializer.Meta.model
        fields = FieldImplementationSerializer.Meta.fields + ("fieldchoice_set", )


class RiskTypeSerializer(serializers.ModelSerializer):
    fieldimplementation_set = serializers.SerializerMethodField()

    def get_fieldimplementation_set(self, obj):
        data = []

        for fi in obj.fieldimplementation_set.filter(is_active=True):
            if fi.type == FIELD_TYPE_ENUM:
                data.append(EnumFieldImplementationSerializer(fi).data)
            else:
                data.append(FieldImplementationSerializer(fi).data)

        return data

    class Meta:
        model = RiskType
        fields = ("id", "slug", "title", "fieldimplementation_set")
