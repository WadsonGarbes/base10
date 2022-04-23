from app import db
from app.models import Question

question = Question(
    subject="Português", 
    body="A internet proporcionou o surgimento de novos paradigmas sociais e impulsionou a modificação de outros já estabelecidos nas esferas da comunicação e da informação. A principal consequência criticada na tirinha sobre esse processo é a",
    img_link="https://static.todamateria.com.br/upload/qu/es/questao19-cke.jpg",
    alternativeA="criação de memes.",
    alternativeB="ampliação da blogosfera.",
    alternativeC="supremacia das ideias cibernéticas.",
    alternativeD="comercialização de pontos de vista",
    alternativeE="banalização do comércio eletrônico.",
    answer="d) comercialização de pontos de vista."
)

db.session.add(question)
db.session.commit()
db.session.close()