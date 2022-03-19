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
2. Create a GCP Compute Engine VM Instance. Note down the external IP address.
3. Access the server by SSH tunneling by executing
```
ssh -i ~/.ssh/{KEY_NAME} {VM_USERNAME}@{EXTERNAL_IP_ADDRESS}
```
In my case, it looks like this
```
ssh -i ~/.ssh/gcp ammar@34.xxx.xxx.xx
```
4. To simplify ssh access, create a `config` file under `~/.ssh`, and add these lines into the config file
```
Host {VM_HOSTNAME}
    HostName {EXTERNAL_IP_ADDRESS}
    User {VM_USERNAME}
    IdentityFile {PATH_TO_SSH_PRIVATE_KEY}
```
In my case, it looks like this
```
Host data-eng-zoomcamp
    HostName 34.xxx.xxx.xx
    User ammar
    IdentityFile "c:/Users/Ammar Chalifah/.ssh/gcp"
```
To access the remote server, just type
```
ssh data-eng-zoomcamp
```
5. Start configuring and setting up the remote server. Use VS Code remote server extension to access the server via GUI. Use VS Code port forwarding as well to access the interfaces.