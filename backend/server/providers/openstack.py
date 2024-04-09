import requests
from os import environ as env

class OpenStackProvider:
    def __init__(self) -> None:
        json_data = {
            "auth": {
                "identity": {
                    "methods": ["password"],
                    "password": {
                        "user": {
                            "domain": {"name": f"{env['OS_USER_DOMAIN_NAME']}"},
                            "name": f"{env['OS_USERNAME']}",
                            "password": f"{env['OS_PASSWORD']}",
                        }
                    },
                },
                "scope": {
                    "project": {
                        "domain": {"name": f"{env['OS_USER_DOMAIN_NAME']}"},
                        "name": f"{env['OS_PROJECT_NAME']}",
                    }
                },
            }
        }

        resp = requests.post(f'{env["OS_AUTH_URL"]}/v3/auth/tokens', json=json_data)

        self.token = resp.headers["X-Subject-Token"]
        compute_endpoints = next(
            filter(lambda x: x["type"] == "compute", resp.json()["token"]["catalog"])
        )["endpoints"]
        self.compute_url = next(
            filter(lambda x: x["interface"] == "public", compute_endpoints)
        )["url"]
        image_endpoints = next(
            filter(lambda x: x["type"] == "image", resp.json()["token"]["catalog"])
        )["endpoints"]
        self.image_url = next(
            filter(lambda x: x["interface"] == "public", image_endpoints)
        )["url"]

    def open_console(self, vm_id: str) -> dict:
        resp = requests.post(
            f"{self.compute_url}/servers/{vm_id}/action",
            headers={"X-Auth-Token": self.token},
            json={"os-getVNCConsole": {"type": "novnc"}},
        )
        return resp.json()["console"]["url"]

    def create_vm(self, name: str, image: str, flavor: str) -> dict:
        resp = requests.post(
            f"{self.compute_url}/servers",
            headers={"X-Auth-Token": self.token},
            json={"server": {"name": name, "imageRef": image, "flavorRef": flavor}},
        )
        return resp.json()

    def delete_vm(self, vm_id: str) -> None:
        requests.delete(
            f"{self.compute_url}/servers/{vm_id}", headers={"X-Auth-Token": self.token}
        )

    def get_images(self) -> dict:
        images = []
        resp = requests.get(
            f"{self.image_url}/v2/images", headers={"X-Auth-Token": self.token}
        )
        while True:
            images += [{"name": x['name'], "id": x['id']} for x in resp.json()['images']]
            if 'next' not in resp.json():
                break
            resp = requests.get(
                f"{self.image_url}{resp.json()['next']}", headers={"X-Auth-Token": self.token}
            )
        return images

    def get_flavors(self) -> dict:
        flavors = []
        resp = requests.get(
            f"{self.compute_url}/flavors", headers={"X-Auth-Token": self.token}
        )
        while True:
            flavors += [{"name": x['name'], "id": x['id']} for x in resp.json()['flavors']]
            if 'next' not in resp.json():
                break
            resp = requests.get(
                f"{self.image_url}{resp.json()['next']}", headers={"X-Auth-Token": self.token}
            )
        return flavors
