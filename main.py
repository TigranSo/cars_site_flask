from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__, template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cars.db"
db = SQLAlchemy(app)



class Car(db.Model):
	"""Класс для бд и их опред."""
	id = db.Column(db.Integer, primary_key=True)
	name_car = db.Column(db.String(100))
	color = db.Column(db.String(50))
	date_v = db.Column(db.Integer)
	price = db.Column(db.Integer)
	contry = db.Column(db.String(50))
	image = db.Column(db.LargeBinary)

	# def __repr__(self):
	# 	return '<Car %r>' % self.id

class Оrder(db.Model):
	"""Класс для бд и их опред."""
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(100))
	telephone = db.Column(db.String(50))
	model_car = db.Column(db.String(50))
	date_v = db.Column(db.Integer) #Дата выпуска
	new_old = db.Column(db.String(50)) #Новый или старый


with app.app_context():
	"""Создаем таблицы в базе данных"""
	db.create_all()


@app.route('/')
def index():
	"""Главная страница"""
	return render_template("index.html")


@app.route('/cars')
def cars():
	"""Страница авто."""
	catalog = db.session.query(Car).all()
	return render_template("cars.html", catalog=catalog)


@app.route('/about', methods=['GET', 'POST'])
def about():
	"""Страница формы"""
	if request.method == 'POST':
		first_name = request.form['first_name']
		telephone = request.form['telephone']
		model_car = request.form['model_car']
		date_v = request.form['date_v']
		new_old = request.form['new_old']

        # Сохранение в базу данных
		order = Оrder(first_name=first_name, telephone=telephone, model_car=model_car, date_v=date_v, new_old=new_old)
		db.session.add(order)
		db.session.commit()
		success = ""
		return render_template("result.html", success=success)

	return render_template("about.html")


if __name__ == "__main__":
	app.run(debug = True)