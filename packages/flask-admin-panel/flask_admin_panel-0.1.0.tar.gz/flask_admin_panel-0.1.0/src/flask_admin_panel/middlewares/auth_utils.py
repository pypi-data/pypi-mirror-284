import datetime
import os
from functools import wraps
from flask import current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)


def get_user_details():
    users = {}
    if not current_app.config.get("TESTING"):
        APP_ADMIN_USER = current_app.config.get("APP_ADMIN_USER",os.getenv("APP_ADMIN_USER","admin"))
        APP_ADMIN_PASSWORD = current_app.config.get("APP_ADMIN_PASSWORD",os.getenv("APP_ADMIN_PASSWORD"))
        users = {APP_ADMIN_USER: APP_ADMIN_PASSWORD}
    return users

def check_for_valid_user(user, request_data):
    if not user or user != request_data.get("password"):
        return False
    return True


def refresh_access_token(request):
    current_user = get_jwt_identity()
    access_token = create_access_token(
        identity=current_user, expires_delta=datetime.timedelta(minutes=15)
    )
    return access_token


def authenticate_user(request):    
    request_data = request.json
    users = get_user_details()
    user = users.get(request_data.get("username"))
    
    if check_for_valid_user(user, request_data):
        access_token = create_access_token(
            identity={"username": request_data.get("username")},
            expires_delta=datetime.timedelta(minutes=30),
        )
        refresh_token = create_refresh_token(
            identity={"username": request_data.get("username")}
        )
        return access_token, refresh_token
    return None, None
