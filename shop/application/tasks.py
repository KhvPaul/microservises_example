


def sync_orders(id_: int):
    order = Order.obj.get(pk=id_)
    data = {
        "user_email": order.user.email,
        "status": order.status,
        "delivery_address": order.delivery_address,
        "order_id_in_shop": order.pk,
        "book_items": [
            {
                "book_store_id": item.book.id_in_store,
                "quantity": item.quantity,
            } for item in order.order_items
        ],
    }
    request.post("warehouse:8001/sync_order/", json=data)
