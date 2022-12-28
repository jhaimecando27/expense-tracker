from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint('main', __name__)


@bp.route('/', methods=('POST', 'GET'))
@login_required
def index():
    db = get_db()

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        error = None

        if not name:
            error = 'Name is required.'
        elif not price:
            error = 'price is required.'

        if error is not None:
            flash(error)
        else:
            db.execute(
                'INSERT INTO expense (name, price, user_id)'
                ' VALUES (?, ?, ?)',
                (name, price, g.user['id'])
            )
            db.commit()
            return redirect(url_for('main.index'))

    expenses = db.execute(
        'SELECT e.id, name, price, user_id, username, bought'
        ' FROM expense e JOIN user u ON e.user_id = u.id'
        ' WHERE user_id=?'
        ' ORDER BY bought DESC',
        (g.user['id'],)
    ).fetchall()

    tmp = 0

    for expense in expenses:
        tmp = tmp + expense['price']

    return render_template('main/index.html', expenses=expenses, total=tmp)


def get_expense(id):
    expense = get_db().execute(
        'SELECT e.id, name, price, bought, user_id'
        ' FROM expense e JOIN user u ON e.user_id = u.id'
        ' WHERE e.id = ?',
        (id,)
    ).fetchone()

    if expense is None:
        abort(404, f"Post id {id} doesn't exist.")
    if expense['user_id'] != g.user['id']:
        abort(403)

    return expense


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    expense = get_expense(id)

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        error = None

        if not name:
            error = 'Title is required.'
        elif not price:
            error = 'Price is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE expense SET name = ?, price = ?'
                ' WHERE id = ?',
                (name, price, id)
            )
            db.commit()
            return redirect(url_for('main.index'))

    return render_template('main/update.html', expense=expense)


@bp.route('/<int:id>/delete', methods=('POST', 'GET'))
@login_required
def delete(id):
    get_expense(id)
    db = get_db()
    db.execute('DELETE FROM expense WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('main.index'))
