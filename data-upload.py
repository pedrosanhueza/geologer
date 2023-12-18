
import subprocess

def upload_to_github(repository_path, file_path, commit_message):
    # Change to the repository directory
    subprocess.run(["cd", repository_path], shell=True)

    # Add the file to the staging area
    subprocess.run(["git", "add", file_path])

    # Commit the changes
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push the changes to GitHub
    subprocess.run(["git", "push"])
    
repository_path = "https://github.com/pedrosanhueza/geologer"

file_path = "C:/Users/pedro/Documents/Scripts/Geologger/geologer/Sierra_Gorda - editado5.csv"

commit_message = "Upload CSV file updated"

upload_to_github(repository_path, file_path, commit_message)