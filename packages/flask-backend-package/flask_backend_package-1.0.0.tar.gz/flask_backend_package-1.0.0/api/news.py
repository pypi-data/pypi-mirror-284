from flask import Blueprint, request, jsonify
from models.news import News

news_bp = Blueprint('news', __name__)