from app.schemas.product import Product


def create_product(product: Product):
    if product.precio < 1000:
        return {
            "error": "El precio debe ser mayor o igual a 1000"
    }
        
    return product