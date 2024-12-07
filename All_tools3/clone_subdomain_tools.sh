#!/bin/bash

# Array of GitHub repository URLs
repos=(
    "https://github.com/aboul3la/Sublist3r"
    "https://github.com/OWASP/Amass"
    "https://github.com/blechschmidt/massdns"
    "https://github.com/Findomain/Findomain"
    "https://github.com/Screetsec/Sudomy"
    "https://github.com/projectdiscovery/chaos-client"
    "https://github.com/TypeError/domained"
    "https://github.com/appsecco/bugcrowd-levelup-subdomain-enumeration"
    "https://github.com/projectdiscovery/shuffledns"
    "https://github.com/d3mondev/puredns"
    "https://github.com/christophetd/censys-subdomain-finder"
    "https://github.com/fleetcaptain/Turbolist3r"
    "https://github.com/0xbharath/censys-enumeration"
    "https://github.com/LordNeoStark/tugarecon"
    "https://github.com/cinerieus/as3nt"
    "https://github.com/si9int/Subra"
    "https://github.com/nexxai/Substr3am"
    "https://github.com/jhaddix/domain/"
    "https://github.com/infosec-au/altdns"
    "https://github.com/anshumanbh/brutesubs"
    "https://github.com/lorenzog/dns-parallel-prober"
    "https://github.com/rbsec/dnscan"
    "https://github.com/guelfoweb/knock"
    "https://github.com/hakluke/hakrevdns"
    "https://github.com/projectdiscovery/dnsx"
    "https://github.com/projectdiscovery/subfinder"
    "https://github.com/tomnomnom/assetfinder"
    "https://github.com/nahamsec/crtndstry"
    "https://github.com/codingo/VHostScan"
    "https://github.com/edoardottt/scilla"
    "https://github.com/3nock/sub3suite"
    "https://github.com/glebarez/cero"
    "https://github.com/incogbyte/shosubgo"
    "https://github.com/hakluke/haktrails"
    "https://github.com/blacklanternsecurity/bbot"
)

# Directory where repositories will be cloned
clone_dir="subdomain_enumeration_tools"

# Create directory if not exists
mkdir -p $clone_dir

# Change to the directory
cd $clone_dir

# Loop through the array and clone each repository
for repo in "${repos[@]}"; do
    git clone $repo
done

echo "All repositories have been cloned."
