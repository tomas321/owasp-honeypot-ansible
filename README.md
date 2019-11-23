# owasp-honeypot-ansible

Provide deployment for [OWASP python Honeypot](https://www.owasp.org/index.php/OWASP_Python_Honeypot). It comprises of Ansible roles required to install and prepare the honeypot.

## Structure

`docker` - Ansible role to install Docker.

`mongodb` - Ansible role to install mongodb.

`owasp-honeypot` - Ansible role followinf OWASP honeypot [installation guide](https://github.com/zdresearch/OWASP-Honeypot/wiki/Installation)

## Example Ansible playbook

    - hosts: servers
      roles:
        - owasp_honeypot/docker
        - owasp_honeypot/mongodb
        - owasp_honeypot/owasp-honeypot
