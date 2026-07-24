import argparse
import os
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
ENV_FILE = PROJECT_DIR / ".env"


def load_env_file(path):
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def require_setting(name):
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"Missing {name}. Add it to .env first.")
    return value


def build_parser():
    parser = argparse.ArgumentParser(
        description="Simple Instagram bot that follows one target account."
    )
    parser.add_argument(
        "--target",
        default=os.getenv("IG_TARGET", "").strip(),
        help="Instagram username to follow. Defaults to IG_TARGET from .env.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check settings without logging in or following anyone.",
    )
    return parser


def main():
    load_env_file(ENV_FILE)
    args = build_parser().parse_args()

    username = require_setting("IG_USERNAME")
    password = require_setting("IG_PASSWORD")
    target = (args.target or "").strip().lstrip("@")

    if not target:
        raise ValueError("Missing target username. Add IG_TARGET to .env or use --target.")

    if args.dry_run:
        print(f"Ready to log in as @{username} and follow @{target}.")
        return

    from instabot import Bot

    bot = Bot()
    try:
        if not bot.login(username=username, password=password):
            raise RuntimeError("Instagram login failed. Check your credentials or challenge status.")

        bot.follow(target)
        print(f"Follow request completed for @{target}.")
    finally:
        try:
            bot.logout()
        except Exception:
            pass


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)
