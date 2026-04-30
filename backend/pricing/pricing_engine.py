
def calculate_price(product):
    base_price = float(product.base_price)
    views = product.views
    purchased = product.purchased
    stock = product.stock

    new_price = base_price
    if views > 0:
        conversion_rate = purchased / views
    else:
        conversion_rate = 0
    
    if conversion_rate  > 0.3:
        new_price *= 1.10
    elif conversion_rate < 0.2 and views > 10:
        new_price *= 0.90

    if purchased > 10:
        new_price *= 1.10
    
    
    if 0 < stock < 5 :
        new_price *= 1.10
    
    if new_price < 0.5 * base_price:
        new_price = 0.5 * base_price
    
    if new_price > 2 * base_price:
        new_price = 2 * base_price

    new_price = round(new_price, 2)

    return new_price