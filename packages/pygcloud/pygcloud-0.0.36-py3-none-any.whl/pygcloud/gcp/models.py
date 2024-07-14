"""
Data models related to GCP services

@author: jldupont
"""
from typing import List, Dict
from dataclasses import dataclass
from pygcloud.utils import JsonObject


class _base:

    @classmethod
    def parse_json(cls, json_str: str) -> dict:
        import json
        try:
            json_obj = json.loads(json_str)
        except Exception:
            raise ValueError(f"Cannot parse for JSON: {json_str}")

        return json_obj

    @classmethod
    def from_json_string(cls, json_str: str):
        """
        Create a dataclass from a JSON string
        Make sure to only include fields declare
        in the dataclass
        """
        obj = cls.parse_json(json_str)

        fields = cls.__annotations__

        sobj = {
            key: value for key, value in obj.items()
            if fields.get(key, None) is not None
        }
        return cls(**sobj)


@dataclass
class IAMBindings:

    members: List[str]
    role: str


@dataclass
class IAMBinding:
    """
    By default, if the 'email' does not
    contain a namespace prefix, it will be
    set to "serviceAccount"
    """

    ns: str
    email: str
    role: str

    def __post_init__(self):

        maybe_split = self.email.split(":")
        if len(maybe_split) == 2:
            self.ns = maybe_split[0]
            self.email = maybe_split[1]
        else:
            self.ns = "serviceAccount"

    @property
    def sa_email(self):
        return f"{self.ns}:{self.email}"


@dataclass
class IPAddress(_base):
    """
    Compute Engine IP address
    """
    name: str
    address: str
    addressType: str
    ipVersion: str


@dataclass
class CloudRunRevisionSpec:
    """
    Cloud Run Revision Specification (flattened)
    """
    name: str
    url: str
    labels: Dict

    @classmethod
    def from_string(cls, json_str: str):

        obj = JsonObject.from_string(json_str)

        d = {
            "url": obj["status.url"],
            "labels": obj["spec.template.metadata.labels"],
            "name": obj["metadata.name"],
        }

        return cls(**d)


@dataclass
class BackendGroup:
    balancingMode: str
    group: str
    capacityScaler: int


@dataclass
class BackendServiceSpec:

    name: str
    port: int
    portName: str
    protocol: str
    backend_groups: List[BackendGroup]

    @classmethod
    def from_string(cls, json_str: str):

        obj = JsonObject.from_string(json_str)

        raw_groups = obj["backends"]
        groups = []

        for group in raw_groups:
            group = BackendGroup(**group)
            groups.append(group)

        d = {
            "name": obj["name"],
            "port": obj["port"],
            "portName": obj["portName"],
            "protocol": obj["protocol"],
            "backend_groups": groups
        }

        return cls(**d)
