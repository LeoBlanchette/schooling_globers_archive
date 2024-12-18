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
        title = row['Title'] if row['Title'] else '[Untitled]'
        url = row['URL']
        links.append(f"- **Episode {episode_number} - {title}** {url}")

# Read the contributing content from 2_CONTRIBUTING.md
with open('readme_parts/2_contributing.md', 'r') as contributing_file:
    contributing_content = contributing_file.read()

# Write the content to README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(intro_content)
    readme_file.write('\n\n## Schooling Globers, Complete YouTube List\n\n')
    for link in links:
        readme_file.write(f"{link}\n")
    readme_file.write('\n\n')
    readme_file.write(contributing_content)