from mongoengine import fields,  Document
from datetime import datetime

class User(Document):
    name = fields.StringField(required=True)
    username = fields.StringField(required=True)
    password = fields.StringField(required=True)
    status = fields.BooleanField(default=True)
    client = fields.BooleanField(default=False)
    role = fields.StringField(required=False)
    created_at = fields.DateTimeField(default=datetime.utcnow)



class Project(Document):
    name = fields.StringField(required=True)
    client = fields.ReferenceField(User, required=True)
    input_files  = fields.ListField(required=True)
    data_files = fields.ListField(required=False)
    out_put_template = fields.ListField(required=False)
    status = fields.BooleanField(default=False)
    created_at = fields.DateTimeField(default=datetime.utcnow())
    # created_by = fields.ReferenceField(User, required=True)

class Output_headers(Document):
    project = fields.ReferenceField(Project, required=True)
    headers = fields.ListField(required=True)
    file_name = fields.StringField(required=True)
    sheet_name = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow)

class Input_headers(Document):
    project = fields.ReferenceField(Project, required=True)
    headers = fields.DictField(required=True)
    file_name = fields.StringField(required=True)
    sheet_name = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow)

class Product(Document):
    project = fields.ReferenceField(Project, required=True)
    sku = fields.StringField(required=False)
    details = fields.DictField(required=True)
    file_name = fields.StringField(required=True)
    sheet_name = fields.StringField(required=True)
    input_headers = fields.ReferenceField(Input_headers, required=True)
    status = fields.BooleanField(default=False)
    created_at = fields.DateTimeField(default=datetime.utcnow)


class DataFiles(Document):
    project = fields.ReferenceField(Project, required=True)
    details = fields.DictField(required=True)
    file_name = fields.StringField(required=True)
    sheet_name = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow)

class Rules(Document):
    project = fields.ReferenceField(Project, required=True)
    details = fields.StringField(required=True)
    file_name = fields.StringField(required=True)
    sheet_name = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow)


class Content(Document):
    project = fields.ReferenceField(Project, required=True)
    content = fields.DictField(required=True)
    file_name = fields.StringField(required=True)
    sheet_name = fields.StringField(required=True)
    input_headers = fields.ReferenceField(Input_headers, required=True)
    status = fields.BooleanField(default=False)
    created_at = fields.DateTimeField(default=datetime.utcnow)

