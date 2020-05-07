import json

def entityContactPoint(entity_id, washlist):
    contactpoints = []
    contactpoint = {}

    email = contactPointEmail(entity_id)
    url = contactPointUrl(entity_id)
    name = contactPointName(entity_id)

    if url is not None:
        contactpoint['hasURL'] = url
    if email in washlist['whiteList']:
        contactpoint['email'] = email
        contactpoint['organizationUnit'] = name
    elif email in washlist['blackListNameByEmail']:
        contactpoint['email'] = email

    contactpoints.append(contactpoint)
    return contactpoints

def contactPointEmail(entity_id):
    email_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_data_contact_mail.json')
    email_field = json.load(email_file)
    email = email_field['field_data_contact_mail_value'].get('0')

    return email

def contactPointName(entity_id):
    name_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_data_contact_name.json')
    name_field = json.load(name_file)
    name = name_field['field_data_contact_name_value'].get('0')

    return name

def contactPointUrl(entity_id):
    url = {}
    org_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_organization.json')
    org = json.load(org_file)

    if org['field_organization_nid'].get('0'):
        homepage_file = open('../tmp/extract/organization/' + str(org['field_organization_nid'].get('0')) + '/field_data_field_organization_homepage.json')
        homepage = json.load(homepage_file)
        url = homepage['field_organization_homepage_value'].get('0')
    return url

