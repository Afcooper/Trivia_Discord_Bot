import sqlite3
import os
from sqlite.sql_statements import sql_create_users_table, sql_create_questions_table, sql_create_trivia_game_table \
    , sql_insert_trivia_game, sql_insert_question, sql_get_question_by_title, sql_insert_user, \
    sql_get_user_by_full_name, sql_update_user_results


class TriviaDatabase:
    def __init__(self):
        self.db_path = self.get_db_path()
        self.connection = self.create_connection()
        self.create_trivia_db()
        self.create_all_trivia_tables()

    def get_db_path(self):
        current_dir = os.getcwd()
        trivia_db_path = os.path.normpath(os.path.join(current_dir, 'sqlite/trivia.db'))
        return trivia_db_path

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(self.db_path)
            print(sqlite3.version)
            return conn
        except Exception as e:
            print(e)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            print(f'Creating table with sql: \n {create_table_sql}')
            c = self.connection.cursor()
            c.execute(create_table_sql)
            print(f'Finished creating table...')
        except Exception as e:
            print(e)

    def create_trivia_db(self):
        print(f"creating a trivia db at {self.db_path}")
        self.connection.execute("PRAGMA foreign_keys = ON;")

    def create_all_trivia_tables(self):
        if self.connection is not None:
            self.create_table(sql_create_users_table)
            self.create_table(sql_create_trivia_game_table)
            self.create_table(sql_create_questions_table)
            self.connection.commit()
            # self.create_table(sql_create_questions_answers_table)
        else:
            print("Error! cannot create the database connection.")

    def insert_trivia_game(self, trivia_game):
        query = sql_insert_trivia_game(
            category=quote(trivia_game.type_of_trivia),
            num_of_questions=trivia_game.num_of_questions,
            seconds_per_question=trivia_game.seconds_per_question,
            is_complete=trivia_game.is_complete,
            begin_date=quote(trivia_game.created_date),
            end_date=quote(trivia_game.end_date),
        )
        self.connection.execute(query)
        self.connection.commit()

    def insert_user(self, user):
        if self.get_user(user.full_name) is not None:
            return
        query = sql_insert_user.format(
            full_name=quote(user.full_name),
            username=quote(user.username),
            discriminator=quote(user.discriminator),
            points=user.points,
            questions_correct=user.questions_correct,
            questions_answered=user.questions_answered,
            begin_date=quote(user.begin_date),
            end_date=quote(user.end_date),
        )
        self.connection.execute(query)
        self.connection.commit()
        print(f"Successfully inserted new user {user.full_name} into database.")

    def get_user(self, full_name):
        query = sql_get_user_by_full_name.format(
            full_name=quote(full_name)
        )
        results = self.connection.execute(query).fetchone()
        return results

    def get_question(self, question):
        query = sql_get_question_by_title.format(
            title=quote(question.title),
            category=quote(question.category)
        )
        results = self.connection.execute(query).fetchone()
        return results

    def add_question(self, question) -> bool:
        if self.get_question(question) is not None:
            return False
        query = sql_insert_question.format(
            title=quote(question.title),
            category=quote(question.category),
            answer1=quote(question.answer1),
            answer2=quote(question.answer2),
            answer3=quote(question.answer3),
            answer4=quote(question.answer4),
            correct_answer=question.correct_answer,
            created_by=quote(question.created_by)
        )
        self.connection.execute(query)
        self.connection.commit()
        print(f"created question {question.title} by user {question.created_by}")
        return True

    def update_user_score(self, full_name, points: int=0, questions_correct: int=0, questions_answered: int=0):
        user_details = self.get_user(full_name)
        print(user_details)
        user_points = user_details[4]
        user_questions_correct = user_details[5]
        user_questions_answered = user_details[6]
        query = sql_update_user_results.format(
            full_name=quote(full_name),
            points=points + user_points,
            questions_correct=questions_correct + user_questions_correct,
            questions_answered=questions_answered+user_questions_answered,
        )
        self.connection.execute(query)
        self.connection.commit()
        print(f"Updated user score for user {full_name}")


def quote(s):
    if s is None:
        return s
    if not isinstance(s, str):
        s = str(s)
    return '\"' + s + '\"'
