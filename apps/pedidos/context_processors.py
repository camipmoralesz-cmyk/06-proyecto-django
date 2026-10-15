def carrito_context(request):
    """Permite acceder al numero de figuras en el carrito desde cualquier plantillas"""
    carrito = request.session.get('carrito', {})
    total_items = sum(item.get('cantidad', 0) for item in carrito.values())
    return{
        'carrito_total_items': total_items
    }