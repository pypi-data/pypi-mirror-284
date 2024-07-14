import requests


class Shopify:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_inventory_locations(self):
        try:
            response = requests.request(
                "GET",
                f"https://{self.url}.myshopify.com/admin/api/2023-10/locations.json",
                headers={"X-Shopify-Access-Token": self.token},
            )
            return response.json()["locations"]
        except requests.exceptions.RequestException as e:
            print(e)

    def get_inventory_levels(self, location_id):
        try:
            response = requests.request(
                "GET",
                f"https://{self.url}.myshopify.com/admin/api/2023-10/inventory_levels.json?limit=250&location_ids="
                + str(location_id),
                headers={"X-Shopify-Access-Token": self.token},
            )
            return response.json()["inventory_levels"]
        except requests.exceptions.RequestException as e:
            print(e)

    def get_products(self):
        try:
            response = requests.request(
                "GET",
                f"https://{self.url}.myshopify.com/admin/api/2024-04/products.json?limit=250",
                headers={"X-Shopify-Access-Token": self.token},
            )
            products = response.json()["products"]
            return products
        except requests.exceptions.RequestException as e:
            print(e)

    def is_lipo10(self, item_bar_code):
        if item_bar_code == "INJ-LIPO10ml":
            return True
        else:
            return False

    def is_lipo30(self, item_bar_code):
        if item_bar_code == "INJ-LIPO30ml":
            return True
        else:
            return False

    def get_inventory_item_barcode_and_name(self, item_id):
        try:
            inventory_item_response = requests.post(
                f"https://{self.url}.myshopify.com/admin/api/2023-10/graphql.json",
                headers={"X-Shopify-Access-Token": self.token},
                json={
                    "query": """{
                        inventoryItem(id: "gid://shopify/InventoryItem/"""
                    + str(item_id)
                    + """"){
                            variant{
                                barcode
                                product {
                                    title
                                    status
                                }
                            }
                        }
                    }""",
                },
            )
            inventory_item = inventory_item_response.json()
            status = inventory_item["data"]["inventoryItem"]["variant"]["product"][
                "status"
            ]
            if status != "ACTIVE":
                return None, None

            barcode = inventory_item["data"]["inventoryItem"]["variant"]["barcode"]
            title = inventory_item["data"]["inventoryItem"]["variant"]["product"][
                "title"
            ]

            return barcode, title
        except requests.exceptions.RequestException as e:
            print(e)

    def set_inventory_item_level(self, item_id, location_id, quantity):
        if quantity < 0:
            quantity = 0
        try:
            query = """
                    mutation inventorySetOnHandQuantities($input: InventorySetOnHandQuantitiesInput!) {
                    inventorySetOnHandQuantities(input: $input) {
                        userErrors {
                            field
                            message
                        }
                        inventoryAdjustmentGroup {
                            createdAt
                            reason
                            referenceDocumentUri
                            changes {
                                name
                                delta
                            }
                        }
                    }
                    }
            """
            input = {
                "reason": "correction",
                "referenceDocumentUri": "uri://options.zenoti.com",
                "setQuantities": [
                    {
                        "inventoryItemId": f"gid://shopify/InventoryItem/{item_id}",
                        "locationId": f"gid://shopify/Location/{location_id}",
                        "quantity": round(quantity),
                    }
                ],
            }
            variables = {"input": input}
            response = requests.post(
                f"https://{self.url}.myshopify.com/admin/api/2023-10/graphql.json",
                headers={"X-Shopify-Access-Token": self.token},
                json={"query": query, "variables": variables},
            )
            output = response.json()
            if len(output["data"]["inventorySetOnHandQuantities"]["userErrors"]) > 0:
                raise Exception(
                    output["data"]["inventorySetOnHandQuantities"]["userErrors"]
                )
            return output

        except requests.exceptions.RequestException as e:
            print(e)

    def set_product_name(self, product_id, newName):
        try:
            response = requests.request(
                "PUT",
                f"https://{self.url}.myshopify.com/admin/api/2024-04/products/{product_id}.json",
                headers={"X-Shopify-Access-Token": self.token},
                json={"product": {"id": product_id, "title": newName}},
            )
            # print(response.json())

        except requests.exceptions.RequestException as e:
            print(e)

    def make_product_inactive(self, product_id):
        try:
            response = requests.request(
                "POST",
                f"https://{self.url}.myshopify.com/admin/api/2024-04/products/{product_id}/.json",
                headers={"X-Shopify-Access-Token": self.token},
                json={"product": {"id": product_id, "status": "archived"}},
            )
            print(response.json())
        except requests.exceptions.RequestException as e:
            print(e)
