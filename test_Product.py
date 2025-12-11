from Product import product_details

def test_product_details():
    expected_output = (
        "Product Name: Phone\n"
        "Product ID: 1001\n"
        "Quantity:1\n"
        "Price: 10000\n"
    )
    assert product_details("Phone", "1001", "1", 10000) == expected_output
