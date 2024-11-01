from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pedido

bp_pedidos = Blueprint('pedidos', __name__, template_folder="templates")

@bp_pedidos.route('/')
def index():
    dados = Pedido.query.all()
    return render_template('pedido.html', dados=dados)

@bp_pedidos.route('/add')
def add():
    return render_template('pedido_add.html')

@bp_pedidos.route('/save', methods=['POST'])
def save():
    usuario_id = request.form.get('usuario')
    pizza_id = request.form.get('pizza')
    data = request.form.get('data')
    if usuario_id and pizza_id and data:
        objeto = Pedido(usuario_id, pizza_id, data)
        db.session.add(objeto)
        db.session.commit()
        flash('Pedido anotado com sucesso!')
        return redirect('/pedidos')
    else:
        flash('Preencha todos os campos!')
        return redirect('/pedidos/add')