from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId  # Nếu cần thiết

from app.models import get_all_plants, add_plant, update_plant, delete_plant, get_plant_by_code  # Sửa đường dẫn import nếu cần

main = Blueprint('main', __name__)

@main.route('/')
def index():
    plants = get_all_plants()
    return render_template('index.html', plants=plants)

@main.route('/admin')
def admin():
    plants = get_all_plants()
    return render_template('admin.html', plants=plants)

@main.route('/admin/add', methods=['POST'])
def add():
    plant_data = {
        'name': request.form['name'],
        'variety': request.form['variety'],
        'plant_code': request.form['plant_code'],
        'price': float(request.form['price']),
        'planting_date': request.form['planting_date'],
        'location': request.form['location'],
        'health_status': request.form['health_status'],
        'notes': request.form['notes'],
        'image': request.form['image']
    }
    add_plant(plant_data)
    return redirect(url_for('main.admin'))

@main.route('/admin/update/<id>', methods=['POST'])
def update(id):
    plant_data = {
        'name': request.form['name'],
        'variety': request.form['variety'],
        'price': float(request.form['price']),
        'planting_date': request.form['planting_date'],
        'location': request.form['location'],
        'health_status': request.form['health_status'],
        'notes': request.form['notes'],
        'image': request.form['image']
    }
    try:
        update_plant(ObjectId(id), plant_data)
    except Exception as e:
        return str(e), 500
    return redirect(url_for('main.admin'))

@main.route('/admin/delete/<id>', methods=['POST'])
def delete(id):
    try:
        delete_plant(ObjectId(id))
    except Exception as e:
        return str(e), 500
    return redirect(url_for('main.admin'))

@main.route('/plant/<plant_code>')
def plant_detail(plant_code):
    plant = get_plant_by_code(plant_code)
    return render_template('plant_detail.html', plant=plant)

@main.route('/plants')
def show_plants():
    plant_code = request.args.get('plant_code', default='imported')
    plants = get_plants_by_code(plant_code)
    return render_template('index.html', plants=plants)
