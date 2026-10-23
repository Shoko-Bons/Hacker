import base64
import os
import random
import sys
import time

try:
    import msvcrt
except ImportError:
    msvcrt = None

# TODO: maybe move more of these here later if they get annoying to change
CONFIG = {
    "loan_amount": 50000,
    "loan_repay": 65000.0,
    "pie_chance": 0.0314,  # lol pi joke, don't delete
    "blackmail_cooldown": 600,
    "heat_min": 15,
    "heat_max": 30,
}

def get_files_dir():
    # fix path joining bug from earlier lol
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hackerfiles")
    os.makedirs(path, exist_ok=True)
    return path

def to_hex(name):
    return name.encode().hex()

def from_hex(h):
    try:
        return bytes.fromhex(h).decode()
    except (ValueError, UnicodeDecodeError):
        return "Unknown"

def b64(s):
    return base64.b64encode(s.encode()).decode()

def unb64(s):
    try:
        return base64.b64decode(s.encode()).decode()
    except (ValueError, TypeError):
        return s

def default_player(username, password):
    return {
        "username": username,
        "password": password,
        "balance": 1000.0,
        "pies": 0,
        "hacks_success": 0,
        "hacks_failed": 0,
        "internet": 0,
        "decrypter": 0,
        "vpn": 0,
        "keylogger": 0,
        "crawler": 0,
        "insider": 0,
        "oven": 0,
        "sandevistan": 0,
        "davids_jacket": 0,
        "icebreaker": 0,
        "berserk": 0,
        "cynosure": 0,
        "heat": 0,
        "difficulty": "normal",
        "loan": 0.0,
        "theme": "default",
        "blackmail_time": 0.0,
    }

def save(player):
    path = os.path.join(get_files_dir(), f"{to_hex(player['username'].lower())}.txt")
    with open(path, "w", encoding="utf-8") as f:
        for k, v in player.items():
            if k == "password":
                f.write(f"{k}:{b64(v)}\n") # base64 is basically plaintext btw, whatever
            elif k == "blackmail_time":
                f.write(f"{k}:{b64(str(v))}\n")
            else:
                f.write(f"{k}:{v}\n")

def load(username):
    path = os.path.join(get_files_dir(), f"{to_hex(username.lower())}.txt")
    if not os.path.exists(path):
        return None
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                k, v = line.strip().split(":", 1)
                data[k] = v
    try:
        p = default_player(username, unb64(data.get("password", "")))
        
        # cleaned up the 20 lines into a type map since it was driving me nuts
        type_map = {
            "balance": float,
            "pies": int,
            "hacks_success": int,
            "hacks_failed": int,
            "internet": int,
            "decrypter": int,
            "vpn": int,
            "keylogger": int,
            "crawler": int,
            "insider": int,
            "oven": int,
            "sandevistan": int,
            "davids_jacket": int,
            "icebreaker": int,
            "berserk": int,
            "cynosure": int,
            "heat": int,
            "difficulty": str,
            "loan": float,
            "theme": str,
        }
        
        for key, conv in type_map.items():
            if key in data:
                p[key] = conv(data[key])
                
        if "blackmail_time" in data:
            p["blackmail_time"] = float(unb64(data["blackmail_time"]))
            
        return p
    except (ValueError, TypeError, KeyError):
        return None

def apply_theme(theme):
    if os.name != "nt":
        return
    colors = {"matrix": "0A", "amber": "0E", "cyber": "0B"}
    os.system(f"color {colors.get(theme, '07')}")

def auth():
    print("=" * 50)
    print("          CYBER-CMD: AUTHENTICATION")
    print("=" * 50)
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("\nauth@terminal:~$ ").strip().lower()
        if choice in ("2", "register"):
            username = input("Username: ").strip()
            if not username:
                print("[!] Can't be empty.")
                continue
            if load(username):
                print("[!] Username taken.")
                continue
            password = input("Password: ").strip()
            if not password:
                print("[!] Password required.")
                continue
            p = default_player(username, password)
            save(p)
            print(f"[+] Account '{username}' created.")
            return p
        elif choice in ("1", "login", "log in"):
            username = input("Username: ").strip()
            p = load(username)
            if not p:
                print("[!] User not found.")
                continue
            if input("Password: ").strip() == p["password"]:
                print(f"\n[+] Welcome back, {username}.")
                apply_theme(p["theme"])
                return p
            print("[!] Wrong password.")
        elif choice in ("3", "exit"):
            sys.exit(0)
        else:
            print("Invalid choice.")

