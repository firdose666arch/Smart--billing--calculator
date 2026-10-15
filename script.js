
const addButton = document.getElementById("addProduct");
const products = document.getElementById("products");

addButton.addEventListener("click", function () {
    const product = document.createElement("div");
    product.className = "product";

    product.innerHTML = `
        <input name="name" placeholder="Product name" required>
        <input name="price" type="number" min="0.01"
               step="0.01" placeholder="Price (₹)" required>
        <input name="quantity" type="number" min="1"
               step="1" placeholder="Quantity" required>
        <button type="button" class="removeProduct">
            Remove
        </button>
    `;

    products.appendChild(product);

    product.querySelector(".removeProduct")
        .addEventListener("click", function () {
            product.remove();
        });
});

