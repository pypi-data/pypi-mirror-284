from datetime import datetime, timedelta
import json
import MediLink_API_v3

try:
    from MediLink import MediLink_ConfigLoader
except ImportError:
    import MediLink_ConfigLoader

# Load configuration
config, _ = MediLink_ConfigLoader.load_configuration()

# Initialize the API client
client = MediLink_API_v3.APIClient()

# Get provider_last_name and npi from configuration
provider_last_name = config['MediLink_Config'].get('default_billing_provider_last_name')
npi = config['MediLink_Config'].get('default_billing_provider_npi')

# Define the list of payer_id's to iterate over
payer_ids = ['87726']  # Default value
# If there is a specific list of payer_ids, it should be defined here
# payer_ids = ['87726', '12345', '67890']

# List of patients with DOB and MemberID
patients = [
    ('1959-02-20', '985269007'),
    ('1959-03-16', '916622481')
]

# Function to get eligibility information
def get_eligibility_info(client, payer_id, provider_last_name, date_of_birth, member_id, npi):
    eligibility = MediLink_API_v3.get_eligibility(client, payer_id, provider_last_name, 'MemberIDDateOfBirth', date_of_birth, member_id, npi)
    return eligibility

# Function to extract required fields and display in a tabular format
def display_eligibility_info(patient_info_list):
    table_header = "{:<20} | {:<10} | {:<10} | {:<15} | {:<10} | {:<20} | {:<15} | {:<20}".format(
        "Patient Name", "DOB", "Payer ID", "Insurance Type", "Type Code", "Eligibility End Date", "Policy Status", "Remaining Amount")
    print(table_header)
    print("-" * len(table_header))
    
    for data, dob, member_id in patient_info_list:
        for policy in data["memberPolicies"]:
            # Skip non-medical policies
            if policy["policyInfo"]["coverageType"] != "Medical":
                continue

            patient_info = policy["patientInfo"][0]
            lastName = patient_info.get("lastName", "")
            firstName = patient_info.get("firstName", "")
            middleName = patient_info.get("middleName", "")

            # TODO This needs to be upgraded because sometimes the remaining amount is per family. Need to check 'message'. There's some complicated if that needs to go here.
            remaining_amount = policy["deductibleInfo"]["individual"]["inNetwork"].get("remainingAmount", "")

            insurance_info = policy["insuranceInfo"]
            ins_insuranceType = insurance_info.get("insuranceType", "")
            ins_insuranceTypeCode = insurance_info.get("insuranceTypeCode", "")
            ins_memberID = insurance_info.get("memberId", "")
            ins_payerID = insurance_info.get("payerId", "")

            policy_info = policy["policyInfo"]
            eligibilityDates = policy_info.get("eligibilityDates", "")
            policy_status = policy_info.get("policyStatus", "")

            patient_name = "{} {} {}".format(firstName, middleName, lastName).strip()

            # Create a summary JSON
            summary = {
                "Payer ID": ins_payerID,
                "Provider": provider_last_name,
                "Member ID": ins_memberID,
                "Date of Birth": dob,
                "Patient Name": patient_name,
                "Patient Info": {
                    "DOB": dob,
                    "Address": "{} {}".format(patient_info.get("addressLine1", ""), patient_info.get("addressLine2", "")).strip(),
                    "City": patient_info.get("city", ""),
                    "State": patient_info.get("state", ""),
                    "ZIP": patient_info.get("zip", ""),
                    "Relationship": patient_info.get("relationship", "")
                },
                "Insurance Info": {
                    "Payer Name": insurance_info.get("payerName", ""),
                    "Payer ID": ins_payerID,
                    "Member ID": ins_memberID,
                    "Group Number": insurance_info.get("groupNumber", ""),
                    "Insurance Type": ins_insuranceType,
                    "Type Code": ins_insuranceTypeCode,
                    "Address": "{} {}".format(insurance_info.get("addressLine1", ""), insurance_info.get("addressLine2", "")).strip(),
                    "City": insurance_info.get("city", ""),
                    "State": insurance_info.get("state", ""),
                    "ZIP": insurance_info.get("zip", "")
                },
                "Policy Info": {
                    "Eligibility Dates": eligibilityDates,
                    "Policy Member ID": policy_info.get("memberId", ""),
                    "Policy Status": policy_status
                },
                "Deductible Info": {
                    "Remaining Amount": remaining_amount
                }
            }

            # Print debug JSON
            # Uncomment below if you need to debug later
            # print("\nDebug JSON Summary:")
            # print(json.dumps(summary, indent=2))

            # Display patient information in a table row format
            eligibility_end_date = eligibilityDates.get("endDate", "")
            table_row = "{:<20} | {:<10} | {:<10} | {:<15} | {:<10} | {:<20} | {:<15} | {:<20}".format(
                patient_name, dob, ins_payerID, ins_insuranceType, ins_insuranceTypeCode, eligibility_end_date, policy_status, remaining_amount)
            print(table_row)

# Loop through each payer_id and patient to call the API, then display the eligibility information
patient_info_list = []
for payer_id in payer_ids:
    for dob, member_id in patients:
        eligibility_data = get_eligibility_info(client, payer_id, provider_last_name, dob, member_id, npi)
        patient_info_list.append((eligibility_data, dob, member_id))

display_eligibility_info(patient_info_list)