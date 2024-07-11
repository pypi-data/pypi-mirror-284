"""
TODOS:
    1. eventually we need to seperate this out to client and server utils
"""
import cloudpickle
import logging
import json
import requests
import pickle
import codecs

logger = logging.getLogger(__name__)


def decode_str(obj_in_str):
    return pickle.loads(codecs.decode(obj_in_str.encode("utf-8"), "base64"))


def encode_obj(obj):
    return codecs.encode(cloudpickle.dumps(obj), "base64").decode("utf-8")


def check_response(resp):
    if not resp.ok:
        if resp.status_code == 422:
            raise ValueError(
                "Request to {} not sucessful, Error Code: {}, your JWT token is invalid or incorrect, \
                please delete the previous token at ~/.kaleidoscope.jwt and generate a new one".format(
                    resp.url, resp.status_code
                )
            )
        elif resp.status_code == 401:
            raise ValueError(
                "Request to {} not sucessful, Error Code: {}, your JWT token is expired, please \
                    delete the previous token at ~/.kaleidoscope.jwt and generate a new one".format(
                    resp.url, resp.status_code
                )
            )
        raise ValueError(
            "Request to {} not sucessful, Error Code: {}, {}".format(
                resp.url, resp.status_code, resp.json()["msg"]
            )
        )
    logger.debug("addr %s response code %s", resp.url, resp.status_code)


def get(addr, auth_key=None, headers={}):

    if auth_key:
        headers["Authorization"] = f"Bearer {auth_key}"

    resp = requests.get(addr, headers=headers)
    check_response(resp)

    return resp.json()


def post(addr, body, auth_key=None, headers={}):

    if auth_key:
        headers["Authorization"] = f"Bearer {auth_key}"

    resp = requests.post(addr, json=body, headers=headers)
    check_response(resp)

    return resp.json()
