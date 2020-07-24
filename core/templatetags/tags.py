from django import template
from core.models import Address

register = template.Library()


@register.inclusion_tag('../templates/core/includes/footer.html', takes_context=True)
def get_address(context):
    address = Address.objects.get()
    return {'street': address.street, 'city': address.cityName, 'phone': address.phone,
            'email': address.email}
