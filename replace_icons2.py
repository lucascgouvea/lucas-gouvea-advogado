import os
import re
import urllib.request

svg_cache = {}

def get_svg(icon_name):
    if icon_name in svg_cache:
        return svg_cache[icon_name]
    try:
        url = f"https://unpkg.com/lucide-static@latest/icons/{icon_name}.svg"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            svg = response.read().decode('utf-8')
            svg_cache[icon_name] = svg
            return svg
    except Exception as e:
        print(f"Error fetching {icon_name}: {e}")
        return None

def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    pattern = r'<i([^>]*)data-lucide="([^"]+)"([^>]*)>(.*?)</i>'
    
    def repl(match):
        before_attrs = match.group(1)
        icon_name = match.group(2)
        after_attrs = match.group(3)
        
        svg = get_svg(icon_name)
        if not svg:
            print(f"Icon {icon_name} not found!")
            return match.group(0)
            
        all_attrs = before_attrs + " " + after_attrs
        class_match = re.search(r'class="([^"]+)"', all_attrs)
        
        extra_classes = class_match.group(1) if class_match else ""
        
        if extra_classes:
            svg = svg.replace('class="', f'class="{extra_classes} ', 1)
            
        return svg

    new_content = re.sub(pattern, repl, content)
    
    script_pattern1 = r'<script src="https://unpkg\.com/lucide@latest"></script>\s*'
    script_pattern2 = r'<script>\s*lucide\.createIcons\(\);\s*</script>\s*'
    new_content = re.sub(script_pattern1, "", new_content)
    new_content = re.sub(script_pattern2, "", new_content)

    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk("."):
    if "node_modules" in root: continue
    for file in files:
        if file.endswith(".html"):
            process_file(os.path.join(root, file))
