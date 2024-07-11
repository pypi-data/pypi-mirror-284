from flask import Blueprint, request, jsonify
from models.feedback import Feedback

feedbacks_bp = Blueprint('feedbacks', __name__)
