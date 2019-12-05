# InvoiceDigitizer

## Architecture
![](https://github.com/anuj-kumar/InvoiceDigitizer/blob/master/InvoiceDigitizerArchitecture.png)

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

## Yet To Do / Not Implemented yet
1. Test Code.
1. External raw invoice store such as S3.
1. Logic for digitization.
1. API Auth.
1. Cache expiry time setup.
1. Dedicated queue for invoice digitization setup. Currently default queue is being used.