def print_banner(p):
    upgrades = []
    if p["internet"]: upgrades.append("Fiber")
    if p["decrypter"]: upgrades.append("Decrypter")
    if p["vpn"]: upgrades.append("VPN")
    if p["keylogger"]: upgrades.append("Keylogger")
    if p["crawler"]: upgrades.append("Crawler")
    if p["insider"]: upgrades.append("Insider")
    if p["oven"]: upgrades.append("Oven")
    if p["sandevistan"]: upgrades.append("Sandevistan")
    if p["davids_jacket"]: upgrades.append("David's Jacket")
    if p["icebreaker"]: upgrades.append("Icebreaker")
    if p["berserk"]: upgrades.append("Berserk")
    if p["cynosure"]: upgrades.append("Cynosure")
    print("=" * 50)
    upg = f" [{', '.join(upgrades)}]" if upgrades else ""
    print(f"  CYBER-CMD V0.1 [{p['username']}]{upg} | {p['difficulty'].upper()}")
    if p["loan"] > 0:
        print(f"  [!] DEBT: ${p['loan']:,.2f}")
    print("=" * 50)
    print("  hack / blackmail / shop / piestore / loan")
    print("  leaderboard / theme  / clear / balance / logout")
    print("-" * 50)

def run_counter_hack():
    if not msvcrt:
        print("[!] Counter-hack skipped (msvcrt not available).")
        return True
    print("\n" + "!" * 50)
    print("INCOMING COUNTER-HACK! Use ARROW KEYS!")
    print("!" * 50)
    arrows = ["UP", "DOWN", "LEFT", "RIGHT"]
    symbols = {"UP": "↑", "DOWN": "↓", "LEFT": "←", "RIGHT": "→"}
    combo = [random.choice(arrows) for _ in range(4)]
    progress = 0
    start = time.time()
    while msvcrt.kbhit():
        msvcrt.getch()
    while time.time() - start < 5.0:
        remaining = round(5.0 - (time.time() - start), 1)
        display = " ".join(
            symbols[a] if i >= progress else f"[{symbols[a]}]"
            for i, a in enumerate(combo)
        )
        sys.stdout.write(f"\r[DEFEND] {display} | {remaining}s ")
        sys.stdout.flush()
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key in (b"\x00", b"\xe0"):
                sc = msvcrt.getch()
                expected = combo[progress]
                hit = (
                    (sc == b"H" and expected == "UP") or
                    (sc == b"P" and expected == "DOWN") or
                    (sc == b"K" and expected == "LEFT") or
                    (sc == b"M" and expected == "RIGHT")
                )
                if hit:
                    progress += 1
                    if progress == 4:
                        print("\n[+] Counter-hack blocked.")
                        return True
                else:
                    print("\n[-] Wrong arrow, reset.")
                    progress = 0
        time.sleep(0.02)
    print("\n[X] You got breached.")
    return False

def run_hack_minigame(p):
    if not msvcrt:
        return random.random() > 0.3  # fallback
    diff = p["difficulty"]
    if diff == "easy":
        speed, leeway, lives = 1.0, 2, 6 if p["internet"] else 4
    elif diff == "hard":
        speed, leeway, lives = 0.5, 999, 4 if p["internet"] else 2
    else:
        speed, leeway, lives = 0.7, 4, 5 if p["internet"] else 3
    lives += 3 if p["sandevistan"] else 0
    print(f"\n[!] Firewall ({diff.upper()}) - 6 chars")
    print("Press ENTER or SPACE to lock.")
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    target = [random.choice(chars) for _ in range(6)]
    locked = ["_"] * 6
    start_idx = 0
    if p["decrypter"]:
        print("[+] Decrypter: first 2 chars solved.")
        locked[0] = target[0]
        locked[1] = target[1]
        start_idx = 2
    print(f"[*] Target: {' '.join(target)}")
    for i in range(start_idx, 6):
        t_char = target[i]
        t_idx = chars.index(t_char)
        while True:
            while msvcrt.kbhit():
                msvcrt.getch()
            roll = random.choice(chars)
            disp = list(locked)
            disp[i] = f"[{roll}]"
            sys.stdout.write(f"\r[LOCKING] {' '.join(disp)} | Lives: {lives}  ")
            sys.stdout.flush()
            t0 = time.time()
            pressed = False
            while time.time() - t0 < speed:
                if msvcrt.kbhit():
                    k = msvcrt.getch()
                    if k in (b"\r", b"\n", b" "):
                        pressed = True
                        break
                time.sleep(0.03)
            if pressed:
                dist = min(abs(t_idx - chars.index(roll)), 36 - abs(t_idx - chars.index(roll)))
                if dist <= leeway:
                    locked[i] = t_char
                    print(f"\n[+] Locked {i+1}/6: [{t_char}]")
                    break
                else:
                    lives -= 1
                    print(f"\n[-] Miss. Needed [{t_char}], got [{roll}]. Lives: {lives}")
                    if lives <= 0:
                        print("\n[X] Lockout.")
                        return False
                    break
    print("\n[+] Firewall bypassed.")
    return True

