import ibm_db
from flask import *
import secrets
from flask_login import *

from forms import *
from models import *

app.secret_key = secrets.token_hex()


@app.route('/home')
def home():
    job_request_form = JobRequestForm()
    job_offers = JobOffer.query.all()
    return render_template('index.html', job_offers=job_offers, form=job_request_form)


@app.route('/companyindex')
def companyindex():
    form = JobOfferForm()
    companyprofile = CompanyProfile.query.filter_by(user=current_user.id).first()
    joboffers = JobOffer.query.filter_by(company=companyprofile.id).all()
    return render_template('company_index.html', form=form, companyprofile=companyprofile, joboffers=joboffers)


@app.route('/')
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, is_company=form.is_company.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            if user.is_company:
                return redirect(url_for('companyindex'))
            else:
                return redirect(next or url_for('home'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form=form)


@app.route('/jobseekerprofile', methods=['GET', 'POST'])
def jobseekerprofile():
    form = JobSeekerForm()
    if form.validate_on_submit():
        js = JobSeeker.query.filter_by(user=form.user_id.data).first()
        if js is None:
            jobseeker = JobSeeker(
                user=form.user_id.data,
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                phone=form.phone.data,
                address=form.address.data,
                programming_language=form.programming_languages.data,
                tools=form.tools.data,
                degree=form.degree.data,
                dept=form.dept.data,
                current_status=form.current_status.data,
                cgpa=form.cgpa.data,
                x_percent=form.x_percent.data,
                xii_percent=form.xii_percent.data
            )

            db.session.add(jobseeker)
            db.session.commit()
            return redirect(url_for('jobseekerprofile'))
    return render_template('jobseekerprofile.html', form=form)


@app.route('/companyprofile', methods=['GET', 'POST'])
def companyprofile():
    form = CompanyForm()
    if form.validate_on_submit():
        company_exist = CompanyProfile.query.filter_by(user=form.user_id.data).first()
        if company_exist is None:
            company = CompanyProfile(
                user=form.user_id.data,
                com_name=form.com_name.data,
                com_address=form.com_address.data,
            )
            db.session.add(company)
            db.session.commit()
            return redirect(url_for('companyprofile'))
    return render_template('company_profile.html', form=form)


@app.route('/create_job', methods=['POST'])
def create_job():
    form = JobOfferForm()
    joboffer = JobOffer(
        company=form.company_id.data,
        job_title=form.job_title.data,
        total_applications=form.total_applications.data,
        skill_required=form.skill_required.data
    )
    db.session.add(joboffer)
    db.session.commit()
    companyprofile = CompanyProfile.query.filter_by(user=current_user.id).first()
    joboffersresult = JobOffer.query.filter_by(company=companyprofile.id).all()
    return render_template("compnay_joboffer_table.html", companyprofile=companyprofile, joboffers=joboffersresult)


@app.route('/request_job', methods=['POST'])
def request_job():
    form = JobRequestForm()
    req_exists = JobRequest.query.filter_by(company=form.job_offer.data, jobseeker=form.job_seeker.data).first()
    if req_exists is None:
        job_request = JobRequest(
            company=form.job_offer.data,
            jobseeker=form.job_seeker.data
        )
        db.session.add(job_request)
        db.session.commit()
        job_offers = JobOffer.query.all()
        return render_template('compnay_joboffer_table.html', job_offers=job_offers, job_id=form.job_offer.data)
    return render_template('index.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


def get_company(id):
    return CompanyProfile.query.filter_by(id=id).first()


def job_seeker(id):
    return JobSeeker.query.filter_by(user=id).first()


def req_exist(com_id, seeker_id):
    return JobRequest.query.filter_by(company=com_id, jobseeker=seeker_id).first()


app.jinja_env.globals.update(
    get_company=get_company,
    job_seeker=job_seeker,
    req_exist=req_exist
)

if __name__ == '__main__':
    app.run()
