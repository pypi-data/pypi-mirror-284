# Example illustration using the blueguard client to access the blueguard privacy APIs
# To be able run this client from command-line
# `cd src` and run `python -m blueguard_client.client_example`
import os, json
from blueguard_client import BlueGuardAPIClient, Mode

# Load the API_KEY variable
api_key = os.getenv('BLUEGUARD_API_KEY')
org_uuid = os.getenv('ORG_UUID')

# Initialize Blueguard API Client with URL
BLUEGUARD_SCHEME = "https"
BLUEGUARD_HOST = "localhost"
BLUEGUARD_URL = BLUEGUARD_SCHEME + "://" + BLUEGUARD_HOST

bgx_client = BlueGuardAPIClient(url = BLUEGUARD_URL, api_key=api_key, org_uuid=org_uuid)
#bgx_client = BlueGuardAPIClient(url="http://localhost:5000", api_key=api_key, org_uuid=org_uuid)

# Check the health of the server /ping/
print(bgx_client.health())

# Get the current version of the server
print(bgx_client.get_version())

###############################
#   Sample Redact example     
###############################

sample_text = ['Hi Sam, how are you. Whats your Margin', 'I live in Chennai']
response = bgx_client.process_text(Mode.REDACT, text_inputs=sample_text)
print(f"\n\n Original text: {sample_text}")
print(response.processed_text, response.context_id)

################################################
#   Sample Mask example with 
#       ==> Detailed index positions enabled
################################################

response = bgx_client.process_text(Mode.MASK, text_inputs=sample_text
                                   , enable_details = True)
print(f"\n\n Original text: {sample_text}")
print(f"Output: {json.dumps(response.output, indent=4)} ")

################################################
#   Sample REDACT example with 
#       ==> Sensitive terms scanning enabled
################################################

response = bgx_client.add_or_update_confidential_terms(keywords = ["revenue margin"]) # Custom confidential term added

sample_text = ["Hi Ram. The current revenue margin has hit 10%."]

response = bgx_client.process_text(Mode.REDACT, text_inputs=sample_text
                                   , enable_sensitive_scan = True) # False, turns the senstive terms detection off.
print(f"\n\n Original text: {sample_text}")
print(f"{response.processed_text}")

#########################################
#   Sample REPLACE example with
#   => custom confidential terms detected, replaced
#########################################

sample_text = ["Hi Ram, I lost my cc card in Chennai", "Product retrograde is ambitious"]

bgx_client.add_or_update_confidential_terms(keywords = ["retrograde", "card"]) # Custom confidential term added

response = bgx_client.process_text(Mode.REPLACE, text_inputs=sample_text
                                   , enable_sensitive_scan = True)
print(f"\n\n Original text: {sample_text}")
print("############## CONFIDENTIAL Terms Detected, Redacted: ############## \n", response.processed_text, response.context_id)

############################
#  Retrieve the text back
############################

# Let us recall the original text by calling reidentify_text with the previously processed (redacted/masked/replaced) text
original_text_reidentified = bgx_client.reidentify_text(text_inputs= response.processed_text
                                                        , context_id = response.context_id[0] # context_id that was originally passed to the original de-identification
                                                        , enable_details = True) 
print(f"\n\nProcessed text: {response.processed_text}")
print(f"############## Retrieved Original Text: ############## \n {original_text_reidentified.original_text[0]}")


########################################
#   Enable Scanning Secret Credentials
#   AWS, Google, OAuth, pgp, rsa,
#   slack, ssh, stripe and more ...
#########################################

sample_text = ["How do I set up AWS Config. Here's my key AKIASD5L34F2GHJFPGE7"]

# Redact text Sensitive Terms Scanned
response = bgx_client.process_text(Mode.REDACT, text_inputs=sample_text
                                   , identify_credentials = True) #False, turns off the detection
print(f"{response.extract_detailed_info()}")