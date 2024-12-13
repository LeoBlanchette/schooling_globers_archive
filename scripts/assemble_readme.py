import csv

# Read the intro content from 0_intro.md
with open('readme_parts/0_intro.md', 'r') as intro_file:
    intro_content = intro_file.read()

# Read the link list from linklist.csv
with open('linklist.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    links = []
    for row in csv_reader:
        episode_number = row['Episode Number']
        title = row['Title'] if row['Title'] else 'Untitled'
        url = row['URL']
        links.append(f"{episode_number}: **Episode {episode_number} - {title}** {url}")

# Write the content to README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(intro_content)
    readme_file.write('\n\n## Schooling Globers, Complete YouTube List\n\n')
    for link in links:
        readme_file.write(f"1. {link}\n")