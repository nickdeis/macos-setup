import subprocess


def start_install(name: str, cmd: str):
    print(f"Installing {name}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("Success")
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with status {e.returncode}")
    print(f"Finished Installing {name}")


start_install(
    "Oh my ZSH",
    [
        "sh",
        "-c",
        "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)",
    ],
)
start_install(
    "Brew",
    [
        "/bin/bash",
        "-c",
        "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)",
    ],
)
start_install(
    "NVM",
    "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash",
)
start_install("Node 24", "nvm install 24 && nvm alias default 24")
start_install("Git, DuckDB, and Podman", "brew install git duckdb podman")
start_install("Bun", "npm install -g bun", shell=True)
start_install("VSCode", "brew install --cask visual-studio-code")
start_install("PGAdmin", "brew install --cask pgadmin4")
