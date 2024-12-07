import os
import subprocess

# Tools to download
tools = {
    "XSS Injection": [
        "https://github.com/s0md3v/XSStrike",
        "https://github.com/evilcos/xssor2",
        "https://github.com/DanMcInerney/xsscrapy",
        "https://github.com/Netflix-Skunkworks/sleepy-puppy",
        "https://github.com/ssl/ezXSS",
        "https://github.com/mandatoryprogrammer/xsshunter",
        "https://github.com/hahwul/dalfox",
        "https://github.com/epsylon/xsser",
        "https://github.com/hahwul/XSpear",
        "https://github.com/hakluke/weaponised-XSS-payloads",
        "https://github.com/nccgroup/tracy",
        "https://github.com/jobertabma/ground-control",
        "https://github.com/nVisium/xssValidator",
        "https://github.com/Den1al/JSShell",
        "https://github.com/LewisArdern/bXSS",
        "https://github.com/whitel1st/docem",
        "https://github.com/bugbountyforum/XSS-Radar",
        "https://github.com/rajeshmajumdar/BruteXSS",
        "https://github.com/dwisiswant0/findom-xss",
        "https://github.com/fcavallarin/domdig",
        "https://github.com/wish-i-was/femida",
        "https://github.com/SpiderMate/B-XSSRF",
        "https://github.com/yaph/domxssscanner",
        "https://github.com/mandatoryprogrammer/xsshunter_client",
        "https://github.com/Damian89/extended-xss-search",
        "https://github.com/Jewel591/xssmap",
        "https://github.com/menkrep1337/XSSCon",
        "https://github.com/BitTheByte/BitBlinder",
        "https://github.com/dxa4481/XSSOauthPersistence",
        "https://github.com/shadow-workers/shadow-workers",
        "https://github.com/profmoriarity/rexsser",
        "https://github.com/EgeBalci/xss-flare",
        "https://github.com/jiangsir404/Xss-Sql-Fuzz",
        "https://github.com/hipotermia/vaya-ciego-nen",
        "https://github.com/AsaiKen/dom-based-xss-finder",
        "https://github.com/machinexa2/XSSTerminal",
        "https://github.com/vavkamil/xss2png",
        "https://github.com/vavkamil/XSSwagger",
    ],
    "Secrets": [
        "https://github.com/awslabs/git-secrets",
        "https://github.com/zricethezav/gitleaks",
        "https://github.com/dxa4481/truffleHog",
        "https://github.com/hisxo/gitGraber",
        "https://github.com/thoughtworks/talisman",
        "https://github.com/BishopFox/GitGot",
        "https://github.com/anshumanbh/git-all-secrets",
        "https://github.com/gwen001/github-search",
        "https://github.com/cve-search/git-vuln-finder",
        "https://github.com/x1sec/commit-stream",
        "https://github.com/michenriksen/gitrob",
        "https://github.com/auth0/repo-supervisor",
        "https://github.com/UnkL4b/GitMiner",
        "https://github.com/eth0izzle/shhgit",
        "https://github.com/Yelp/detect-secrets",
        "https://github.com/newrelic/rusty-hog",
        "https://github.com/Skyscanner/whispers",
        "https://github.com/nielsing/yar",
        "https://github.com/BishopFox/dufflebag",
        "https://github.com/duo-labs/secret-bridge",
        "https://github.com/americanexpress/earlybird",
        "https://github.com/trufflesecurity/Trufflehog-Chrome-Extension",
        "https://github.com/praetorian-inc/noseyparker"
    ],
    "Git": [
        "https://github.com/internetwache/GitTools",
        "https://github.com/liamg/gitjacker",
        "https://github.com/arthaud/git-dumper",
        "https://github.com/digininja/GitHunter",
        "https://github.com/kost/dvcs-ripper",
        "https://github.com/praetorian-inc/gato",
        "https://github.com/jobertabma/ground-control",
        "https://github.com/GoSecure/dtd-finder",
        "https://github.com/whitel1st/docem",
        "https://github.com/staaldraad/xxeserv",
        "https://github.com/luisfontes19/xxexploiter",
        "https://github.com/BuffaloWill/oxml_xxe",
        "https://github.com/vp777/metahttp",
    ],
    "SSTI Injection": [
        "https://github.com/epinna/tplmap",
        "https://github.com/vladko312/SSTImap"
    ]
}

# Function to run shell commands
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if err:
        print(f"Error: {err.decode()}")

# Create folders and clone repositories
for folder, urls in tools.items():
    os.makedirs(folder, exist_ok=True)
    os.chdir(folder)
    for url in urls:
        run_command(f"git clone {url}")
    os.chdir("..")