def show_leaderboard():
    files = [f for f in os.listdir(get_files_dir()) if f.endswith(".txt")]
    if not files:
        print("\n[!] No players yet.")
        return
    ranking = []
    for f in files:
        uname = from_hex(f[:-4])
        bal = pies = succ = fail = 0
        try:
            with open(os.path.join(get_files_dir(), f), encoding="utf-8") as fh:
                for line in fh:
                    if line.startswith("balance:"):
                        bal = float(line.split(":", 1)[1])
                    elif line.startswith("pies:"):
                        pies = int(line.split(":", 1)[1])
                    elif line.startswith("hacks_success:"):
                        succ = int(line.split(":", 1)[1])
                    elif line.startswith("hacks_failed:"):
                        fail = int(line.split(":", 1)[1])
        except (IOError, ValueError, IndexError):
            pass
        ranking.append((uname, bal, pies, succ, fail, bal + pies * 5000))
    ranking.sort(key=lambda x: x[5], reverse=True)
    print("\n" + "=" * 70)
    print(f"{'Rank':<5} {'Name':<14} {'Balance':<14} {'Pies':<6} {'Succ':<6} {'Fail'}")
    print("-" * 70)
    for i, (n, b, pi, s, f, _) in enumerate(ranking, 1):
        print(f"{i:<5} {n:<14} ${b:,.2f}    {pi:<6} {s:<6} {f}")
    print("=" * 70)

def handle_generic_shop(p, title, currency_key, currency_label, items):
    # extracted the duplicated shop logic into a shared helper
    while True:
        print("\n" + "=" * 50)
        print(f"            {title}")
        print("=" * 50)
        if currency_key == "balance":
            print(f" Balance: ${p[currency_key]:,.2f}")
        else:
            print(f" {currency_label}: {p[currency_key]}")
        print("-" * 50)
        
        for num, data in items.items():
            name = data[0]
            cost = data[1]
            key = data[2]
            desc = data[3] if len(data) > 3 else None
            
            status = "[OWNED]" if p[key] else "[AVAILABLE]"
            cost_str = f"${cost:,}" if currency_key == "balance" else f"{cost} {currency_label.lower()}"
            print(f" {num}. {name} ({cost_str})  {status}")
            if desc:
                print(f"    {desc}")
                
        print("-" * 50)
        print(f"buy <1-{len(items)}>  |  exit")
        cmd = input(f"\n{title.lower().replace(' ', '')[:8]}@terminal:~$ ").strip().lower()
        if cmd == "exit":
            break
        num = cmd.replace("buy", "").strip()
        if num not in items:
            print("Unknown.")
            continue
            
        item_data = items[num]
        name, cost, key = item_data[0], item_data[1], item_data[2]
        
        if p[key]:
            print(f"[!] Already own {name}.")
        elif p[currency_key] >= cost:
            if currency_key == "balance":
                p["balance"] = round(p["balance"] - cost, 2)
            else:
                p[currency_key] -= cost
            p[key] = 1
            save(p)
            print(f"[+] Got {name}.")
        else:
            print(f"[!] Need {cost if currency_key != 'balance' else f'${cost:,}'}.")

def run_shop(p):
    items = {
        "1": ("Fiber Optic Internet", 80000, "internet"),
        "2": ("Quantum Auto-Decrypter", 200000, "decrypter"),
        "3": ("VPN Proxy Router", 50000, "vpn"),
        "4": ("Hardware Keylogger", 120000, "keylogger"),
        "5": ("AI Subnet Crawler", 350000, "crawler"),
        "6": ("Corporate Insider Pass", 500000, "insider"),
        "7": ("Master Chef's Oven", 1000000, "oven"),
    }
    handle_generic_shop(p, "BLACK MARKET SHOP", "balance", "Balance", items)

