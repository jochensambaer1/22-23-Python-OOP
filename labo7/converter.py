import os
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

# Define paths
pages_path = "pages"
posts_path = "posts"
templates_path = "templates"
site_path = "_site"

# Create site directory if it doesn't exist
if not os.path.exists(site_path):
    os.makedirs(site_path)

# Initialize Jinja environment
env = Environment(loader=FileSystemLoader(templates_path))

# Loop through pages
for filename in os.listdir(pages_path):
    # Only process Markdown files
    if filename.endswith(".md"):
        # Parse front matter and content
        with open(os.path.join(pages_path, filename), "r") as f:
            content = f.read()
            _, front_matter, text = content.split("---")
            data = yaml.safe_load(front_matter.strip())
            html = markdown.markdown(text.strip())

        # Render template with data and content
        template = env.get_template("page.html")
        output = template.render(data=data, content=html)

        # Write output to file
        with open(os.path.join(site_path, filename.replace(".md", ".html")), "w") as f:
            f.write(output)

# Loop through posts
for filename in os.listdir(posts_path):
    # Only process Markdown files
    if filename.endswith(".md"):
        # Parse front matter and content
        with open(os.path.join(posts_path, filename), "r") as f:
            content = f.read()
            _, front_matter, text = content.split("---")
            data = yaml.safe_load(front_matter.strip())
            html = markdown.markdown(text.strip())

        # Render template with data and content
        template = env.get_template("post.html")
        output = template.render(data=data, content=html)

        # Write output to file
        with open(os.path.join(site_path, "posts", filename.replace(".md", ".html")), "w") as f:
            f.write(output)
