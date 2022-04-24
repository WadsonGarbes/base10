from app import create_app, db
from app.models import Question
from app.integrator import integrate_questions

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Question": Question
    }
    
@app.cli.command("integrate")
def integrate_round_12():
    """populates database with some questions"""
    print("Integrating companies and roles")
    integrate_questions()
    print("Integration OK")