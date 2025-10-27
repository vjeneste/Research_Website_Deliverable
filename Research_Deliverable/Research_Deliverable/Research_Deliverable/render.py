from jinja2 import Environment, FileSystemLoader 
env = Environment(loader = FileSystemLoader('templates'))
names = env.list_templates()

print(names)

# Iterates through each file name in templates/
for name in names:
    # Get the jinja template 
    template = env.get_template(name)

    # Opening output file in renders folders, printing the rendered HTML to that file
    with open(f"renders/{name}", 'w') as f:
        print(template.render(), file = f)
