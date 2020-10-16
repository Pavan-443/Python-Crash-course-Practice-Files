def printing_models(designing_products, completed_products):
    """This function simulates printing of car products"""
    while designing_products:
        current_product = designing_products.pop()
        print(f'{current_product} is printing')
        completed_products.append(current_product)
    return completed_products


def printedproducts(completed_products):
    """This function prints all the printed products"""
    print(f"\nFollowing products are printed: ")
    for completed_product in completed_products:
        print(f'-{completed_product}')