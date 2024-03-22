from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


db_session.global_init("db/mars_explorer.db")
db_sess = db_session.create_session()

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.adress = "module_1"
user.email = "scott_chief@mars.org"
db_sess.add(user)
db_sess.commit()


user = User()
user.surname = "Harris"
user.name = "Leo"
user.age = 25
user.position = "worker"
user.speciality = "engineer"
user.adress = "module_2"
user.email = "leo_harris@mars.org"
db_sess.add(user)
db_sess.commit()


user = User()
user.surname = "Carter"
user.name = "Anthony"
user.age = 28
user.position = "worker"
user.speciality = "developer"
user.adress = "module_1"
user.email = "antony_carter@mars.org"
db_sess.add(user)
db_sess.commit()


user = User()
user.surname = "Cobb"
user.name = "Steven"
user.age = 30
user.position = "worker"
user.speciality = "cook"
user.adress = "module_3"
user.email = "steven_cobb@mars.org"
db_sess.add(user)
db_sess.commit()


db_sess.add(user)
db_sess.commit()


def main():
    app.run()


if __name__ == '__main__':
    main()