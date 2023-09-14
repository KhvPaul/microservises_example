from django.shortcuts import render

# Create your views here.


def view(request):
    data = request.body
    order = Order.obj.create(
        user_email=data.get("user_email"), status=data.get("status"), delivery_address=data.get("delivery_address")
    )
    for item in data.get("book_items"):
        order_item = OrderItem.obj.create(
            order_id=order.pk, book_store_id=item.get("book_store_id"), quentity=item.get("quentity")
        )
        book = Book.obj.get(pk=book_store_id)
        book.quentity -= item.get("quentity")
        book.save()
