# Learning Notes

OS: Windows 11

## Step-by-step
1. Generate SSH key, then upload SSH public key to GCP's VM.
```
ssh-keygen -t rsa -f {KEY_NAME} -C {VM_USERNAME} -b 2048 
```
For my case, it looks like this:
```
ssh-keygen -t rsa -f gcp -C ammmar -b 2048
```