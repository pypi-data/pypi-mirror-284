import requests
import os
import urllib3
from pprint import pprint
import json
import requests
import os
import sys
import datetime
import tempfile
import pynetbox
import urllib3
import datetime
from awx.awx_common import awx_get_id
from awx.awx_common import getawxdata
from awx.awx_credential import awx_create_credential
from common import prettyllog
from awx.awx_organisation import awx_create_organization
from awx.awx_project import awx_create_project
from awx.awx_project import awx_get_project
from ..common import get_vault_secret
from ..common import get_vault_secret_data
from ..common import get_vault_secret_field
from ..common import get_vault_secret_field_decrypt
from ..common import get_vault_secret_field_encrypt
from ..common import get_vault_client
from ..common import decrypt_text
from ..common import encrypt_text

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
VERIFY_SSL = False



def awx_get_organization(orgid, mytoken=None, r=None):
  headers = {"User-agent": "python-awx-client", "Content-Type": "application/json","Authorization": "Bearer {}".format(ansibletoken)}
  url = os.getenv("IGN8_AAP_HOST") + "/api/v2/organizations/%s" % orgid
  resp = requests.get(url,headers=headers, verify=VERIFY_SSL)
  return   json.loads(resp.content)

def aap_organisations():
    url = secrets["aaphost"] + "
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    data = {
        "client_id": secrets["client_id"],
        "client_secret": secrets["client_secret"],
        "username": secrets["username"],
        "password": secrets["password"],
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    return response.json()



def status():
    #We need to create an ascii menu that shows the status of the AAP
    #We need to show the status of the AAP
    hvac_client = get_vault_client()
    

    print("AAP Status")
    print("==========")
    print("Checking AAP Status")
    print("Please wait...")
    print(default_secrets())
    print("....")



    