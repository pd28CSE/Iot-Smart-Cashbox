# Iot-Smart-Cashbox
 
All Product of Store

Get Request URL

    https://filesharingbd.pythonanywhere.com/cash-box-api/

Data Format:

    [
        {
            "id": "e8d4774c-8b97-4ed8-8f93-b52e52a1d0a8",
            "quantity": 100,
            "name": "Potato chip",
            "brand": "Pran",
            "sellingcost": 10.0,
            "buyingcost": 8.0,
            "currentquantity": 99
        },
        {
            "id": "825c36bc-45c1-41a5-8bc4-faffeef721c9",
            "quantity": 100,
            "name": "LAYS CHIPS SPANISH TOMATO TANGO 25 GM",
            "brand": "Pran",
            "sellingcost": 100.0,
            "buyingcost": 40.0,
            "currentquantity": 88
        }
    ]

All Customers Orders Information

Get Request URL

    https://filesharingbd.pythonanywhere.com/cash-box-api/customers/

Data Format:

    [
        {
            "id": 19,
            "customer": {
                "id": 28,
                "name": "user"
            },
            "orderproduct": [
                {
                    "id": 19,
                    "productcode": {
                        "id": "e8d4774c-8b97-4ed8-8f93-b52e52a1d0a8",
                        "quantity": 100,
                        "name": "Potato chip",
                        "brand": "Pran",
                        "sellingcost": 10.0,
                        "buyingcost": 8.0,
                        "currentquantity": 99
                    },
                    "quantity": 1,
                    "price": 10.0
                },
                {
                    "id": 20,
                    "productcode": {
                        "id": "825c36bc-45c1-41a5-8bc4-faffeef721c9",
                        "quantity": 100,
                        "name": "LAYS CHIPS SPANISH TOMATO TANGO 25 GM",
                        "brand": "Pran",
                        "sellingcost": 100.0,
                        "buyingcost": 40.0,
                        "currentquantity": 88
                    },
                    "quantity": 3,
                    "price": 300.0
                }
            ],
            "orderdatetime": "2023-02-24T10:25:08.517386Z",
            "totalprice": 310.0
        }
    ]

Customers Order

Post Request URL

    https://filesharingbd.pythonanywhere.com/cash-box-api/customers/


Post Request Type For Single Product Order

    [
        {
        "productcode": "____________",
        "quantity": 10
        }
    ]


Post Request Type For Multiple Product Order

    [
        {
        "productcode": "____________",
        "quantity": 10
        },
        {
        "productcode": "____________",
        "quantity": 5
        }
    ]




