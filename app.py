
from flask import Flask, render_template, request

app = Flask(__name__)


def get_discount(subtotal):
    if subtotal >= 5000:
        return 15
    elif subtotal >= 2000:
        return 10
    elif subtotal >= 1000:
        return 5
    return 0


@app.route("/", methods=["GET", "POST"])
def home():
    bill = None
    error = None

    if request.method == "POST":
        try:
            names = request.form.getlist("name")
            prices = request.form.getlist("price")
            quantities = request.form.getlist("quantity")

            items = []
            subtotal = 0.0

            for name, price, quantity in zip(
                names, prices, quantities
            ):
                name = name.strip()
                price = float(price)
                quantity = int(quantity)

                if not name or price <= 0 or quantity <= 0:
                    raise ValueError

                amount = price * quantity
                subtotal += amount

                items.append({
                    "name": name,
                    "price": price,
                    "quantity": quantity,
                    "amount": amount
                })

            if not items:
                raise ValueError

            rate = get_discount(subtotal)
            discount = subtotal * rate / 100
            taxable = subtotal - discount

            gst_rate = 5
            gst = taxable * gst_rate / 100
            total = taxable + gst

            bill = {
                "items": items,
                "subtotal": subtotal,
                "rate": rate,
                "discount": discount,
                "taxable": taxable,
                "gst": gst,
                "total": total
            }

        except (ValueError, TypeError):
            error = "Invalid details. Please check your inputs."

    return render_template(
        "index.html", bill=bill, error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
