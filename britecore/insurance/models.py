from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class SlugModel(models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True


class RiskType(SlugModel):
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


FIELD_TYPE_TEXT = "text"
FIELD_TYPE_NUMBER = "integer"
FIELD_TYPE_DATE = "date"
FIELD_TYPE_ENUM = "enum"
# FIELD_TYPE_SO_FORTH = "and so forth ;)"

FIELD_TYPES = [
    (FIELD_TYPE_TEXT, _(u"Text Field")),
    (FIELD_TYPE_NUMBER, _(u"Number Field")),
    (FIELD_TYPE_DATE, _(u"Date Field")),
    (FIELD_TYPE_ENUM, _(u"Enum Field")),
    # (FIELD_TYPE_SO_FORTH, _(u"and so forth ;) field type")),
]


class FieldImplementation(models.Model):
    is_active = models.BooleanField(default=False)
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=FIELD_TYPES)
    title = models.CharField(max_length=200)
    is_forced = models.BooleanField(default=False)
    regular_expression = models.CharField(max_length=200, blank=True, default="")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class FieldChoice(models.Model):
    field = models.ForeignKey(FieldImplementation, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
