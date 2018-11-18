# DjangoApi
Test the App by installing required frameworks given in requirements.txt. Basic python support is required. The Django version must be compatible for checking API instances with python version being 3.6.
TASK

Test Django API for various tasks for reducing load on server and better optimization.Recieve proper response from clients for interaction between different software components.Amend necessary GUI for integrating API at the endpoints.

WORK

The first API till 15/11/2018 tests the headers of uploaded xlsx sheets and makes entries in MongoDb.If MongoDb not created the API should create an API for itself.Further uploads take the created database for updation.The uploaded sheets makes a new document entry in the collection populated with the headers.Every sheets must be associated with a SKU(admin).
The second API generates a list of union of headers from both the input and output xlsx sheets.This must not ignore headers with different case and having special charecters.

INFERENCE

Endpoint verification via Postman
