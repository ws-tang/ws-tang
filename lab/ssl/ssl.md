# SSL Setup and Configuration

One can use [OpenSSL](https://www.openssl.org/) for typical SSL certificate handling (identity/key certificates and trust certificates).

`OpenSSL` is used for the notes herein. There are other utilities like **Java** `keytool` to manage SSL certificates in different formats.

The version of OpenSSL referred herein is OpenSSL **3.0.13** from a **Ubuntu Server 22.04** Linux server. Refer to [**Setup the Lab Environment with a Linux Server**](../linuxBase.md) for a base lab Linux environment.

<br/>

## OpenSSL

**References**

- [Download](https://openssl-library.org/source/)
- Documentation: [master](https://docs.openssl.org/master/) or [OpenSSL 3.0](https://docs.openssl.org/3.0/)
- [OpenSSL Guide](https://docs.openssl.org/3.2/man7/ossl-guide-introduction/)
- [OpenSSL Release (main)](https://github.com/openssl/openssl/releases?page=1)
- [OpenSSL Certificate Authority](https://jamielinux.com/docs/openssl-certificate-authority/index-full.html) by **Jamie Nguyen**

### OpenSSL Commands for CA Certificates

Refer to the file [openssl.cnf](./openssl.cnf) for the default OpenSSL configuration. This `openssl.cnf` comes from OpenSSL 3.0.13 for Ubuntu Server 22.04.

_Create a private CA_
Step 1: Create the key and CA certificate:

```
openssl genrsa -aes256 -out private/ocspca.key.pem 4096

openssl req -config ocsp.cnf -key private/ocspca.key.pem -new -x509 -days 7300 -sha256 -extensions v3_issued -out certs/ocspca.cert.pem
```

_Create the OCSP server certificate_

```
openssl genrsa -aes256 -out private/ocsp-cert.key 2048

openssl req -config ocsp.cnf -new -sha256 -key private/ocsp-cert.key -out csr/ocsp-cert.csr

openssl ca -config ocsp.cnf -extensions ocsp -days 730 -notext -md sha256 -in csr/ocsp-cert.csr -out certs/ocsp-cert.crt
```

_Create a browser cert with OCSP URL_

```
openssl genrsa -aes256 -out private/ocspbrowser-cert.key 2048

openssl req -config ocsp.cnf -key private/ocspbrowser-cert.key -new -sha256 -out csr/ocspbrowser-cert.csr

openssl ca -config ocsp.cnf -policy signing_policy -extensions signing_req -out certs/ocspbrowser-cert.pem -infiles csr/ocspbrowser-cert.csr

openssl pkcs12 -export -inkey private/ocspbrowser-cert.key -in certs/ocspbrowser-cert.pem -out ocspbrowser-cert.p12
```

_Revoke a certificate_

```
openssl ca -revoke newcerts/1001.pem -keyfile private/ocspca-cert.key -cert ocspca-cert.pem
```

### OpenSSL Commands for CA CRL

_Create a CRL_

```
openssl ca -config ocsp.cnf -gencrl -out crl/ocspca-crl.pem
```

_View a CRL_

```
openssl crl -text -noout -in crl/ocspca-crl.pem
```

_Verify a cert against its CA and CRL_

```
openssl verify -crl_check -CAfile crl_chain.pem certs/ocspbrowser.cert.pem
```

(Note the crl_chain.pem contains both the signing CA public cert and the CRL)

_Covert a CRL from PEM to DER_

```
openssl x509 -in cert.crt -outform der -out cert.der
```

### OpenSSL OCSP Commands

_Run OCSP Responder with OpenSSL_

```
openssl ocsp -port _PORT_ -sha256 -index _CA_IDX_FILE_ -CA _CA_CHAIN_PEM_ -rkey _SERVER_CERT_KEY_ -rsigner _SERVER_CERT_PEM_ -text -out log.txt
```

Example:

```
openssl ocsp -port 23456 -sha256 -index index.txt -CA ocsp-ca-chain.pem -rkey ocsp-server-cert.key -rsigner ocsp-server-cert.pem -text -out log.txt
```

_Issue a OCSP request with OpenSSL_

```
openssl ocsp -issuer _ISSUER_CERT_ -cert _CERT_TO_CHECK_ -CAfile _CA_SIGN_OCSP_RESP_SVR_CERT_ -url _OCSP_URL_ -resp_text -respout resp.der
```

Example:

```
openssl ocsp -issuer ocsp-ca-chain.pem -cert certs/browser.cert.pem -CAfile ocsp-ca-chain.pem -url http://server4911-vm02.richlab.avaya.com:23456 -resp_text -respout resp.der
```

_View OCSP response via OpenSSL_

```
openssl ocsp -respin resp.der -text -noverify
```

<br/>
