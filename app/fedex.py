import requests

payload = {
  "requestedShipment": {
    "shipDatestamp": "2012-08-14",
    "totalDeclaredValue": {
      "amount": 1556.25,
      "currency": "USD"
    },
    "shipper": {
      "address": {
        "streetLines": [
          "10 FedEx Parkway",
          "Suite 302"
        ],
        "city": "Beverly Hills",
        "stateOrProvinceCode": "CA",
        "postalCode": "90210",
        "countryCode": "US",
        "residential": 'false'
      },
      "contact": {
        "personName": "John Taylor",
        "emailAddress": "sample@company.com",
        "phoneExtension": "91",
        "phoneNumber": "XXXX567890",
        "companyName": "Fedex"
      },
      "tins": [
        {
          "number": "XXX567",
          "tinType": "FEDERAL",
          "usage": "usage",
          "effectiveDate": "2000-01-23T04:56:07.000+00:00",
          "expirationDate": "2000-01-23T04:56:07.000+00:00"
        }
      ]
    },
    "soldTo": {
      "address": {
        "streetLines": [
          "10 FedEx Parkway",
          "Suite 302"
        ],
        "city": "Beverly Hills",
        "stateOrProvinceCode": "CA",
        "postalCode": "90210",
        "countryCode": "US",
        "residential": 'false'
      },
      "contact": {
        "personName": "John Taylor",
        "emailAddress": "sample@company.com",
        "phoneExtension": "91",
        "phoneNumber": "1234567890",
        "companyName": "Fedex"
      },
      "tins": [
        {
          "number": "123567",
          "tinType": "FEDERAL",
          "usage": "usage",
          "effectiveDate": "2000-01-23T04:56:07.000+00:00",
          "expirationDate": "2000-01-23T04:56:07.000+00:00"
        }
      ],
      "accountNumber": {
        "value": "Your account number"
      }
    },
    "recipients": [
      {
        "address": {
          "streetLines": [
            "10 FedEx Parkway",
            "Suite 302"
          ],
          "city": "Beverly Hills",
          "stateOrProvinceCode": "CA",
          "postalCode": "90210",
          "countryCode": "US",
          "residential": 'false'
        },
        "contact": {
          "personName": "John Taylor",
          "emailAddress": "sample@company.com",
          "phoneExtension": "000",
          "phoneNumber": "XXXX345671",
          "companyName": "FedEx"
        },
        "tins": [
          {
            "number": "123567",
            "tinType": "FEDERAL",
            "usage": "usage",
            "effectiveDate": "2000-01-23T04:56:07.000+00:00",
            "expirationDate": "2000-01-23T04:56:07.000+00:00"
          }
        ],
        "deliveryInstructions": "Delivery Instructions"
      }
    ],
        }
      }

import requests

url = "https://apis-sandbox.fedex.com/ship/v1/shipments/tag"

# payload = input # 'input' refers to JSON Payload
headers = {
    'Content-Type': "application/json",
    'X-locale': "en_US",
    'Authorization': "Bearer l7b66fa3d083c246e68a374612bcad2988"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)