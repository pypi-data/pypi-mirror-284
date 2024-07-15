import copy
import json
import random
import shutil
import zipfile
import os
import datetime
import hashlib
import re

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives import hmac as cr_hmac

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_der_public_key, load_pem_public_key, load_pem_private_key, \
	load_der_private_key

import hmac


def tohexstr(input):
	if type(input) == str:
		return input
	return input.hex()


def tobytes(input):
	if type(input) == str:
		return bytes.fromhex(input)
	elif type(input) == bytes:
		return input
	else:
		return bytes(input)

def is_hex_string(s):
	"""
	입력받은 문자열이 16진수 문자열인지 검사합니다.
	:param s: 검사할 문자열
	:return: 16진수 문자열이면 True, 아니면 False
	"""
	# 문자열이 공백인 경우 False 반환
	if not s:
		return False
	# 문자열이 16진수 패턴에 맞는지 검사
	pattern = r'^[0-9a-fA-F]+$'
	if not re.match(pattern, s):
		return False
	# 문자열 길이가 짝수인지 검사
	if len(s) % 2 != 0:
		return False

	return True

def SHA256(value: bytes) -> str:
	return hashlib.sha256(value).digest().hex()


def SHA1(input: bytes) -> str:
	return hashlib.sha1(input).digest().hex()


def StrFromFile(filepath, enc='utf-8'):

	fb = open(filepath, 'rb')
	rt = fb.read()
	fb.close()
	return rt

def get_file_name(path):
	return os.path.basename(path)


def ECDH(pem_prk:str, pem_puk:str)->bytes:
	puk = load_pem_public_key(pem_puk.encode(),default_backend())
	prk = load_pem_private_key(pem_prk.encode(),None,default_backend())
	return prk.exchange(ec.ECDH(), puk)


def zero(length:int) -> bytes:
	return b'\x00'*length


def AES_ENC_CBC(symm_key: bytes, msg: bytes) -> bytes:
	iv = zero(16)
	cipher = Cipher(algorithms.AES(symm_key), modes.CBC(iv),default_backend())
	encryptor = cipher.encryptor()
	ct = encryptor.update(msg) + encryptor.finalize()

	return ct


def AES_DEC_CBC(symm_key: bytes, enc_msg: bytes) -> bytes:
	iv = zero(16)
	cipher = Cipher(algorithms.AES(symm_key), modes.CBC(iv),default_backend())
	decryptor = cipher.decryptor()
	msg = decryptor.update(enc_msg) + decryptor.finalize()

	return msg


def HMAC(hmac_key: bytes, msg: bytes) -> bytes:

	h = cr_hmac.HMAC(hmac_key, hashes.SHA256(),default_backend())
	h.update(msg)
	return h.finalize()


def RANDOM(length):
	return bytes(random.getrandbits(8) for _ in range(length))


def print_formatting(data: dict, key_list=None):
	if key_list is None:
		key_list = []
	for key, value in data.items():
		if isinstance(value, dict):
			key_list.append(key)
			print_formatting(value, key_list)
			key_list.remove(key)
		else:
			if isinstance(value, str) and len(value) > 50:
				data[key] = value[:50] + "......"
	return data


def print_data(data: dict, msg_cut=False):
	temp = copy.deepcopy(data)
	if msg_cut:
		return json.dumps(print_formatting(temp), indent=2, ensure_ascii=False)
	return json.dumps(temp, indent=2, ensure_ascii=False)


def pad(data: bytes):
	"""
	pkcs5 padding
	"""
	block_size = 16
	pad_len = block_size - len(data) % block_size
	return data + (bytes([pad_len]) * pad_len)


# pkcs5 - unpadding
def unpad(data: bytes):
	return data[:-ord(data[-1:])]

