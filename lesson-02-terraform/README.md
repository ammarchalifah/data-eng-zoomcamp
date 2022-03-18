# Learning Notes

Terraform is am Infrastructure-as-Code (IaC) used to build, change, and manage infrastructure in a safe, consistent, and repeatable way. Terraform is an open-source tool developed by HashiCorp.

OS: Windows 11

## Step-by-step
1. Install `gcloud` SDK
2. Install `terraform` CLI
3. Create GCP account
4. Create a project in GCP account
5. Create a service account and assign **Storage Admin**, **Storage Object Admin**, and **BigQuery Admin** roles.
6. Download the service account key (`.json`) and place it in the current directory.
7. Enable IAM API and IAM Credential API in the GCP
8. Login to GCP via CLI with
```
gcloud auth login --cred-file={PATH-TO-GCP-CREDENTIAL}.json
```
9. Initialize terraform (used to set up environment and install the relevant providers, in this case Google provider managed by HashiCorp).
```
terraform init
```
10. Plan terraform infrastructure creation with
```
terraform plan -var="project=<your-gcp-project-path>" -var="credentials="<your-gcp-json-key>"
```
11. Create new infrastructure by applying them
```
terraform apply -var="project=<your-gcp-project-path>" -var="credentials="<your-gcp-json-key>"
```
12. Check your GCP console to see the implemented changes.
13. Once done, destroy your resources by 
```
terraform destroy
```