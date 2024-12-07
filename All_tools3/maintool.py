import os
import subprocess

# Dictionary containing sections and their associated GitHub repos
tools = {
    "Command Injection": [
        "https://github.com/commixproject/commix"
    ],
    "CORS Misconfiguration": [
        "https://github.com/s0md3v/Corsy",
        "https://github.com/RUB-NDS/CORStest",
        "https://github.com/laconicwolf/cors-scanner",
        "https://github.com/Shivangx01b/CorsMe"
    ],
    "CRLF Injection": [
        "https://github.com/Nefcore/CRLFsuite",
        "https://github.com/dwisiswant0/crlfuzz",
        "https://github.com/MichaelStott/CRLF-Injection-Scanner",
        "https://github.com/BountyStrike/Injectus"
    ],
    "CSRF Injection": [
        "https://github.com/0xInfection/XSRFProbe"
    ],
    "Directory Traversal": [
        "https://github.com/wireghoul/dotdotpwn",
        "https://github.com/chrispetrou/FDsploit",
        "https://github.com/bayotop/off-by-slash",
        "https://github.com/momenbasel/liffier"
    ],
    "File Inclusion": [
        "https://github.com/mzfr/liffy",
        "https://github.com/Team-Firebugs/Burp-LFI-tests",
        "https://github.com/mthbernardes/LFI-Enum",
        "https://github.com/D35m0nd142/LFISuite",
        "https://github.com/hussein98d/LFI-files"
    ],
    "GraphQL Injection": [
        "https://github.com/doyensec/inql",
        "https://github.com/swisskyrepo/GraphQLmap",
        "https://github.com/szski/shapeshifter",
        "https://github.com/zidekmat/graphql_beautifier",
        "https://github.com/nikitastupin/clairvoyance"
    ],
    "Header Injection": [
        "https://github.com/mlcsec/headi"
    ],
    "SQL Injection": [
        "https://github.com/sqlmapproject/sqlmap",
        "https://github.com/codingo/NoSQLMap",
        "https://github.com/0xbug/SQLiScanner",
        "https://github.com/RhinoSecurityLabs/SleuthQL",
        "https://github.com/blackarrowsec/mssqlproxy",
        "https://github.com/zt2/sqli-hunter",
        "https://github.com/ghostlulzhacks/waybackSqliScanner",
        "https://github.com/NetSPI/ESC",
        "https://github.com/Keramas/mssqli-duet",
        "https://github.com/Miladkhoshdel/burp-to-sqlmap",
        "https://github.com/InitRoot/BurpSQLTruncSanner",
        "https://github.com/sadicann/andor",
        "https://github.com/mhaskar/Blinder",
        "https://github.com/the-robot/sqliv",
        "https://github.com/Charlie-belmer/nosqli",
        "https://github.com/r0oth3x49/ghauri",
        "https://github.com/frohoff/ysoserial",
        "https://github.com/BishopFox/GadgetProbe",
        "https://github.com/pwntester/ysoserial.net",
        "https://github.com/ambionics/phpggc"
    ],
    "Insecure Direct Object References": [
        "https://github.com/Quitten/Autorize"
    ],
    "Open Redirect": [
        "https://github.com/r0075h3ll/Oralyzer",
        "https://github.com/BountyStrike/Injectus",
        "https://github.com/Naategh/dom-red",
        "https://github.com/devanshbatham/OpenRedireX"
    ],
    "Race Condition": [
        "https://github.com/compsec-snu/razzer",
        "https://github.com/racepwn/racepwn",
        "https://github.com/nccgroup/requests-racer",
        "https://github.com/PortSwigger/turbo-intruder",
        "https://github.com/TheHackerDev/race-the-web"
    ],
    "Request Smuggling": [
        "https://github.com/anshumanpattnaik/http-request-smuggling",
        "https://github.com/defparam/smuggler",
        "https://github.com/BishopFox/h2csmuggler",
        "https://github.com/defparam/tiscripts"
    ]
}

# Function to clone GitHub repos into a directory
def clone_repo(repo_url, folder):
    try:
        subprocess.run(["git", "clone", repo_url, folder], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning {repo_url}: {e}")

# Create folders and clone repositories
for section, repos in tools.items():
    # Create section directory if it doesn't exist
    if not os.path.exists(section):
        os.makedirs(section)
    
    for repo in repos:
        folder_name = repo.split('/')[-1]  # Extract folder name from repo URL
        target_folder = os.path.join(section, folder_name)
        clone_repo(repo, target_folder)

print("All tools have been downloaded and organized.")
