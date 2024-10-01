from django import template
register = template.Library()

@register.filter(name='is_cart')
def is_cart(product,cart):
    print(cart.keys())
    keys=cart.keys()
    for id in keys:
        if id == str(product.id):
            return True
    # print(product,cart)


    return False
