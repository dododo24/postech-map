from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Facility_Info
from app.models import Facility

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/po-map', methods=['GET', 'POST'])
def map():
    restaurant = Facility.query.filter_by(category='restaurant').all()
    Cafe = Facility.query.filter_by(category='Cafe').all()
    GS25 = Facility.query.filter_by(category='GS25').all()
    GSR = Facility.query.filter_by(category='GSR').all()
    Sports = Facility.query.filter_by(category='Sports').all()
    Others = Facility.query.filter_by(category='Others').all()
    return render_template('po-map.html', title='Sign In', restaurant=restaurant)
@app.route('/db', methods=['GET', 'POST'])
def add_db():
    form = Facility_Info()
    if form.validate_on_submit():
        category = form.category.data
        name = form.name.data
        time = form.time.data
        home_url = form.home_url.data
        menu_url = form.menu_url.data
        reserv_url = form.reserv_url.data
        phone_num = form.phone_num.data
        new_info = Facility(category=category, name=name, time=time, home_url=home_url, menu_url=menu_url, reserv_url=reserv_url, phone_num=phone_num)
        db.session.add(new_info)
        db.session.commit()
        return redirect(url_for('add_db'))
    return render_template('add_db.html', title='Add DB', form=form)
