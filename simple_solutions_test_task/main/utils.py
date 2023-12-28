import stripe


stripe.api_key = "sk_test_51ORpzDKmJF1wZ1wl48hIxBZivBiKUuQNxeuazfBbFKKig4b7Q1UOPYQvM8waZOtBhSuArrwVb0lximmvc3UWMf3f00cBhtWXn6"


def stripe_session_create(obj):
    session_id = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price_data": {
            "product_data": {"name": obj.name},
            "unit_amount_decimal": obj.price * 100,
            "currency": "RUB"
        }, "quantity": 1}],
        mode="payment"
     )

    return session_id
