import json
import os
import paypalrestsdk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

os.makedirs(DATA_DIR, exist_ok=True)

def load_all_settings():
    settings_path = os.path.join(DATA_DIR, 'config.json')
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            return json.load(f)
    return {}

def save_all_settings(all_settings):
    settings_path = os.path.join(DATA_DIR, 'config.json')
    with open(settings_path, 'w') as f:
        json.dump(all_settings, f)
    print('Settings saved:', all_settings)  

def get_template_list():
    templates = [f.split('.')[0] for f in os.listdir(DATA_DIR) if f.endswith('.json')]
    return templates

def load_template(template_name):
    template_path = os.path.join(DATA_DIR, f'{template_name}.json')
    if os.path.exists(template_path):
        with open(template_path, 'r') as f:
            return json.load(f)
    raise FileNotFoundError(f"Template '{template_name}' not found.")

def save_template(template_name, all_settings):
    with open(os.path.join(DATA_DIR, f'{template_name}.json'), 'w') as f:
        json.dump(all_settings, f)
    print(f"Template '{template_name}' saved.")

def delete_template(template_name):
    template_path = os.path.join(DATA_DIR, f'{template_name}.json')
    if os.path.exists(template_path):
        os.remove(template_path)
        print(f"Template '{template_name}' deleted.")
    else:
        raise FileNotFoundError(f"Template '{template_name}' not found.")

def configure_paypal(client_id, client_secret):
    paypalrestsdk.configure({
        "mode": "sandbox",  # or "live" for production
        "client_id": client_id,
        "client_secret": client_secret
    })
