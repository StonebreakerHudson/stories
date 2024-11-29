import os
import shutil

# Define the source directory (your current folder structure)
SOURCE_DIR = "./"  # Adjust to your path if needed
TARGET_DIR = "./github-pages-repo"

def copy_folder_structure(source, target):
    """
    Recursively copy the folder structure and files while organizing for GitHub Pages.
    """
    for root, dirs, files in os.walk(source):
        # Get relative path to preserve structure
        rel_path = os.path.relpath(root, source)
        target_path = os.path.join(target, rel_path)

        if not os.path.exists(target_path):
            os.makedirs(target_path)

        # Copy files to the new structure
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(target_path, file)
            shutil.copy2(src_file, dest_file)

            # Rename index.html files for better routing
            if file == "index.html" and rel_path != ".":
                new_dest = os.path.join(target_path, "index.html")
                os.rename(dest_file, new_dest)

def create_root_index(target, languages):
    """
    Create a root-level index.html file with links to language-specific pages.
    """
    index_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project Home</title>
    </head>
    <body>
        <h1>Welcome to the Project</h1>
        <p>Select a language to continue:</p>
        <ul>
    """
    for lang in languages:
        index_content += f'            <li><a href="{lang}/index.html">{lang.upper()}</a></li>\n'
    index_content += """
        </ul>
    </body>
    </html>
    """
    with open(os.path.join(target, "index.html"), "w") as f:
        f.write(index_content)

def organize_for_github_pages():
    """
    Main function to organize the folder structure for GitHub Pages.
    """
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    os.makedirs(TARGET_DIR)

    # Copy source structure into the target folder
    copy_folder_structure(SOURCE_DIR, TARGET_DIR)

    # Create a root index.html
    languages = ["de", "en"]  # Add other languages as needed
    create_root_index(TARGET_DIR, languages)

    print(f"GitHub Pages repository structure created at: {TARGET_DIR}")

if __name__ == "__main__":
    organize_for_github_pages()

