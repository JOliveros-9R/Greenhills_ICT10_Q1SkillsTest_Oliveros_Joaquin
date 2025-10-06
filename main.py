from pyscript import display, document

prices = {
    "Double Cheese Burger": 200,
    "Chicken Wings": 250,
    "Iced lemon Tea": 90,
    "Iced Tea": 80
}

def create_order(event):
    selected_items = []
    total = 0

    for item in prices:
        if document.getElementById(item).checked:
            selected_items.append(item)
            total += prices[item]

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    summary = f"""
    Order for: {name}<br>
    Address: {address}<br>
    Contact number: {contact}<br>
    Selected items: {', '.join(selected_items)}<br>
    Total: ₱ {total:.2f}
    """
    display(summary, target="output")
