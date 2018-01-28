





def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

menu = {
    'name': 'Quinoa dish', 'price': 500,

}

x = apply_discount(menu, 0.25)
print(x)

# DO NOT USE ASSERTIONS TO VALIDATE DATA - assertions can be disabled in Python interpreter

def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin to delete')
    if not store.has_product(product_id):
        raise ValueError('Unknown product id')
    store.get_product(product_id).delete()



