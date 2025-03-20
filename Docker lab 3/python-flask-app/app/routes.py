from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db
from app.models import Product

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные из формы
        name = request.form.get("name")
        quantity_sold = request.form.get("quantity_sold")
        total_revenue = request.form.get("total_revenue")
        category = request.form.get("category")  # Получаем категорию товара

        # Проверка на обязательные поля
        if not name or not quantity_sold or not total_revenue or not category:
            return "Missing fields", 400  # Можно добавить более подробную обработку ошибок

        # Создаем новый продукт и добавляем его в базу данных
        product = Product(name=name, quantity_sold=quantity_sold, total_revenue=total_revenue, category=category)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for("main.index"))

    # Если это GET-запрос, то выводим список продуктов
    products = Product.query.all()
    return render_template("index.html", products=products)