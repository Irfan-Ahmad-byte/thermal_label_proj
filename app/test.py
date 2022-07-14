payload = {
  "requestedShipment": {
    "shipDatestamp": "2022-10-14",
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
        "residential": False
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
        "residential": False
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
        "value": "6207341699377"
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
          "residential": False
        },
        "contact": {
          "personName": "John Taylor",
          "emailAddress": "sample@company.com",
          "phoneExtension": "000",
          "phoneNumber": "1661345671",
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
    "recipientLocationNumber": "1234567",
    "pickupType": "USE_SCHEDULED_PICKUP",
    "serviceType": "PRIORITY_OVERNIGHT",
    "packagingType": "YOUR_PACKAGING",
    "totalWeight": 20.6,
    "origin": {
      "address": {
        "streetLines": [
          "10 FedEx Parkway",
          "Suite 302"
        ],
        "city": "Beverly Hills",
        "stateOrProvinceCode": "CA",
        "postalCode": "38127",
        "countryCode": "US",
        "residential": False
      },
      "contact": {
        "personName": "person name",
        "emailAddress": "email address",
        "phoneNumber": "phone number",
        "phoneExtension": "phone extension",
        "companyName": "company name",
        "faxNumber": "fax number"
      }
    },
    "shippingChargesPayment": {
      "paymentType": "SENDER",
      "payor": {
        "responsibleParty": {
          "address": {
            "streetLines": [
              "10 FedEx Parkway",
              "Suite 302"
            ],
            "city": "Beverly Hills",
            "stateOrProvinceCode": "CA",
            "postalCode": "90210",
            "countryCode": "US",
            "residential": False
          },
          "contact": {
            "personName": "John Taylor",
            "emailAddress": "sample@company.com",
            "phoneNumber": "1661567890",
            "phoneExtension": "phone extension",
            "companyName": "Fedex",
            "faxNumber": "fax number"
          },
          "accountNumber": {
            "value": "6206271528204"
          }
        }
      }
    },
    "shipmentSpecialServices": {
      "specialServiceTypes": [
        "THIRD_PARTY_CONSIGNEE",
        "PROTECTION_FROM_FREEZING"
      ],
      "etdDetail": {
        "attributes": [
          "POST_SHIPMENT_UPLOAD_REQUESTED"
        ],
        "attachedDocuments": [
          {
            "documentType": "PRO_FORMA_INVOICE",
            "documentReference": "DocumentReference",
            "description": "PRO FORMA INVOICE",
            "documentId": "090927d680038c61"
          }
        ],
        "requestedDocumentTypes": [
          "VICS_BILL_OF_LADING",
          "GENERAL_AGENCY_AGREEMENT"
        ]
      },
      "returnShipmentDetail": {
        "returnEmailDetail": {
          "merchantPhoneNumber": "19012635656",
          "allowedSpecialService": [
            "SATURDAY_DELIVERY"
          ]
        },
        "rma": {
          "reason": "Wrong Size or Color"
        },
        "returnAssociationDetail": {
          "shipDatestamp": "2022-10-01",
          "trackingNumber": "123456789"
        },
        "returnType": "PRINT_RETURN_LABEL"
      },
      "deliveryOnInvoiceAcceptanceDetail": {
        "recipient": {
          "address": {
            "streetLines": [
              "23, RUE JOSEPH-DE MA",
              "Suite 302"
            ],
            "city": "Beverly Hills",
            "stateOrProvinceCode": "CA",
            "postalCode": "90210",
            "countryCode": "US",
            "residential": False
          },
          "contact": {
            "personName": "John Taylor",
            "emailAddress": "sample@company.com",
            "phoneExtension": "000",
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
          "deliveryInstructions": "Delivery Instructions"
        }
      },
      "internationalTrafficInArmsRegulationsDetail": {
        "licenseOrExemptionNumber": "9871234"
      },
      "pendingShipmentDetail": {
        "pendingShipmentType": "EMAIL",
        "processingOptions": {
          "options": [
            "ALLOW_MODIFICATIONS"
          ]
        },
        "recommendedDocumentSpecification": {
          "types": "ANTIQUE_STATEMENT_EUROPEAN_UNION"
        },
        "emailLabelDetail": {
          "recipients": [
            {
              "emailAddress": "neena@fedex.com",
              "optionsRequested": {
                "options": [
                  "PRODUCE_PAPERLESS_SHIPPING_FORMAT",
                  "SUPPRESS_ACCESS_EMAILS"
                ]
              },
              "role": "SHIPMENT_COMPLETOR",
              "locale": "en_US"
            }
          ],
          "message": "your optional message"
        },
        "attachedDocuments": [
          {
            "documentType": "PRO_FORMA_INVOICE",
            "documentReference": "DocumentReference",
            "description": "PRO FORMA INVOICE",
            "documentId": "090927d680038c61"
          }
        ],
        "expirationTimeStamp": "2023-01-01"
      },
      "holdAtLocationDetail": {
        "locationId": "YBZA",
        "locationContactAndAddress": {
          "address": {
            "streetLines": [
              "10 FedEx Parkway",
              "Suite 302"
            ],
            "city": "Beverly Hills",
            "stateOrProvinceCode": "CA",
            "postalCode": "38127",
            "countryCode": "US",
            "residential": False
          },
          "contact": {
            "personName": "John Taylor",
            "emailAddress": "sample@company.com",
            "phoneNumber": "1234567890",
            "phoneExtension": "000",
            "companyName": "Fedex",
          }
        },
        "locationType": "FEDEX_ONSITE"
      },
    "pickupDetail": {
      "readyPickupDateTime": "2020-07-03T09:00:00Z",
      "latestPickupDateTime": "2020-07-03T09:00:00Z"
    }
  },
  "accountNumber": {
    "value": "Your account number"
  }
}
}


import requests

url = "https://apis-sandbox.fedex.com/ship/v1/shipments/tag"

payload = input # 'input' refers to JSON Payload
headers = {
    'Content-Type': "application/json",
    'X-locale': "en_US",
    'Authorization': "Bearer l7b66fa3d083c246e68a374612bcad2988"
    }

response = requests.request("POST", url, data=payload(), headers=headers)

print(response.text)