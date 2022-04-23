from flask import url_for
from app import db


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            "items": [item.to_dict() for item in resources.items],
            "_meta": {
                "page": page,
                "per_page": per_page,
                "total_pages": resources.pages,
                "total_items": resources.total,
            },
            "_links": {
                "self": url_for(endpoint, page=page, per_page=per_page, **kwargs),
                "next": url_for(endpoint, page=page + 1, per_page=per_page, **kwargs)
                if resources.has_next
                else None,
                "prev": url_for(endpoint, page=page - 1, per_page=per_page, **kwargs)
                if resources.has_prev
                else None,
            },
        }
        return data


class Question(db.Model, PaginatedAPIMixin):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200))
    body = db.Column(db.String(800))
    img_link = db.Column(db.String(200))
    alternativeA = db.Column(db.String(300))
    alternativeB = db.Column(db.String(300))
    alternativeC = db.Column(db.String(300))
    alternativeD = db.Column(db.String(300))
    alternativeE = db.Column(db.String(300))
    answer = db.Column(db.String(300))

    def to_dict(self):
        data = {
            "_id": self.id,
            "subject": self.subject,
            "body": self.body,
            "img_link": self.img_link,
            "alternativeA": self.alternativeA,
            "alternativeB": self.alternativeB,
            "alternativeC": self.alternativeC,
            "alternativeD": self.alternativeD,
            "alternativeE": self.alternativeE,
            "answer": self.answer
        }
        return data

    def __repr__(self):
        return f'<Question: {self.id}>'