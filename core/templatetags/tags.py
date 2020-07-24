from django import template
from django.core.exceptions import ObjectDoesNotExist

from core.models import Address

register = template.Library()


@register.inclusion_tag('../templates/core/includes/footer.html', takes_context=True)
def get_address(context):
    try:
        address = Address.objects.get()
        data = {'street': address.street, 'city': address.cityName, 'phone': address.phone,
                'email': address.email}
    except ObjectDoesNotExist:
        data = {}
    return data
