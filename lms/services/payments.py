from requests import request
import os


def create_payment(price: float) -> dict:
    """ Create payment on stripe """
    # token = os.getenv('STRIPE_TOKEN')
    token = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
    url = "https://api.stripe.com/v1/payment_intents"
    amount = price
    # currency = os.getenv('CURRENCY')
    currency = 'usd'
    payload = f'amount={amount}&currency={currency}&automatic_payment_methods%5Benabled%5D=true' # баг: выдаёт None, если ввести 33
    # payload = f'amount=2000&currency=usd&automatic_payment_methods%5Benabled%5D=true'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': f'Bearer {token}'
    }

    response = request("POST", url, headers=headers, data=payload)

    # print(response.text)
    return response.json().get('id')


def retrieve_payment(stripe_id):
    """ Get payment data: amount_received status [0,1] from stripe """
    # token = os.getenv('STRIPE_TOKEN')
    token = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
    payment_id = stripe_id
    url = f"https://api.stripe.com/v1/payment_intents/{payment_id}"
    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = request("GET", url, headers=headers, data=payload)

    # print(response.text)
    return response.json().get('amount_received')


if __name__ == '__main__':
    payment_id = create_payment(333)
    print(payment_id)

    retrieve_payment_response = retrieve_payment(payment_id)

    print(retrieve_payment_response)
