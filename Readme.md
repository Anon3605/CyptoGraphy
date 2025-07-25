<h1 align="center">Anon3605's Cryptography Repository</h1>
<p align="center">
  <em>Low-level data control. High-level discipline.</em><br>
  <strong>Encoding | Encryption | Hashing</strong><br>
  If you see this, don't mess others with these codes
</p>

---

##  Overview

Welcome to the private cryptography vault of **Mr X**.  
This repository documents and demonstrates the foundational and advanced components of modern cryptographic systems, written from scratch and tested for security behavior in isolated lab environments.

> ⚠ For research and educational purposes only. Misuse is your responsibility, not mine.

---

##  Contents

<table>
  <tr>
    <td><strong> Encoding / Decoding</strong></td>
    <td>Base64, Hex, ASCII ↔ Binary, UTF conversions</td>
  </tr>
  <tr>
    <td><strong> Encryption / Decryption</strong></td>
    <td>AES, RSA, Caesar, Vigenère, stream/block ciphers</td>
  </tr>
  <tr>
    <td><strong> Hashing</strong></td>
    <td>SHA-2, SHA-3, MD5 (demo only), HMAC, PBKDF2</td>
  </tr>
</table>

---

## File Structure

```text
cryptography/
├── encoding_decoding/
│   ├── base64_tool.py
│   ├── binary_ascii_converter.py
│   └── hex_utf_converter.py
│
├── encryption_decryption/
│   ├── aes_cipher.py
│   ├── rsa_toolkit.py
│   └── custom_ciphers/
│       ├── caesar.py
│       └── vigenere.py
│
├── hashing/
│   ├── sha_hashing.py
│   ├── md5_demo.py
│   └── hmac_pbkdf2.py
│
└── README.md
