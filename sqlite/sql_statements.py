sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                    user_id integer PRIMARY KEY,
                                    full_name text NOT NULL,
                                    username text NOT NULL,
                                    discriminator text NOT NULL,
                                    points integer DEFAULT 0 NOT NULL,
                                    questions_correct integer DEFAULT 0 NOT NULL,
                                    questions_answered integer DEFAULT 0 NOT NULL,
                                    begin_date text,
                                    end_date text
                                ); """

sql_create_trivia_game_table = """CREATE TABLE IF NOT EXISTS trivia_game (
                                game_id integer PRIMARY KEY,
                                category text,
                                num_of_questions integer NOT NULL,
                                seconds_per_question integer NOT NULL,
                                is_complete integer DEFAULT 0 NOT NULL,
                                begin_date text,
                                end_date text
                            );"""
                            
                            
sql_create_questions_table = """CREATE TABLE IF NOT EXISTS questions (
                                 question_id integer PRIMARY KEY,
                                 category string NOT NULL,
                                 title text NOT NULL,
                                 answer1 text NOT NULL,
                                 answer2 text NOT NULL,
                                 answer3 text NOT NULL,
                                 answer4 text NOT NULL,
                                 correct_answer integer NOT NULL,
                                 created_by text
                             );"""

sql_get_question_by_title = """SELECT * from questions where title={title} and category={category};"""


sql_insert_question = """INSERT INTO questions (category, title, answer1, answer2, answer3, answer4, correct_answer, created_by)
                                VALUES ({category}, {title}, {answer1}, {answer2}
                                , {answer3}, {answer4}, {correct_answer}, {created_by});"""


# """CREATE TABLE IF NOT EXISTS question (
#                                 question_id integer PRIMARY KEY,
#                                 trivia_game_key integer NOT NULL,
#                                 question_title text NOT NULL,
#                                 num_of_answers integer NOT NULL,
#                                 is_complete integer DEFAULT 0 NOT NULL,
#                                 begin_date text,
#                                 end_date text,
#                                 FOREIGN KEY (trivia_game_key) REFERENCES trivia_game (game_id)
#                             );"""
                            
                            
# sql_create_questions_answers_table = """CREATE TABLE IF NOT EXISTS question_answers (
#                                 answer_id integer PRIMARY KEY,
#                                 question_key integer NOT NULL,
#                                 question_text text NOT NULL,
#                                 users_who_answered string,
#                                 is_complete integer DEFAULT 0 NOT NULL,
#                                 begin_date text,
#                                 end_date text,
#                                 FOREIGN KEY (question_key) REFERENCES question (question_id)
#                             );"""


sql_insert_trivia_game = """INSERT INTO trivia_game (
                                (category, num_of_questions, seconds_per_question, is_complete, begin_date, end_date)
                                VALUES ({category}, {num_of_questions}, {seconds_per_question}, {is_complete}
                                , {begin_date}, {end_date})
                            ;"""


sql_insert_user = """INSERT INTO users (full_name, username, discriminator, points, questions_correct, questions_answered, begin_date, end_date)
                                VALUES ({full_name}, {username}, {discriminator}, {points}, {questions_correct}, {questions_answered}, {begin_date}, {end_date})
                            ;"""


sql_get_user_by_full_name = """SELECT * from users where full_name={full_name}
                            ;"""


sql_update_user_results = """UPDATE users SET points={points}, questions_correct={questions_correct}, questions_answered={questions_answered} WHERE full_name={full_name};"""
