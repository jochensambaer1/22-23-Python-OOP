import os
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

directory = "my_directory"
templates_path = "templates"

# Initialize Jinja environment
env = Environment(loader=FileSystemLoader(templates_path))

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        # Parse front matter and content
        with open(os.path.join(directory, filename), "r") as f:
            content = f.read()
            _, front_matter, text = content.split("---")
            data = yaml.safe_load(front_matter.strip())
            html = markdown.markdown(text.strip())

        # Render template with data and content
        template = env.get_template("my_template.html")
        output = template.render(data=data, content=html)

        # Write output to file
        with open(os.path.join(directory, filename.replace(".md", ".html")), "w") as f:
            f.write(output)
