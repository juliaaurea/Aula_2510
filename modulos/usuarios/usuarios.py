from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pizza

bp_usuario = Blueprint('usuarios', __name__, template_folder="templates")

@bp_usuario.route('/')
def index():
    dados = Pizza.query.all()
    return render_template('pizza.html', dados=dados)

@bp_usuario.route('/add')
def add():
    return render_template('pizza_add.html')

@bp_usuario.route('/save', methods=['POST'])
def save():
    sabor = request.form.get('sabor')
    ingredientes = request.form.get('ingredientes')
    preco = request.form.get('preco')
    if sabor and ingredientes and preco:
        objeto = Pizza(sabor, ingredientes, preco)
        db.session.add(objeto)
        db.session.commit()
        flash('Pedido anotado com sucesso!')
        return redirect('/pizzas')
    else:
        flash('Preencha todos os campos!')
        return redirect('/pizzas/add')
    
