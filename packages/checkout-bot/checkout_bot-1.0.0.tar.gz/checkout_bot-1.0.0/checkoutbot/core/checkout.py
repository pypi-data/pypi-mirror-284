import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def process_checkout(product_url, payment_details, user_details, proxies=None):
    """
    Automate the checkout process for a given product.

    Args:
        product_url (str): The URL of the product to purchase.
        payment_details (dict): Payment information (e.g., card number, expiry date, or PayPal credentials).
        user_details (dict): User information (e.g., shipping address, contact).
        proxies (dict): Optional. Proxies to use for the browser.

    Returns:
        bool: True if checkout was successful, False otherwise.
    """
    try:
        options = webdriver.ChromeOptions()
        if proxies:
            options.add_argument(f'--proxy-server={proxies["http"]}')
        driver = webdriver.Chrome(options=options)
        driver.get(product_url)

        # Example of form filling, this will vary depending on the website
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'quantity'))
        ).send_keys('1')
        driver.find_element(By.NAME, 'add-to-cart').click()

        # Proceed to checkout
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'checkout'))
        ).click()

        if payment_details['payment_method'] == 'credit-card':
            # Fill in credit card details
            driver.find_element(By.NAME, 'card_number').send_keys(payment_details['card_number'])
            driver.find_element(By.NAME, 'expiry_date').send_keys(payment_details['expiry_date'])
            driver.find_element(By.NAME, 'cvv').send_keys(payment_details['cvv'])
            driver.find_element(By.NAME, 'place_order').click()
        
        elif payment_details['payment_method'] == 'paypal':
            # Process payment with PayPal
            if not process_paypal_payment(payment_details):
                return False

            # Continue with the remaining steps of the checkout
            driver.find_element(By.NAME, 'paypal_continue').click()
            driver.find_element(By.NAME, 'place_order').click()

        # Verify success
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'success-message'))
        )
        return True if success_message else False
    except Exception as e:
        print(f"Error during checkout: {e}")
        return False
    finally:
        driver.quit()

def process_paypal_payment(payment_details):
    """
    Processes a payment using PayPal's API.

    Args:
        payment_details (dict): PayPal payment information.

    Returns:
        bool: True if payment was successful, False otherwise.
    """
    try:
        url = "https://api.sandbox.paypal.com/v1/oauth2/token"
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en_US"
        }
        data = {
            "grant_type": "client_credentials"
        }
        response = requests.post(url, headers=headers, data=data, auth=(payment_details['paypal_client_id'], payment_details['paypal_client_secret']))

        if response.status_code != 200:
            print("Error obtaining PayPal token:", response.json())
            return False

        access_token = response.json()['access_token']

        # Create a payment
        payment_url = "https://api.sandbox.paypal.com/v1/payments/payment"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        payment_data = {
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": "10.00",
                    "currency": "USD"
                },
                "description": "This is the payment transaction description."
            }],
            "redirect_urls": {
                "return_url": "https://example.com/your_redirect_url/",
                "cancel_url": "https://example.com/your_cancel_url/"
            }
        }

        payment_response = requests.post(payment_url, headers=headers, json=payment_data)

        if payment_response.status_code != 201:
            print("Error creating PayPal payment:", payment_response.json())
            return False

        approval_url = next(link['href'] for link in payment_response.json()['links'] if link['rel'] == 'approval_url')
        print("Please approve the payment by visiting this URL:", approval_url)

        # Ideally, you'd redirect the user to approval_url and handle the return URL to complete the payment

        return True

    except Exception as e:
        print(f"Error during PayPal payment: {e}")
        return False
