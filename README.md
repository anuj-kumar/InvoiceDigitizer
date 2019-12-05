# InvoiceDigitizer

## Architecture
![](https://raw.githubusercontent.com/anuj-kumar/InvoiceDigitizer/master/InvoiceDigitizerArchitecture.png?token=AAZTS5WE4GKEESHAO3XGPJC55FPGS)

## Context

### Digifier
This app takes care of the digitization.
1. A document is uploaded to the `digifier` API.
2. Backend submits it to digitization queue.
3. Digitization status is updated in the cache.
4. A celery worker picks up the request from the queue and processes the digitization.
5. The status is again updated in the cache.

### Invoice
This app takes care of everything post automatic digitization. Digitized invoices are maintained in a structured format here.
The put API can make updates to existing docs.

## Not implemented
1. External raw invoice store such as S3.
2. Logic for digitization.
3. API Auth.
