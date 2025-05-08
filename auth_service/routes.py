from flask import Blueprint, request, jsonify
from models import User
from extensions import db, bcrypt  # ✅ cambia esto
from auth_utils import generate_token
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "Email already exists"}), 400
    # En /register
    hashed_pw = generate_password_hash(
        data["password"], method='pbkdf2:sha256')
    new_user = User(name=data["name"], email=data["email"], password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    # En /login
    if user and check_password_hash(user.password, data["password"]):
        token = generate_token(identity=user.email)
        return jsonify({"token": token}), 200
    return jsonify({"msg": "Invalid credentials"}), 401


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Hello {current_user}!"}), 200
