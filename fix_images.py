import os
import re

def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # logo-horizontal-advogado
    content = content.replace(
        '<img src="assets/logo-horizontal-advogado.png" alt="LUCAS GOUVEA Advogado" class="logo-img">',
        '<img src="assets/logo-horizontal-advogado-small.png" alt="LUCAS GOUVEA Advogado" class="logo-img" width="120" height="48">'
    )
    content = content.replace(
        '<img src="../../assets/logo-horizontal-advogado.png" alt="LUCAS GOUVEA Advogado" class="logo-img">',
        '<img src="../../assets/logo-horizontal-advogado-small.png" alt="LUCAS GOUVEA Advogado" class="logo-img" width="120" height="48">'
    )

    # logo-stacked
    content = content.replace(
        '<img src="assets/logo-stacked.png" alt="Lucas Gouvea Advogado" class="drawer-logo">',
        '<img src="assets/logo-stacked-small.png" alt="Lucas Gouvea Advogado" class="drawer-logo" width="185" height="50">'
    )
    content = content.replace(
        '<img src="../../assets/logo-stacked.png" alt="Lucas Gouvea Advogado" class="drawer-logo">',
        '<img src="../../assets/logo-stacked-small.png" alt="Lucas Gouvea Advogado" class="drawer-logo" width="185" height="50">'
    )

    # logo-horizontal-light
    content = content.replace(
        '<img src="assets/logo-horizontal-light.png" alt="Lucas Gouvea Advogado" class="footer-logo">',
        '<img src="assets/logo-horizontal-light-small.png" alt="Lucas Gouvea Advogado" class="footer-logo" width="182" height="48">'
    )
    content = content.replace(
        '<img src="../../assets/logo-horizontal-light.png" alt="Lucas Gouvea Advogado" class="footer-logo">',
        '<img src="../../assets/logo-horizontal-light-small.png" alt="Lucas Gouvea Advogado" class="footer-logo" width="182" height="48">'
    )

    with open(filepath, "w") as f:
        f.write(content)

for root, dirs, files in os.walk("."):
    if "node_modules" in root: continue
    for file in files:
        if file.endswith(".html"):
            process_file(os.path.join(root, file))
