import subprocess
import json

# Step 1: Export dependencies
with open("requirements.txt", "w") as f:
    subprocess.run(["pip", "freeze"], stdout=f)

# Step 2: Run Safety scan
print("Running security scan with Safety...")
subprocess.run(["safety", "check", "--file=requirements.txt", "--full-report"])

# Step 3: Generate SBOM (JSON)
with open("requirements.txt") as f:
    packages = f.read().splitlines()

sbom = {"packages": packages}

with open("sbom.json", "w") as f:
    json.dump(sbom, f, indent=4)

print("SBOM generated: sbom.json")