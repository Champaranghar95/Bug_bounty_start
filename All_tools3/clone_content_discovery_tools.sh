#!/bin/bash

# Array of GitHub repository URLs for content discovery tools, link extraction, parameters, and fuzzing
repos=(
    # Content Discovery
    "https://github.com/OJ/gobuster"
    "https://github.com/C-Sto/recursebuster"
    "https://github.com/epi052/feroxbuster"
    "https://github.com/maurosoria/dirsearch"
    "https://github.com/evilsocket/dirsearch"
    "https://github.com/henshin/filebuster"
    "https://github.com/stefanoj3/dirstalk"
    "https://github.com/digination/dirbuster-ng"
    "https://github.com/jaeles-project/gospider"
    "https://github.com/hakluke/hakrawler"
    "https://github.com/s0rg/crawley"
    "https://github.com/projectdiscovery/katana"

    # Links
    "https://github.com/GerbenJavado/LinkFinder"
    "https://github.com/zseano/JS-Scan"
    "https://github.com/arbazkiraak/LinksDumper"
    "https://github.com/0xsha/GoLinkFinder"
    "https://github.com/InitRoot/BurpJSLinkFinder"
    "https://github.com/IAmStoxe/urlgrab"
    "https://github.com/tomnomnom/waybackurls"
    "https://github.com/lc/gau"
    "https://github.com/003random/getJS"
    "https://github.com/riza/linx"
    "https://github.com/xnl-h4ck3r/waymore"
    "https://github.com/xnl-h4ck3r/xnLinkFinder"

    # Parameters
    "https://github.com/maK-/parameth"
    "https://github.com/PortSwigger/param-miner"
    "https://github.com/Bo0oM/ParamPamPam"
    "https://github.com/s0md3v/Arjun"
    "https://github.com/devanshbatham/ParamSpider"
    "https://github.com/Sh1Yo/x8"

    # Fuzzing
    "https://github.com/xmendez/wfuzz"
    "https://github.com/ffuf/ffuf"
    "https://github.com/fuzzdb-project/fuzzdb"
    "https://github.com/1N3/IntruderPayloads"
    "https://github.com/Bo0oM/fuzz.txt"
    "https://github.com/googleprojectzero/fuzzilli"
    "https://github.com/Fuzzapi/fuzzapi"
    "https://github.com/ameenmaali/qsfuzz"
    "https://github.com/d4rckh/vaf"
)

# Directory where repositories will be cloned
clone_dir="content_discovery_tools"

# Create directory if it doesn't exist
mkdir -p $clone_dir

# Change to the directory
cd $clone_dir

# Loop through the array and clone each repository
for repo in "${repos[@]}"; do
    git clone $repo
done

echo "All content discovery, link extraction, parameter discovery, and fuzzing tool repositories have been cloned."
