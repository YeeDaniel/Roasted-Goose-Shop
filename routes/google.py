import os
from dotenv import load_dotenv
from google.oauth2 import id_token
from google.auth.transport import requests
from flask import request, render_template, Blueprint, jsonify

google = Blueprint('google', __name__, template_folder='templates')

load_dotenv()
GOOGLE_OAUTH2_CLIENT_ID = os.getenv('GOOGLE_OAUTH2_CLIENT_ID')

@google.route('/')
def index():
    return render_template('google.html', google_oauth2_client_id=GOOGLE_OAUTH2_CLIENT_ID)

@google.route('/google_sign_in', methods=['POST'])
def google_sign_in():
    token = request.json['id_token']

    try:
        # Specify the GOOGLE_OAUTH2_CLIENT_ID of the app that accesses the backend:
        id_info = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_OAUTH2_CLIENT_ID
        )

        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('完了')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        # user_id = id_info['sub']
        # reference: https://developers.google.com/identity/sign-in/web/backend-auth
    except ValueError as exc:
        # Invalid token
        raise ValueError('Token 無效') from exc
    
    print('登入成功')
    return jsonify({}), 200
