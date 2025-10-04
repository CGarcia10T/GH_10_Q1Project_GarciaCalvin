from pyscript import document

def order_food(e):
    order_summary = document.getElementById("summary-content")
    order_summary.innerHTML = ""

    name = document.getElementById("name").value.strip()
    address = document.getElementById("address").value.strip()
    number = document.getElementById("phone").value.strip()

    if not name or not address or not number:
        order_summary.innerHTML = "Please fill in all fields before placing your order."
        return

    checkboxes = document.querySelectorAll("form input[type='checkbox']")
    subtotal = 0.0
    items = []

    for checkbox in checkboxes:
        if checkbox.checked:
            price = float(checkbox.getAttribute("data-price"))
            subtotal += price
            items.append(checkbox.nextElementSibling.innerText)  

    if not items:
        order_summary.innerHTML = "Please select at least one item."
        return

    items_list = "\n    ".join(items)
    summary_message = f"""Order for:  {name}
    Address:    {address}
    Number:     {number}

    Items Ordered:
    {items_list}

    Subtotal: {subtotal:.2f}
    """

    order_summary.innerText = summary_message