def run_pie_store(p):
    items = {
        "1": ("Sandevistan", 5, "sandevistan", "+3 lives on minigames"),
        "2": ("David's Jacket", 10, "davids_jacket", "Heat never goes above 50%"),
        "3": ("Icebreaker", 15, "icebreaker", "Immune to counter-hacks"),
        "4": ("Berserk OS", 8, "berserk", "50% chance to ignore failure"),
        "5": ("Cynosure Deck", 20, "cynosure", "Auto-win counter-hacks + $10k"),
    }
    handle_generic_shop(p, "PIE BLACK MARKET", "pies", "Pies", items)

def run_loan(p):
    while True:
        print("\n" + "=" * 50)
        print("         DARK WEB LOAN SHARK")
        print("=" * 50)
        print(f" Balance: ${p['balance']:,.2f}")
        print(f" Debt:    ${p['loan']:,.2f}")
        print("-" * 50)
        print(f"borrow  - take ${CONFIG['loan_amount']:,} (owe ${CONFIG['loan_repay']:,.0f})")
        print("pay     - pay full debt")
        print("exit")
        cmd = input("\nloan@terminal:~$ ").strip().lower()
        if cmd == "exit":
            break
        elif cmd == "borrow":
            if p["loan"] > 0:
                print("[!] Already have a loan.")
            else:
                p["balance"] = round(p["balance"] + CONFIG["loan_amount"], 2)
                p["loan"] = CONFIG["loan_repay"]
                save(p)
                print(f"[+] ${CONFIG['loan_amount']:,} added. You now owe ${CONFIG['loan_repay']:,.0f}.")
        elif cmd == "pay":
            if p["loan"] == 0:
                print("[*] No debt.")
            elif p["balance"] >= p["loan"]:
                p["balance"] = round(p["balance"] - p["loan"], 2)
                p["loan"] = 0.0
                save(p)
                print("[+] Debt cleared.")
            else:
                print(f"[!] Need ${p['loan']:,.2f}.")
        else:
            print("Unknown.")

def process_outcome(p, profit, success):
    if success:
        p["hacks_success"] += 1
    else:
        p["hacks_failed"] += 1
        
    if profit > 0:
        if p["keylogger"]:
            profit = round(profit * 1.25, 2)
        if p["insider"]:
            profit = round(profit * 2.0, 2)
            
    p["balance"] = round(p["balance"] + profit, 2)
    
    heat_up = random.randint(CONFIG["heat_min"], CONFIG["heat_max"])
    if p["vpn"]:
        heat_up //= 2
    p["heat"] = min(100, p["heat"] + heat_up)
    
    if p["davids_jacket"] and p["heat"] > 50:
        p["heat"] = 50
        
    # oven baking logic mixed in here because splitting it out felt too neat
    if p["oven"] and random.random() < CONFIG["pie_chance"]:
        p["pies"] += 1
        print("[🥧] Oven baked a pie during the run.")
        
    if p["loan"] > 0:
        p["loan"] = round(p["loan"] * 1.05, 2)
        print(f"[!] Interest applied. Debt now ${p['loan']:,.2f}")
        
    print("-" * 40)
    if str(profit).endswith("3.14") and profit > 0:
        p["pies"] += 1
        print(f"[SUCCESS] +${profit:,.2f} and a pie!")
    elif profit > 0:
        print(f"[SUCCESS] +${profit:,.2f}")
    elif profit < 0:
        print(f"[ALERT] Lost ${abs(profit):,.2f}")
    else:
        print("[NEUTRAL] $0")
        
    print(f"[*] Balance: ${p['balance']:,.2f}  |  Pies: {p['pies']}  |  Heat: {p['heat']}%")
    print("-" * 40)
    save(p)

