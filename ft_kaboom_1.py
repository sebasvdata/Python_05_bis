
if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    import alchemy.grimoire.dark_spellbook
    spellbook = alchemy.grimoire.dark_spellbook
    record = spellbook.dark_spell_record("Force", "Bats and wind")
    print(f"Testing dark_spell: {record}")
