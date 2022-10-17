from app import app, Products, session, render_template


@app.route('/user/order-details', methods = ["GET", "POST"])
def order_details():
    grand_total = 0
    index = 0
    total_quantity = 0

    for item in session['cart']:
        product = Products.query.filter_by(id=item['id'])

        quantity = int(item['quantity'])
        total = quantity * product.Price

        grand_total +=total
        total_quantity += quantity

        Products.append({'ID' : Products.ID, 'Product_Name': Products.Product_Name, 'Description': Products.Description, 'Price': Products.Price})
        index +=1
    
    grand_total_shipping_charges = grand_total + 250
    return Products, grand_total, grand_total_shipping_charges, total_quantity

@app.route('/cart')
def cart():
    Products, grand_total, grand_total_shipping_charges, total_quantity = order_details()

    return render_template('cart.html', products=Products, grand_total=grand_total, grand_total_plus_shipping=grand_total_shipping_charges, total_quantity=total_quantity)

if __name__ == "__main__":
    app.run(debug=True)