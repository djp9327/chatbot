from django.db import connection


def get_response_history(question_id):
    cursor = connection.cursor()
    cursor.execute('''select question_history.question_text, response.response_text from response 
    join question_history
    on question_history.id=response.question_history_id
    where question_history.question_id = %s''', [question_id])
    return cursor.fetchall()