import importlib


def check_dependency(name: str, description: str) -> bool:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {description}")
        return True
    except ImportError:
        print(f"[MISSING] {name}")
        print(f"  pip: pip install {name}")
        print(f"  Poetry: poetry add {name}")
        return False


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    all_present = True

    dependencies = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
    }
    for name, description in dependencies.items():
        if not check_dependency(name, description):
            all_present = False

    print()
    print("pip vs Poetry:")
    print(
        "requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "pyproject.toml declares the same constraints, and Poetry "
        "pins the resolved versions in poetry.lock so every install "
        "is identical."
    )

    if all_present:
        print()
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
