# Welcome to ANON3605's Cryptography Repository

> *“Security is not a feature. It’s a discipline.”*

Welcome to my personal cryptography lab. This repository contains my explorations, implementations, and practical experiments in modern cryptography techniques. It's structured for clarity, minimalism, and function — no bloat, no noise.

---

##  Topics Covered

### 1. Encoding / Decoding
Low-level transformations of data for representation, storage, or transmission.

- Base64, Base32, Hex
- UTF-8 ↔ ASCII ↔ Binary
- Manual bitwise manipulations

### 2. Encryption / Decryption
Secure reversible transformations to protect confidentiality and integrity.

- Symmetric Ciphers (AES, DES)
- Asymmetric Ciphers (RSA, ECC)
- Custom implementations (Caesar, Vigenère)

### 3. Hashing
One-way irreversible functions used for integrity verification, fingerprints, and secure storage.

- SHA Family (SHA1, SHA256, SHA3)
- MD5 (for comparison only, not recommended)
- HMAC, PBKDF2

---

## Directory Structure

cryptography/\n
├── encoding_decoding/
│ ├── base64_tool.py
│ ├── binary_ascii_converter.py
│ └── hex_utf_converter.py
│
├── encryption_decryption/
│ ├── aes_cipher.py
│ ├── rsa_toolkit.py
│ └── custom_ciphers/
│ ├── caesar.py
│ └── vigenere.py
│
├── hashing/
│ ├── sha_hashing.py
│ ├── md5_demo.py
│ └── hmac_pbkdf2.py
│
└── README.md


## Dependencies

- Python ≥ 3.8  
- `cryptography`  
- `pycryptodome`  
- `hashlib`, `base64`, `binascii`

Install with:

```bash
pip install -r requirements.txt

