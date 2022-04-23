from flask import jsonify, request

from app.models import Question
from app.api import bp

@bp.route("/question/<int:id>", methods=["GET"])
def get_question(id):
    return jsonify(Question.query.get_or_404(id).to_dict())


@bp.route("/questions", methods=["GET"])
def get_questions():
    subject = request.args.get("subject", default=None, type=str)
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 10, type=int), 100)
    if subject:
        data = Question.to_collection_dict(Question.query.filter(Question.subject.ilike(subject)), page, per_page, "api.get_questions")
    else:
        data = Question.to_collection_dict(Question.query, page, per_page, "api.get_questions")
    return jsonify(data) if data else "{'error': 'an error ocurred'}"