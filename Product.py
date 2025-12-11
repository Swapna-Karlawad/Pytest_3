def product_details(name, prd_id, quantity, price):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {prd_id}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}\n"
    )
    return result

if __name__ == "__main__":
    name = "Phone"
    prd_id = "1001"
    quantity = "1"
    price = "10000"
    
    print(product_details(name, prd_id, quantity, price))
