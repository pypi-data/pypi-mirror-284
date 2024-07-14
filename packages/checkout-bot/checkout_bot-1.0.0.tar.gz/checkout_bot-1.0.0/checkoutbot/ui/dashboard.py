from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, session
from datetime import datetime
from checkoutbot.core import start_scraping, search_product_by_keyword
from checkoutbot.ui.utils import (
    load_all_settings, get_template_list,
    load_template, save_template, delete_template, configure_paypal
)
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    loaded_template = session.get('loaded_template')
    if request.method == 'POST':
        if request.form.get('action') == 'start_bot':
            settings = load_all_settings()
            try:
                product_url = settings['scraping'].get('product_url')
                if not product_url:
                    raise KeyError('product_url')
                
                start_datetime = datetime.strptime(f"{settings['scraping']['start_date']} {settings['scraping']['start_time']}", "%Y-%m-%d %H:%M")
                start_scraping(
                    product_url,
                    settings['scraping']['min_price'],
                    settings['scraping']['max_price'],
                    settings['scraping']['quantity'],
                    start_datetime,
                    int(settings['scraping']['duration']),
                    int(settings['scraping']['frequency']),
                    settings['settings'].get('proxies'),
                    settings['settings'].get('enable_ai')
                )
                flash('Bot started successfully!', 'success')
            except KeyError as e:
                flash(f'Missing or invalid data: {str(e)}', 'danger')
                return redirect(url_for('scraping'))
        return redirect(url_for('index'))
    return render_template('index.html', loaded_template=loaded_template)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        enable_proxy = 'enable-proxy' in request.form
        proxies = request.form['proxies'].splitlines() if enable_proxy and request.form['proxies'] else []
        enable_ai = 'ai-simulation' in request.form
        session['settings'] = {
            'enable_proxy': enable_proxy,
            'proxies': proxies,
            'enable_ai': enable_ai
        }
        return redirect(url_for('payment'))
    settings = session.get('settings', {})
    return render_template('settings.html', settings=settings)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        payment_method = request.form['payment-method']
        
        payment_data = {'payment_method': payment_method}

        if payment_method == 'credit-card':
            payment_data.update({
                'card_name': request.form['card-name'],
                'card_number': request.form['card-number'],
                'expiry_date': request.form['expiry-date'],
                'cvv': request.form['cvv'],
                'billing_address': request.form['billing-address']
            })
        elif payment_method == 'paypal':
            paypal_client_id = request.form['paypal-client-id']
            paypal_client_secret = request.form['paypal-client-secret']
            payment_data.update({
                'paypal_client_id': paypal_client_id,
                'paypal_client_secret': paypal_client_secret
            })
            configure_paypal(paypal_client_id, paypal_client_secret)

        session['payment'] = payment_data
        return redirect(url_for('scraping'))
    
    payment_settings = session.get('payment', {})
    return render_template('payment.html', payment_settings=payment_settings)

@app.route('/scraping', methods=['GET', 'POST'])
def scraping():
    if request.method == 'POST':
        search_method = request.form['search-method']
        product_url = request.form['product-url'] if search_method == 'url' else None
        website_url = request.form['website-url'] if search_method == 'name' else None
        product_name = request.form['product-name'] if search_method == 'name' else None
        min_price = request.form['min-price']
        max_price = request.form['max-price']
        quantity = request.form['quantity']
        start_date = request.form['start-date']
        start_time = request.form['start-time']
        duration = request.form['duration']
        frequency = request.form['frequency']

        if search_method == 'name' and website_url and product_name:
            product_url = search_product_by_keyword(website_url, product_name, session.get('settings', {}).get('proxies'))

        start_datetime = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")
        session['scraping'] = {
            'search_method': search_method,
            'product_url': product_url,
            'website_url': website_url,
            'product_name': product_name,
            'min_price': min_price,
            'max_price': max_price,
            'quantity': quantity,
            'start_date': start_date,
            'start_time': start_time,
            'duration': duration,
            'frequency': frequency
        }
        return redirect(url_for('templates'))
    scraping_settings = session.get('scraping', {})
    return render_template('scraping.html', scraping_settings=scraping_settings)

@app.route('/templates', methods=['GET', 'POST'])
def templates():
    templates = get_template_list()  # Ensure this function returns a list of templates
    if request.method == 'POST':
        action = request.form['action']
        template_name = request.form['template-name']
        if action == 'Save Template':
            all_settings = {
                'settings': session.get('settings', {}),
                'payment': session.get('payment', {}),
                'scraping': session.get('scraping', {})
            }
            save_template(template_name, all_settings)
            flash('Template saved successfully!', 'success')
        elif action == 'Load Template':
            try:
                all_settings = load_template(template_name)
                session['settings'] = all_settings['settings']
                session['payment'] = all_settings['payment']
                session['scraping'] = all_settings['scraping']
                session['loaded_template'] = template_name  # Store the loaded template name in the session
                flash('Template loaded successfully!', 'success')
                return redirect(url_for('index'))
            except FileNotFoundError:
                flash('Template not found!', 'danger')
        elif action == 'Delete Template':
            try:
                delete_template(template_name)
                flash('Template deleted successfully!', 'success')
            except FileNotFoundError:
                flash('Template not found!', 'danger')
        elif action == 'Unload Template':
            session.pop('loaded_template', None)
            flash('Template unloaded successfully!', 'success')
        return redirect(url_for('templates'))
    return render_template('templates.html', templates=templates)

@app.route('/get_templates')
def get_templates():
    templates = get_template_list()
    return jsonify({'templates': templates})

@app.route('/unload_template', methods=['POST'])
def unload_template():
    session.pop('loaded_template', None)
    flash('Template unloaded successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
