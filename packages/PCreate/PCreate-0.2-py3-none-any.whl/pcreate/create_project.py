import os
import subprocess
import sys


def create_project(project_name):
    project_dir = os.path.join(os.getcwd(), project_name)

    if os.path.exists(project_dir):
        print(f"Error: Project '{project_name}' already exists.")
        sys.exit(1)

    os.makedirs(project_dir, exist_ok=True)

    venv_dir = os.path.join(project_dir, 'venv')

    print("Creating virtual environment...")

    subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])

    main_py_path = os.path.join(project_dir, 'main.py')
    with open(main_py_path, 'w') as f:
        f.write('def main():\n')
        f.write('    print("Hello, World!")\n\n')
        f.write('if __name__ == "__main__":\n')
        f.write('    main()\n')

    gitignore_path = os.path.join(project_dir, '.gitignore')
    with open(gitignore_path, 'w') as f:
        f.write('venv/\n')
        f.write('__pycache__/\n')
        f.write('.DS_Store\n')
        f.write('*.pyc\n')
        f.write('.env\n')
        f.write('.idea\n')
        f.write('.vscode\n')

    print(f"Project '{project_name}' created successfully.")
    print(f"Virtual environment created at '{venv_dir}'.")
    print(f"'main.py' created at '{main_py_path}'.")
    print(f"'.gitignore' created at '{gitignore_path}'")

    if os.name == 'nt':
        activate_command = "venv/Scripts/activate"
    else:
        activate_command = "source venv/bin/activate"

    print("\nTo activate the virtual environment, run the following commands:")
    print("cd", project_name)
    print(activate_command)


def main():
    if len(sys.argv) != 2:
        print("Usage: pcreate <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    create_project(project_name)


if __name__ == "__main__":
    main()
