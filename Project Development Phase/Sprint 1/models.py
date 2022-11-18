from faker import Faker
from flask import Flask
from flask_login import login_manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import *

from flask_login import *

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'ibm_db_sa://qrw67838:KudtVYUDstabqSV6@2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:32328/BLUDB;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;sslConnection=true;'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_company = db.Column(db.Boolean, default=False, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __unicode__(self):
        return self.email


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class JobSeeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    programming_language = db.Column(db.String(20), nullable=False)
    tools = db.Column(db.String(20), nullable=False)
    degree = db.Column(db.String(20), nullable=False)
    dept = db.Column(db.String(40), nullable=False)
    current_status = db.Column(db.String(20), nullable=False)
    cgpa = db.Column(db.Integer, nullable=False)
    x_percent = db.Column(db.Integer, nullable=False)
    xii_percent = db.Column(db.Integer, nullable=False)


class CompanyProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    com_name = db.Column(db.String(40), nullable=False)
    com_address = db.Column(db.String(120), nullable=False)


class JobOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.Integer, db.ForeignKey('company_profile.id'), nullable=False)
    job_title = db.Column(db.String(40), nullable=False)
    total_applications = db.Column(db.Integer, nullable=False)
    skill_required = db.Column(db.String(40), nullable=False)


class JobRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_offer = db.Column(db.Integer, db.ForeignKey('job_offer.id'), nullable=False)
    job_seeker = db.Column(db.Integer, db.ForeignKey('job_seeker.id'), nullable=False)


with app.app_context():
    db.create_all()


def create_fake_users(n):
    with app.app_context():
        faker = Faker()
        for i in range(n):
            user = User(email=faker.email(), password=faker.password(), is_company=faker.boolean())
            db.session.add(user)
        db.session.commit()
        print(f'Added {n} fake users to the database.')


def create_job_seeker(n):
    with app.app_context():
        faker = Faker()
        for i in range(n):
            js = JobSeeker(
                user=2,
                firstname=faker.name(),
                lastname=faker.name(),
                phone=9900990099,
                address=faker.address(),
                programming_language='Python',
                tools='Git',
                degree='B.E',
                dept='CSE',
                current_status='Completed',
                cgpa=5,
                x_percent=80,
                xii_percent=90
            )
            db.session.add(js)
        db.session.commit()
        print(f'Added {n} fake job seeker to the database.')
