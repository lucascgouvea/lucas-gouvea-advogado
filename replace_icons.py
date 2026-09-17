import os
import re

def get_svg(icon_name):
    svg_path = f"node_modules/lucide-static/icons/{icon_name}.svg"
    if not os.path.exists(svg_path):
        return None
    with open(svg_path, "r") as f:
        return f.read()

def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # Find all <i ... data-lucide="name" ...></i>
    # The regex needs to capture the whole tag and extract data-lucide and class
    pattern = r'<i([^>]*)data-lucide="([^"]+)"([^>]*)>(.*?)</i>'
    
    def repl(match):
        before_attrs = match.group(1)
        icon_name = match.group(2)
        after_attrs = match.group(3)
        
        svg = get_svg(icon_name)
        if not svg:
            print(f"Icon {icon_name} not found!")
            return match.group(0) # don't replace
            
        # extract classes if any
        all_attrs = before_attrs + " " + after_attrs
        class_match = re.search(r'class="([^"]+)"', all_attrs)
        
        extra_classes = class_match.group(1) if class_match else ""
        
        # The lucide SVG comes as <svg xmlns=... class="lucide lucide-iconname" ...>
        # We need to insert the extra classes into the class attribute
        if extra_classes:
            svg = svg.replace('class="', f'class="{extra_classes} ', 1)
            
        return svg

    new_content = re.sub(pattern, repl, content)
    
    # Remove the lucide script tags
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
