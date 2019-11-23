#!/bin/bash

sudo python3 {{ ansible_env.HOME }}/{{ owasp_honeypot_repo_dest }}/owasp-honeypot/ohp.py -m ssh/weak_password,ics/veeder_root_guardian_ast,http/basic_auth_weak_password,ftp/weak_password "$@"
