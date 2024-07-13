import os
import subprocess
import sys


def create_project(project_name):
    project_dir = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_dir, exist_ok=True)

    venv_dir = os.path.join(project_dir, 'venv')
    subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])

    main_py_path = os.path.join(project_dir, 'main.py')
    with open(main_py_path, 'w') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('def main():\n')
        f.write('    print("Hello, World!")\n\n')
        f.write('if __name__ == "__main__":\n')
        f.write('    main()\n')

    print(f"Project '{project_name}' created successfully.")
    print(f"Virtual environment created at '{venv_dir}'.")
    print(f"'main.py' created at '{main_py_path}'.")


def main():
    if len(sys.argv) != 2:
        print("Usage: pcreate <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    create_project(project_name)


if __name__ == "__main__":
    main()
