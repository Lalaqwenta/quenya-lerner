from jinja2 import Environment, FileSystemLoader
import os
# Set up Jinja environment and file system loader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('qlerner/main/routes_template')

# Define entities
entities = {'Exercise':["id", "question", "answer", "type", "hint"], 
    'Lesson':["id", "title", "exercise_ids"], 
    'User':["role", "username", "email", "password"],
    'Word':["id", "english_meaning", "english_translation", "quenya_tengwar", "quenya_transcription"]}

for entity in entities:
    # Generate code from template
    code = template.render(entity_name=entity, columns=entities[entity])

    # Write code to file in the same directory as the template
    with open(os.path.join('qlerner/main/', f'{entity.lower()}_routes.py'), 'w') as f:
        f.write(code)