def main():
    while True:
        p = auth()
        print_banner(p)
        while True:
            try:
                cmd = input(f"\n{p['username']}@terminal:~$ ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                print(f"\nLater, {p['username']}.")
                sys.exit(0)
                
            if cmd in ("exit", "quit"):
                print(f"Disconnecting... {p['username']}")
                sys.exit(0)
            elif cmd == "logout":
                print(f"[+] Logged out {p['username']}")
                break
            elif cmd == "shop":
                run_shop(p)
                print_banner(p)
            elif cmd == "piestore":
                run_pie_store(p)
                print_banner(p)
            elif cmd == "loan":
                run_loan(p)
                print_banner(p)
            elif cmd == "leaderboard":
                show_leaderboard()
            elif cmd == "blackmail":
                amount = round(random.uniform(30000, 60000), 2)
                p["balance"] = round(p["balance"] + amount, 2)
                p["heat"] = 100
                p["blackmail_time"] = time.time()
                save(p)
                print(f"\n[+] Extorted ${amount:,.2f}")
                print("[!] Heat maxed. Can't clear heat for 10 minutes.")
            elif cmd.startswith("theme "):
                theme = cmd[6:].strip()
                if theme in ("matrix", "amber", "cyber", "default"):
                    p["theme"] = theme
                    apply_theme(theme)
                    save(p)
                    print(f"[+] Theme → {theme}")
                else:
                    print("Themes: matrix, amber, cyber, default")
            elif cmd.startswith("diff "):
                d = cmd[5:].strip()
                if d in ("easy", "normal", "hard"):
                    p["difficulty"] = d
                    save(p)
                    print(f"[+] Difficulty → {d}")
                else:
                    print("easy / normal / hard")
            elif cmd == "clear":
                elapsed = time.time() - p["blackmail_time"]
                if elapsed < CONFIG["blackmail_cooldown"]:
                    left = int(CONFIG["blackmail_cooldown"] - elapsed)
                    print(f"[!] Cooldown: {left // 60}m {left % 60}s left")
                elif p["heat"] == 0:
                    print("[*] Heat already 0.")
                elif p["balance"] >= 1000:
                    p["balance"] = round(p["balance"] - 1000, 2)
                    p["heat"] = 0
                    save(p)
                    print("[+] Heat cleared for $1000.")
                else:
                    print("[!] Need $1000.")
            elif cmd == "balance":
                print(f"[*] ${p['balance']:,.2f}  |  Pies: {p['pies']}")
                print(f"[*] Heat: {p['heat']}%  |  Diff: {p['difficulty']}  |  Theme: {p['theme']}")
                print(f"[*] Hacks: {p['hacks_success']} success / {p['hacks_failed']} failed")
                if time.time() - p["blackmail_time"] < CONFIG["blackmail_cooldown"]:
                    left = int(CONFIG["blackmail_cooldown"] - (time.time() - p["blackmail_time"]))
                    print(f"[*] Blackmail lockout: {left // 60}m {left % 60}s")
                if p["loan"] > 0:
                    print(f"[*] Debt: ${p['loan']:,.2f}")
            elif cmd == "help":
                print("\nhack, blackmail, shop, piestore, loan,")
                print("leaderboard, theme , diff ,")
                print("clear, balance, logout, exit")
            elif cmd == "hack":
                risk = p["heat"] / 100
                print(f"[*] Heat {p['heat']}% → {int(risk*100)}% counter-hack chance")
                if random.random() < risk:
                    if p["cynosure"]:
                        print("\n[+] Cynosure wiped the rivals. +$10k")
                        p["balance"] = round(p["balance"] + 10000, 2)
                    elif p["icebreaker"]:
                        print("\n[+] Icebreaker neutralized the attack.")
                    else:
                        if not run_counter_hack():
                            penalty = round(random.uniform(15000, 25000), 2)
                            print(f"[X] Lost ${penalty:,.2f}")
                            process_outcome(p, -penalty, False)
                            continue
                auto = p["crawler"] and random.random() < 0.2
                if auto:
                    print("\n[+] Crawler auto-bypassed the minigame.")
                    success = True
                else:
                    success = run_hack_minigame(p)
                if not success and p["berserk"] and random.random() < 0.5:
                    print("\n[+] Berserk forced the success.")
                    success = True
                if p["difficulty"] == "easy":
                    raw = random.uniform(0, 3000) if success else random.uniform(-3000, 0)
                elif p["difficulty"] == "hard":
                    raw = random.uniform(0, 25000) if success else random.uniform(-25000, 0)
                else:
                    raw = random.uniform(0, 10000) if success else random.uniform(-10000, 0)
                process_outcome(p, round(raw, 2), success)
            else:
                print(f"Unknown: '{cmd}'. Type help.")

if __name__ == "__main__":
    main()
