from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Box, Order


# -----------------------------------
# Home Page
# -----------------------------------
def home(request):
    products = Product.objects.all()

    return render(request, "index.html", {
        "products": products
    })


# -----------------------------------
# Recommend box for a single product
# -----------------------------------
def recommend_box(request, product_id):

    product = Product.objects.get(id=product_id)

    suitable_boxes = []

    for box in Box.objects.all():

        if (
            box.internal_length >= product.length
            and box.internal_width >= product.width
            and box.internal_height >= product.height
            and box.max_weight >= product.weight
        ):
            suitable_boxes.append(box)

    if suitable_boxes:

        best_box = min(
            suitable_boxes,
            key=lambda x: x.cost
        )

        return render(request, "result.html", {
            "product": product,
            "box": best_box
        })

    return render(request, "result.html", {
        "product": product,
        "box": None
    })


# -----------------------------------
# Recommend box for complete order
# -----------------------------------
def order_recommendation(request, order_id):

    order = Order.objects.get(id=order_id)

    total_weight = 0
    products = []

    # Collect order products
    for item in order.items.all():

        product = item.product

        total_weight += (
            product.weight *
            item.quantity
        )

        products.append({
            "name": product.name,
            "quantity": item.quantity,
            "length": product.length,
            "width": product.width,
            "height": product.height,
            "weight": product.weight
        })

    suitable_boxes = []

    # Check available boxes
    for box in Box.objects.all():

        can_fit = True

        # Check product dimensions
        for item in order.items.all():

            product = item.product

            if (
                box.internal_length < product.length
                or box.internal_width < product.width
                or box.internal_height < product.height
            ):
                can_fit = False
                break

        # Check maximum weight
        if box.max_weight < total_weight:
            can_fit = False

        if can_fit:
            suitable_boxes.append(box)

    if suitable_boxes:

        best_box = min(
            suitable_boxes,
            key=lambda x: x.cost
        )

        return JsonResponse({

            "order_id": order.id,

            "products": products,

            "recommended_boxes": [
                {
                    "box_name": best_box.name,
                    "quantity": 1
                }
            ],

            "total_cost": float(best_box.cost)

        })

    return JsonResponse({
        "message": "No suitable box available"
    })