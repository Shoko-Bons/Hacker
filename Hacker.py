import base64
import os
import random
import sys
import time

try:
  import msvcrt
except ImportError:
  pass


def get_files_directory():
  """Returns the path to the 'hackerfiles' directory inside the script's folder.

  Creates the directory if it doesn't already exist.
  """
  script_dir = os.path.dirname(os.path.abspath(__file__))
  files_dir = os.path.join(script_dir, "hackerfiles")

  if not os.path.exists(files_dir):
    os.makedirs(files_dir)

  return files_dir


def username_to_hex(username):
  """Converts a username string into hexadecimal format."""
  return username.encode("utf-8").hex()


def hex_to_username(hex_str):
  """Converts a hexadecimal string back to a normal username string."""
  try:
    return bytes.fromhex(hex_str).decode("utf-8")
  except ValueError:
    return "Unknown"


def encrypt_data(data_str):
  """Encrypts a string into base64 format."""
  return base64.b64encode(data_str.encode("utf-8")).decode("utf-8")


def decrypt_data(encoded_str):
  """Decrypts a base64 string back to plain text."""
  try:
    return base64.b64decode(encoded_str.encode("utf-8")).decode("utf-8")
  except Exception:
    return encoded_str


def save_user_data(
    username,
    password,
    balance,
    pies,
    hacks_success,
    hacks_failed,
    internet,
    decrypter,
    vpn,
    keylogger,
    crawler,
    insider,
    oven,
    sandevistan,
    davids_jacket,
    icebreaker,
    berserk,
    cynosure,
    heat,
    difficulty,
    loan,
    theme,
    blackmail_time,
):
  """Saves/updates all user data into their hex-named .txt file."""
  files_dir = get_files_directory()
  hex_filename = f"{username_to_hex(username.lower())}.txt"
  file_path = os.path.join(files_dir, hex_filename)

  encrypted_pwd = encrypt_data(password)
  encrypted_blackmail = encrypt_data(str(blackmail_time))

  with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"username:{username}\n")
    f.write(f"password:{encrypted_pwd}\n")
    f.write(f"balance:{balance:.2f}\n")
    f.write(f"pies:{pies}\n")
    f.write(f"hacks_success:{hacks_success}\n")
    f.write(f"hacks_failed:{hacks_failed}\n")
    f.write(f"internet:{internet}\n")
    f.write(f"decrypter:{decrypter}\n")
    f.write(f"vpn:{vpn}\n")
    f.write(f"keylogger:{keylogger}\n")
    f.write(f"crawler:{crawler}\n")
    f.write(f"insider:{insider}\n")
    f.write(f"oven:{oven}\n")
    f.write(f"sandevistan:{sandevistan}\n")
    f.write(f"davids_jacket:{davids_jacket}\n")
    f.write(f"icebreaker:{icebreaker}\n")
    f.write(f"berserk:{berserk}\n")
    f.write(f"cynosure:{cynosure}\n")
    f.write(f"heat:{heat}\n")
    f.write(f"difficulty:{difficulty}\n")
    f.write(f"loan:{loan:.2f}\n")
    f.write(f"theme:{theme}\n")
    f.write(f"blackmail_time:{encrypted_blackmail}\n")


def load_user_data(username):
  """Loads user data from their hex-named file."""
  files_dir = get_files_directory()
  hex_filename = f"{username_to_hex(username.lower())}.txt"
  file_path = os.path.join(files_dir, hex_filename)

  if not os.path.exists(file_path):
    return None

  data = {}
  with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
      if ":" in line:
        key, val = line.strip().split(":", 1)
        data[key] = val

  raw_pwd = data.get("password", "")
  actual_pwd = decrypt_data(raw_pwd)

  raw_blackmail = data.get("blackmail_time", "0.0")
  actual_blackmail = float(decrypt_data(raw_blackmail))

  try:
    return (
        actual_pwd,
        float(data.get("balance", 1000.00)),
        int(data.get("pies", 0)),
        int(data.get("hacks_success", 0)),
        int(data.get("hacks_failed", 0)),
        int(data.get("internet", 0)),
        int(data.get("decrypter", 0)),
        int(data.get("vpn", 0)),
        int(data.get("keylogger", 0)),
        int(data.get("crawler", 0)),
        int(data.get("insider", 0)),
        int(data.get("oven", 0)),
        int(data.get("sandevistan", 0)),
        int(data.get("davids_jacket", 0)),
        int(data.get("icebreaker", 0)),
        int(data.get("berserk", 0)),
        int(data.get("cynosure", 0)),
        int(data.get("heat", 0)),
        data.get("difficulty", "normal"),
        float(data.get("loan", 0.00)),
        data.get("theme", "default"),
        actual_blackmail,
    )
  except ValueError:
    return None


def apply_theme(theme_name):
  """Applies CMD color schemes using Windows color codes."""
  if os.name == "nt":
    if theme_name == "matrix":
      os.system("color 0A")
    elif theme_name == "amber":
      os.system("color 0E")
    elif theme_name == "cyber":
      os.system("color 0B")
    else:
      os.system("color 07")


def auth_screen():
  """Handles initial Login or Registration prompt."""
  print("=" * 50)
  print("          CYBER-CMD: AUTHENTICATION           ")
  print("=" * 50)

  while True:
    print("\nSelect an option:")
    print(" 1. Login ('log in' or '1')")
    print(" 2. Register ('register' or '2')")
    print(" 3. Exit ('exit')")

    choice = input("\nauth@terminal:~$ ").strip().lower()

    if choice in ["register", "2"]:
      print("\n--- ACCOUNT REGISTRATION ---")
      while True:
        username = input("Enter new username: ").strip()
        if not username:
          print("[!] Username cannot be empty.")
          continue

        hex_filename = f"{username_to_hex(username.lower())}.txt"
        file_path = os.path.join(get_files_directory(), hex_filename)
        if os.path.exists(file_path):
          print("[!] Username already exists! Try logging in or pick another.")
          break

        password = input("Enter password: ").strip()
        if not password:
          print("[!] Password cannot be empty.")
          continue

        save_user_data(
            username=username,
            password=password,
            balance=1000.00,
            pies=0,
            hacks_success=0,
            hacks_failed=0,
            internet=0,
            decrypter=0,
            vpn=0,
            keylogger=0,
            crawler=0,
            insider=0,
            oven=0,
            sandevistan=0,
            davids_jacket=0,
            icebreaker=0,
            berserk=0,
            cynosure=0,
            heat=0,
            difficulty="normal",
            loan=0.00,
            theme="default",
            blackmail_time=0.0,
        )

        print(
            f"[+] Account '{username}' created successfully! Password encrypted"
            " securely."
        )
        return load_user_data(username) + (username,)

    elif choice in ["log in", "login", "1"]:
      print("\n--- ACCOUNT LOGIN ---")
      username = input("Enter username: ").strip()
      user_data = load_user_data(username)

      if user_data is None:
        print("[!] Username not found. Please register first.")
        continue

      saved_password = user_data[0]
      password = input("Enter password: ").strip()

      if password == saved_password:
        print(f"\n[+] Welcome back, Netrunner {username}!")
        apply_theme(user_data[20])
        return user_data + (username,)
      else:
        print("[!] Incorrect password.")

    elif choice in ["exit", "3"]:
      print("Disconnecting...")
      sys.exit(0)
    else:
      print("Invalid choice. Please choose 'log in', 'register', or 'exit'.")


def print_banner(
    username,
    internet,
    decrypter,
    vpn,
    keylogger,
    crawler,
    insider,
    oven,
    sandevistan,
    davids_jacket,
    icebreaker,
    berserk,
    cynosure,
    difficulty,
    loan,
):
  print("=" * 50)
  upgrades = []
  if internet == 1:
    upgrades.append("Fiber")
  if decrypter == 1:
    upgrades.append("Decrypter")
  if vpn == 1:
    upgrades.append("VPN")
  if keylogger == 1:
    upgrades.append("Keylogger")
  if crawler == 1:
    upgrades.append("Crawler")
  if insider == 1:
    upgrades.append("Insider Pass")
  if oven == 1:
    upgrades.append("Oven")
  if sandevistan == 1:
    upgrades.append("Sandevistan")
  if davids_jacket == 1:
    upgrades.append("David's Jacket")
  if icebreaker == 1:
    upgrades.append("Icebreaker")
  if berserk == 1:
    upgrades.append("Berserk OS")
  if cynosure == 1:
    upgrades.append("Cynosure Deck")
  upg_str = f" [{', '.join(upgrades)}]" if upgrades else ""

  print(
      f"     CYBER-CMD: TERMINAL HACKING V0.1 [{username}]{upg_str} | Diff:"
      f" {difficulty.upper()}"
  )
  if loan > 0:
    print(f" [!] LOAN SHARK DEBT OWED: ${loan:,.2f}")
  print("=" * 50)
  print(" Type 'hack'         - Infiltrate network.")
  print(" Type 'blackmail'    - Extort corp (10-min Heat Clear lock!).")
  print(" Type 'shop'         - Buy cash upgrades.")
  print(" Type 'piestore'     - Spend pies on legendary OP gear.")
  print(" Type 'loan'         - Visit Dark Web Loan Shark.")
  print(" Type 'leaderboard'  - View netrunner rankings.")
  print(" Type 'theme <color>'- Switch color theme (matrix, amber, cyber, default)")
  print(" Type 'clear'        - Pay $1,000 bribe to clear Police Heat.")
  print(" Type 'balance'      - View status, funds & heat.")
  print(" Type 'logout'       - Return to main menu.")
  print("-" * 50)


def run_counter_hack():
  """Helldivers-style stratagem arrow sequence defense minigame."""
  print("\n" + "!" * 50)
  print("🚨 INCOMING COUNTER-HACK FROM RIVAL HACKERS! DEFEND YOUR NODE! 🚨")
  print("Input the arrow sequence using your ARROW KEYS to fight them off!")
  print("!" * 50)

  arrows = ["UP", "DOWN", "LEFT", "RIGHT"]
  arrow_symbols = {"UP": "↑", "DOWN": "↓", "LEFT": "←", "RIGHT": "→"}

  target_combo = [random.choice(arrows) for _ in range(4)]
  input_progress = 0
  time_limit = 5.0
  start_time = time.time()

  while msvcrt.kbhit():
    msvcrt.getch()

  while time.time() - start_time < time_limit:
    remaining_time = round(time_limit - (time.time() - start_time), 1)
    display_combo = " ".join(
        [
            arrow_symbols[a] if i >= input_progress else f"[{arrow_symbols[a]}]"
            for i, a in enumerate(target_combo)
        ]
    )

    sys.stdout.write(
        f"\r[DEFEND] Combo: {display_combo} | Time: {remaining_time}s "
    )
    sys.stdout.flush()

    if msvcrt.kbhit():
      key = msvcrt.getch()
      if key in [b"\x00", b"\xe0"]:
        scancode = msvcrt.getch()
        expected = target_combo[input_progress]

        matched = False
        if scancode == b"H" and expected == "UP":
          matched = True
        elif scancode == b"P" and expected == "DOWN":
          matched = True
        elif scancode == b"K" and expected == "LEFT":
          matched = True
        elif scancode == b"M" and expected == "RIGHT":
          matched = True

        if matched:
          input_progress += 1
          if input_progress == len(target_combo):
            print("\n[+] COUNTER-HACK REPELLED! Rival hackers blocked.")
            return True
        else:
          print("\n[-] WRONG ARROW! Sequence reset!")
          input_progress = 0

    time.sleep(0.02)

  print(
      "\n[X] DEFENSE FAILED: Rival hackers breached you! (-$15,000 to -$25,000)"
  )
  return False


def run_hack_minigame(internet, decrypter, sandevistan, difficulty):
  """Runs the rolling lock minigame with accurate range checking."""
  if difficulty == "easy":
    tick_speed = 1.0
    leeway = 2
    base_lives = 6 if internet == 1 else 4
  elif difficulty == "hard":
    tick_speed = 0.5
    leeway = 999
    base_lives = 4 if internet == 1 else 2
  else:  # normal
    tick_speed = 0.7
    leeway = 4
    base_lives = 5 if internet == 1 else 3

  lives = base_lives + (3 if sandevistan == 1 else 0)

  print(
      f"\n[!] TARGET FIREWALL ({difficulty.upper()}): Bypass sequence required"
      " (6 chars)"
  )
  print("[!] Press [ENTER] or [SPACEBAR] to lock in each character.")

  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  target_sequence = [random.choice(chars) for _ in range(6)]
  locked_sequence = ["_"] * 6

  start_index = 0
  if decrypter == 1:
    print(
        "[+] QUANTUM AUTO-DECRYPTER ACTIVE: First 2 characters bypass-solved!"
    )
    locked_sequence[0] = target_sequence[0]
    locked_sequence[1] = target_sequence[1]
    start_index = 2

  print(f"[*] TARGET SEQUENCE: {' '.join(target_sequence)}")

  for i in range(start_index, 6):
    target_char = target_sequence[i]
    target_idx = chars.index(target_char)

    while True:
      while msvcrt.kbhit():
        msvcrt.getch()

      current_roll = random.choice(chars)

      display_list = list(locked_sequence)
      display_list[i] = f"[{current_roll}]"
      current_display = " ".join(display_list)

      sys.stdout.write(
          f"\r[LOCKING] {current_display} | Lives Left: {lives}  "
      )
      sys.stdout.flush()

      start_time = time.time()
      keyed = False

      while time.time() - start_time < tick_speed:
        if msvcrt.kbhit():
          key = msvcrt.getch()
          if key in [b"\r", b"\n", b" "]:
            keyed = True
            break
        time.sleep(0.03)

      if keyed:
        roll_idx = chars.index(current_roll)
        distance = min(
            abs(target_idx - roll_idx),
            len(chars) - abs(target_idx - roll_idx),
        )

        if distance <= leeway:
          locked_sequence[i] = target_char
          print(f"\n[+] Character {i+1}/6 Locked: [{target_char}]")
          break
        else:
          lives -= 1
          print(
              f"\n[-] MISMATCH! Target was [{target_char}], rolled"
              f" [{current_roll}]. Lives left: {lives}"
          )
          if lives <= 0:
            print("\n[X] SECURITY LOCKOUT! Intrusion detected.")
            return False
          break

  print("\n[+] SEQUENCE ACCEPTED: Firewall successfully bypassed!")
  return True


def show_leaderboard():
  """Scans hackerfiles folder and displays top netrunners ranked by net worth and hacks."""
  files_dir = get_files_directory()
  files = [f for f in os.listdir(files_dir) if f.endswith(".txt")]

  if not files:
    print("\n[!] No netrunner files found in database.")
    return

  rankings = []
  for filename in files:
    hex_name = filename[:-4]
    uname = hex_to_username(hex_name)
    file_path = os.path.join(files_dir, filename)

    bal, pie_count, h_succ, h_fail = 1000.00, 0, 0, 0
    try:
      with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
          if line.startswith("balance:"):
            bal = float(line.strip().split(":", 1)[1])
          elif line.startswith("pies:"):
            pie_count = int(line.strip().split(":", 1)[1])
          elif line.startswith("hacks_success:"):
            h_succ = int(line.strip().split(":", 1)[1])
          elif line.startswith("hacks_failed:"):
            h_fail = int(line.strip().split(":", 1)[1])
    except Exception:
      pass

    net_worth = bal + (pie_count * 5000.00)
    rankings.append((uname, bal, pie_count, h_succ, h_fail, net_worth))

  rankings.sort(key=lambda x: x[5], reverse=True)

  print("\n" + "=" * 75)
  print("                  GLOBAL NETRUNNER LEADERBOARD V0.1             ")
  print("=" * 75)
  print(
      f"{'Rank':<5} {'Netrunner':<15} {'Balance':<15} {'Pies':<6}"
      f" {'Success':<8} {'Failed':<8}"
  )
  print("-" * 75)
  for idx, (uname, bal, pies, h_succ, h_fail, nw) in enumerate(rankings, 1):
    print(
        f"{idx:<5} {uname:<15} ${bal:,.2f}    {pies:<6} {h_succ:<8}"
        f" {h_fail:<8}"
    )
  print("=" * 75)


def run_pie_store(
    balance,
    pies,
    hacks_success,
    hacks_failed,
    internet,
    decrypter,
    vpn,
    keylogger,
    crawler,
    insider,
    oven,
    sandevistan,
    davids_jacket,
    icebreaker,
    berserk,
    cynosure,
    heat,
    difficulty,
    loan,
    theme,
    blackmail_time,
    username,
    password,
):
  """Allows players to spend pies on legendary OP items."""
  while True:
    print("\n" + "=" * 50)
    print("           PIE BLACK MARKET [EDGERUNNERS]           ")
    print("=" * 50)
    print(f" Your Pie Collection: 🥧 {pies} pies")
    print("-" * 50)
    print(
        " 1. Sandevistan Implant (5 Pies)       "
        f"{'[OWNED]' if sandevistan==1 else '[AVAILABLE]'}"
    )
    print("    - Effect: Grants permanent +3 lives to all minigames.")
    print(
        " 2. David's Jacket (10 Pies)           "
        f"{'[OWNED]' if davids_jacket==1 else '[AVAILABLE]'}"
    )
    print("    - Effect: Caps Police Heat so it can never exceed 50%.")
    print(
        " 3. Netrunner Icebreaker (15 Pies)     "
        f"{'[OWNED]' if icebreaker==1 else '[AVAILABLE]'}"
    )
    print("    - Effect: Absolute immunity to rival counter-hacks.")
    print(
        " 4. Berserk OS (8 Pies)                "
        f"{'[OWNED]' if berserk==1 else '[AVAILABLE]'}"
    )
    print(
        "    - Effect: 50% chance to ignore a minigame failure and succeed"
        " anyway."
    )
    print(
        " 5. Cynosure Deck (20 Pies)            "
        f"{'[OWNED]' if cynosure==1 else '[AVAILABLE]'}"
    )
    print(
        "    - Effect: Auto-wins counter-hacks + pays out $10k reward bonus."
    )
    print("-" * 50)
    print(" Type 'buy <1-5>' or 'exit' to leave pie store.")

    choice = input("\npiestore@terminal:~$ ").strip().lower()

    if choice == "exit":
      break

    item_num = choice.replace("buy", "").strip()

    if item_num == "1":
      if sandevistan == 1:
        print("[!] You already own the Sandevistan Implant!")
      elif pies >= 5:
        pies -= 5
        sandevistan = 1
        print(
            "[+] IMPLANT INSTALLED: Sandevistan active! (+3 minigame lives)"
        )
      else:
        print(f"[!] Not enough pies! You need 5 pies (You have {pies}).")
    elif item_num == "2":
      if davids_jacket == 1:
        print("[!] You already own David's Jacket!")
      elif pies >= 10:
        pies -= 10
        davids_jacket = 1
        print("[+] EQUIPPED: David's Jacket! (Police Heat capped at 50%)")
      else:
        print(f"[!] Not enough pies! You need 10 pies (You have {pies}).")
    elif item_num == "3":
      if icebreaker == 1:
        print("[!] You already own the Netrunner Icebreaker!")
      elif pies >= 15:
        pies -= 15
        icebreaker = 1
        print("[+] INSTALLED: Icebreaker active! (Counter-hack immunity)")
      else:
        print(f"[!] Not enough pies! You need 15 pies (You have {pies}).")
    elif item_num == "4":
      if berserk == 1:
        print("[!] You already own the Berserk OS!")
      elif pies >= 8:
        pies -= 8
        berserk = 1
        print("[+] INSTALLED: Berserk OS active! (50% fail-to-win chance)")
      else:
        print(f"[!] Not enough pies! You need 8 pies (You have {pies}).")
    elif item_num == "5":
      if cynosure == 1:
        print("[!] You already own the Cynosure Deck!")
      elif pies >= 20:
        pies -= 20
        cynosure = 1
        print(
            "[+] INSTALLED: Cynosure Deck active! (Auto-wins counter-hacks +"
            " $10k bounty)"
        )
      else:
        print(f"[!] Not enough pies! You need 20 pies (You have {pies}).")
    else:
      print("Unknown command. Use 'buy <1-5>' or 'exit'.")

    save_user_data(
        username,
        password,
        balance,
        pies,
        hacks_success,
        hacks_failed,
        internet,
        decrypter,
        vpn,
        keylogger,
        crawler,
        insider,
        oven,
        sandevistan,
        davids_jacket,
        icebreaker,
        berserk,
        cynosure,
        heat,
        difficulty,
        loan,
        theme,
        blackmail_time,
    )

  return (
      balance,
      pies,
      hacks_success,
      hacks_failed,
      internet,
      decrypter,
      vpn,
      keylogger,
      crawler,
      insider,
      oven,
      sandevistan,
      davids_jacket,
      icebreaker,
      berserk,
      cynosure,
      heat,
      difficulty,
      loan,
      theme,
      blackmail_time,
  )


def run_loan_shark(balance, loan, username, password, rest_data):
  """Allows players to borrow money from the Dark Web Loan Shark."""
  while True:
    print("\n" + "=" * 50)
    print("            DARK WEB LOAN SHARK TERMINAL            ")
    print("=" * 50)
    print(f" Your Balance: ${balance:,.2f}")
    print(f" Current Debt Owed: ${loan:,.2f}")
    print("-" * 50)
    print(" Type 'borrow' to take a $50,000 loan (Owe $65,000 back).")
    print(" Type 'pay'    to pay off your entire debt.")
    print(" Type 'exit'   to leave loan shark.")

    choice = input("\nloan@terminal:~$ ").strip().lower()

    if choice == "exit":
      break
    elif choice == "borrow":
      if loan > 0:
        print("[!] You already have an active loan! Pay it off first.")
      else:
        balance = round(balance + 50000.00, 2)
        loan = 65000.00
        print("[+] Loan secured! Added $50,000 to your balance. (Debt: $65,000)")
    elif choice == "pay":
      if loan == 0:
        print("[*] You don't owe anything!")
      elif balance >= loan:
        balance = round(balance - loan, 2)
        print(f"[+] Debt fully paid off! Clean slate.")
        loan = 0.00
      else:
        print(f"[!] Insufficient funds to clear debt! You need ${loan:,.2f}.")
    else:
      print("Unknown command. Type 'borrow', 'pay', or 'exit'.")

    (
        pies,
        hacks_success,
        hacks_failed,
        internet,
        decrypter,
        vpn,
        keylogger,
        crawler,
        insider,
        oven,
        sandevistan,
        davids_jacket,
        icebreaker,
        berserk,
        cynosure,
        heat,
        difficulty,
        theme,
        blackmail_time,
    ) = rest_data
    save_user_data(
        username,
        password,
        balance,
        pies,
        hacks_success,
        hacks_failed,
        internet,
        decrypter,
        vpn,
        keylogger,
        crawler,
        insider,
        oven,
        sandevistan,
        davids_jacket,
        icebreaker,
        berserk,
        cynosure,
        heat,
        difficulty,
        loan,
        theme,
        blackmail_time,
    )

  return balance, loan


def process_hack_outcome(
    profit,
    balance,
    pies,
    hacks_success,
    hacks_failed,
    success_flag,
    internet,
    decrypter,
    vpn,
    keylogger,
    crawler,
    insider,
    oven,
    sandevistan,
    davids_jacket,
    icebreaker,
    berserk,
    cynosure,
    heat,
    difficulty,
    loan,
    theme,
    blackmail_time,
    username,
    password,
):
  if success_flag:
    hacks_success += 1
  else:
    hacks_failed += 1

  if profit > 0:
    if keylogger == 1:
      profit = round(profit * 1.25, 2)
    if insider == 1:
      profit = round(profit * 2.0, 2)

  balance = round(balance + profit, 2)

  heat_increase = random.randint(15, 30)
  if vpn == 1:
    heat_increase = int(heat_increase / 2)
  heat = min(100, heat + heat_increase)

  if davids_jacket == 1 and heat > 50:
    heat = 50

  if oven == 1 and random.random() < 0.0314:
    pies += 1
    print(
        "[🥧] MASTER CHEF'S OVEN: A fresh pie baked successfully during the"
        " hack!"
    )

  if loan > 0:
    loan = round(loan * 1.05, 2)
    print(f"[!] LOAN INTEREST APPLIED: Debt increased to ${loan:,.2f}")

  profit_str = f"{profit:.2f}"
  is_pie_drop = profit_str.endswith("3.14") and profit > 0

  print("-" * 40)
  if is_pie_drop:
    pies += 1
    pie_label = "pie" if pies == 1 else "pies"
    print(f"[SUCCESS] Target breached! You stole ${profit:,.2f} and a PIE! 🥧")
    print(f"[*] Updated Balance: ${balance:,.2f} + {pies} {pie_label}")
  elif profit > 0:
    print(f"[SUCCESS] Target breached! You stole ${profit:,.2f}")
    pie_text = f" + {pies} {'pie' if pies == 1 else 'pies'}" if pies > 0 else ""
    print(f"[*] Updated Balance: ${balance:,.2f}{pie_text}")
  elif profit < 0:
    print(
        f"[ALERT]   Trace detected! Security penalized you"
        f" -${abs(profit):,.2f}"
    )
    pie_text = f" + {pies} {'pie' if pies == 1 else 'pies'}" if pies > 0 else ""
    print(f"[*] Updated Balance: ${balance:,.2f}{pie_text}")
  else:
    print("[NEUTRAL] Hack successful, but no funds or penalties found ($0.00)")
    pie_text = f" + {pies} {'pie' if pies == 1 else 'pies'}" if pies > 0 else ""
    print(f"[*] Updated Balance: ${balance:,.2f}{pie_text}")

  print(f"[🔥] Police Heat Level: {heat}%")
  print("-" * 40)

  save_user_data(
      username,
      password,
      balance,
      pies,
      hacks_success,
      hacks_failed,
      internet,
      decrypter,
      vpn,
      keylogger,
      crawler,
      insider,
      oven,
      sandevistan,
      davids_jacket,
      icebreaker,
      berserk,
      cynosure,
      heat,
      difficulty,
      loan,
      theme,
      blackmail_time,
  )
  return (
      balance,
      pies,
      hacks_success,
      hacks_failed,
      internet,
      decrypter,
      vpn,
      keylogger,
      crawler,
      insider,
      oven,
      sandevistan,
      davids_jacket,
      icebreaker,
      berserk,
      cynosure,
      heat,
      difficulty,
      loan,
      theme,
      blackmail_time,
  )


def run_shop(
    balance,
    pies,
    hacks_success,
    hacks_failed,
    internet,
    decrypter,
    vpn,
    keylogger,
    crawler,
    insider,
    oven,
    sandevistan,
    davids_jacket,
    icebreaker,
    berserk,
    cynosure,
    heat,
    difficulty,
    loan,
    theme,
    blackmail_time,
    username,
    password,
):
  while True:
    print("\n" + "=" * 50)
    print("            CYBER-CMD: BLACK MARKET SHOP            ")
    print("=" * 50)
    print(f" Your Current Balance: ${balance:,.2f}")
    print("-" * 50)
    print(
        " 1. Fiber Optic Internet ($80,000)      "
        f"{'[OWNED]' if internet==1 else '[AVAILABLE]'}"
    )
    print(
        " 2. Quantum Auto-Decrypter ($200,000)   "
        f"{'[OWNED]' if decrypter==1 else '[AVAILABLE]'}"
    )
    print(
        " 3. VPN Proxy Router ($50,000)         "
        f"{'[OWNED]' if vpn==1 else '[AVAILABLE]'}"
    )
    print(
        " 4. Hardware Keylogger ($120,000)      "
        f"{'[OWNED]' if keylogger==1 else '[AVAILABLE]'}"
    )
    print(
        " 5. AI Subnet Crawler ($350,000)       "
        f"{'[OWNED]' if crawler==1 else '[AVAILABLE]'}"
    )
    print(
        " 6. Corporate Insider Pass ($500,000)  "
        f"{'[OWNED]' if insider==1 else '[AVAILABLE]'}"
    )
    print("    - Effect: DOUBLES all cash payouts from successful hacks.")
    print(
        " 7. Master Chef's Oven ($1,000,000)    "
        f"{'[OWNED]' if oven==1 else '[AVAILABLE]'}"
    )
    print("-" * 50)
    print(" Type 'buy <number>' (e.g. 'buy 6') or 'exit' to leave.")

    choice = input("\nshop@terminal:~$ ").strip().lower()

    if choice == "exit":
      break

    item_num = choice.replace("buy", "").strip()

    items_data = {
        "1": ("Fiber Optic Internet", 80000, lambda: globals().update(internet=1)),
        "2": (
            "Quantum Auto-Decrypter",
            200000,
            lambda: globals().update(decrypter=1),
        ),
        "3": ("VPN Proxy Router", 50000, lambda: globals().update(vpn=1)),
        "4": ("Hardware Keylogger", 120000, lambda: globals().update(keylogger=1)),
        "5": ("AI Subnet Crawler", 350000, lambda: globals().update(crawler=1)),
        "6": (
            "Corporate Insider Pass",
            500000,
            lambda: globals().update(insider=1),
        ),
        "7": ("Master Chef's Oven", 1000000, lambda: globals().update(oven=1)),
    }

    if item_num in items_data:
      name, cost, activate_fn = items_data[item_num]
      owned_list = [internet, decrypter, vpn, keylogger, crawler, insider, oven]
      if owned_list[int(item_num) - 1] == 1:
        print(f"[!] You already own {name}!")
      elif balance >= cost:
        balance = round(balance - cost, 2)
        activate_fn()
        internet, decrypter, vpn, keylogger, crawler, insider, oven = (
            globals()["internet"],
            globals()["decrypter"],
            globals()["vpn"],
            globals()["keylogger"],
            globals()["crawler"],
            globals()["insider"],
            globals()["oven"],
        )
        save_user_data(
            username,
            password,
            balance,
            pies,
            hacks_success,
            hacks_failed,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            heat,
            difficulty,
            loan,
            theme,
            blackmail_time,
        )
        print(f"[+] Successfully purchased {name}!")
      else:
        print(f"[!] Insufficient funds! You need ${cost:,.2f}.")
    else:
      print("Unknown shop command. Use 'buy <1-7>' or 'exit'.")

  return (
      balance,
      pies,
      hacks_success,
      hacks_failed,
      internet,
      decrypter,
      vpn,
      keylogger,
      crawler,
      insider,
      oven,
      sandevistan,
      davids_jacket,
      icebreaker,
      berserk,
      cynosure,
      heat,
      difficulty,
      loan,
      theme,
      blackmail_time,
  )


def main():
  global internet, decrypter, vpn, keylogger, crawler, insider, oven

  while True:
    auth_data = auth_screen()
    if not auth_data:
      break

    (
        password,
        balance,
        pies,
        hacks_success,
        hacks_failed,
        internet,
        decrypter,
        vpn,
        keylogger,
        crawler,
        insider,
        oven,
        sandevistan,
        davids_jacket,
        icebreaker,
        berserk,
        cynosure,
        heat,
        difficulty,
        loan,
        theme,
        blackmail_time,
        username,
    ) = auth_data

    print_banner(
        username,
        internet,
        decrypter,
        vpn,
        keylogger,
        crawler,
        insider,
        oven,
        sandevistan,
        davids_jacket,
        icebreaker,
        berserk,
        cynosure,
        difficulty,
        loan,
    )

    logged_in = True
    while logged_in:
      try:
        command = input(f"\n{username}@terminal:~$ ").strip()
      except (KeyboardInterrupt, EOFError):
        print(f"\nDisconnecting... Goodbye, {username}.")
        sys.exit(0)

      cmd_lower = command.lower()

      if cmd_lower == "exit":
        print(f"Disconnecting... Goodbye, {username}.")
        sys.exit(0)

      elif cmd_lower == "logout":
        print(f"\n[+] Logging out session for {username}...")
        logged_in = False

      elif cmd_lower == "shop":
        (
            balance,
            pies,
            hacks_success,
            hacks_failed,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            heat,
            difficulty,
            loan,
            theme,
            blackmail_time,
        ) = run_shop(
            balance,
            pies,
            hacks_success,
            hacks_failed,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            heat,
            difficulty,
            loan,
            theme,
            blackmail_time,
            username,
            password,
        )
        print_banner(
            username,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            difficulty,
            loan,
        )

      elif cmd_lower == "piestore":
        (
            balance,
            pies,
            hacks_success,
            hacks_failed,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            heat,
            difficulty,
            loan,
            theme,
            blackmail_time,
        ) = run_pie_store(
            balance,
            pies,
            hacks_success,
            hacks_failed,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            heat,
            difficulty,
            loan,
            theme,
            blackmail_time,
            username,
            password,
        )
        print_banner(
            username,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            difficulty,
            loan,
        )

      elif cmd_lower == "loan":
        balance, loan = run_loan_shark(
            balance,
            loan,
            username,
            password,
            (
                pies,
                hacks_success,
                hacks_failed,
                internet,
                decrypter,
                vpn,
                keylogger,
                crawler,
                insider,
                oven,
                sandevistan,
                davids_jacket,
                icebreaker,
                berserk,
                cynosure,
                heat,
                difficulty,
                theme,
                blackmail_time,
            ),
        )
        print_banner(
            username,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            difficulty,
            loan,
        )

      elif cmd_lower == "leaderboard":
        show_leaderboard()

      elif cmd_lower == "blackmail":
        b_amount = round(random.uniform(30000.00, 60000.00), 2)
        balance = round(balance + b_amount, 2)
        heat = 100
        blackmail_time = time.time()

        print(
            f"\n[+] BLACKMAIL SUCCESSFUL: Extorted ${b_amount:,.2f} from a"
            " megacorp!"
        )
        print(
            "[!] WARNING: Megacorps traced your signal! Police Heat maxed to"
            " 100%!"
        )
        print(
            "[!] LOCKOUT: You cannot clear Police Heat for 10 real-time"
            " minutes!"
        )

        save_user_data(
            username,
            password,
            balance,
            pies,
            hacks_success,
            hacks_failed,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            heat,
            difficulty,
            loan,
            theme,
            blackmail_time,
        )

      elif cmd_lower.startswith("theme "):
        new_theme = cmd_lower[6:].strip()
        if new_theme in ["matrix", "amber", "cyber", "default"]:
          theme = new_theme
          apply_theme(theme)
          save_user_data(
              username,
              password,
              balance,
              pies,
              hacks_success,
              hacks_failed,
              internet,
              decrypter,
              vpn,
              keylogger,
              crawler,
              insider,
              oven,
              sandevistan,
              davids_jacket,
              icebreaker,
              berserk,
              cynosure,
              heat,
              difficulty,
              loan,
              theme,
              blackmail_time,
          )
          print(f"[+] Theme changed to {theme.upper()}!")
        else:
          print("[!] Available themes: matrix, amber, cyber, default")

      elif cmd_lower.startswith("diff "):
        new_diff = cmd_lower[5:].strip()
        if new_diff in ["easy", "normal", "hard"]:
          difficulty = new_diff
          save_user_data(
              username,
              password,
              balance,
              pies,
              hacks_success,
              hacks_failed,
              internet,
              decrypter,
              vpn,
              keylogger,
              crawler,
              insider,
              oven,
              sandevistan,
              davids_jacket,
              icebreaker,
              berserk,
              cynosure,
              heat,
              difficulty,
              loan,
              theme,
              blackmail_time,
          )
          print(f"[+] Difficulty successfully updated to {difficulty.upper()}!")
        else:
          print("[!] Invalid difficulty! Choose: easy, normal, or hard.")

      elif cmd_lower == "clear":
        time_since_bm = time.time() - blackmail_time
        cooldown_period = 600.0

        if time_since_bm < cooldown_period:
          remaining = int(cooldown_period - time_since_bm)
          mins = remaining // 60
          secs = remaining % 60
          print(
              f"\n[!] CLEAR DENIED: Megacorp surveillance active! Cooldown"
              f" remaining: {mins}m {secs}s"
          )
        elif heat == 0:
          print("[*] Police Heat is already at 0%.")
        elif balance >= 1000.00:
          balance = round(balance - 1000.00, 2)
          heat = 0
          save_user_data(
              username,
              password,
              balance,
              pies,
              hacks_success,
              hacks_failed,
              internet,
              decrypter,
              vpn,
              keylogger,
              crawler,
              insider,
              oven,
              sandevistan,
              davids_jacket,
              icebreaker,
              berserk,
              cynosure,
              heat,
              difficulty,
              loan,
              theme,
              blackmail_time,
          )
          print("[+] Bribe paid. Police Heat reset to 0%!")
        else:
          print("[!] Insufficient funds to clear heat ($1,000 required).")

      elif cmd_lower == "balance":
        pie_text = f" + {pies} {'pie' if pies == 1 else 'pies'}" if pies > 0 else ""
        print(f"[*] Current Balance: ${balance:,.2f}{pie_text}")
        print(
            f"[*] Police Heat: {heat}% | Difficulty: {difficulty.upper()}"
            f" | Theme: {theme}"
        )
        print(
            f"[*] Hack Stats -> Successful: {hacks_success} | Failed:"
            f" {hacks_failed}"
        )

        time_since_bm = time.time() - blackmail_time
        if time_since_bm < 600.0:
          remaining = int(600.0 - time_since_bm)
          print(
              f"[*] Megacorp Blackmail Lockout: {remaining // 60}m"
              f" {remaining % 60}s remaining"
          )

        if loan > 0:
          print(f"[*] Active Debt: ${loan:,.2f}")

      elif cmd_lower == "help":
        print("\nAvailable Commands:")
        print("  hack          - Infiltrate a system")
        print(
            "  blackmail     - Extort a corp for instant cash ($30k-$60k, 10m"
            " heat lock)"
        )
        print("  shop          - Buy cash upgrades")
        print("  piestore      - Spend pies on Edgerunners OP items")
        print("  loan          - Dark Web Loan Shark")
        print("  leaderboard   - View netrunner rankings")
        print("  theme <color> - Switch command prompt color theme")
        print("  diff <lvl>    - Change hacking difficulty")
        print("  clear         - Pay $1,000 bribe to clear heat")
        print("  balance       - View status & funds")
        print("  logout        - Return to main menu")
        print("  exit          - Quit")

      elif cmd_lower == "hack":
        counter_hack_chance = heat / 100.0
        print(
            f"[*] Scanning network... [Police Heat: {heat}% | Counter-Hack Risk:"
            f" {int(counter_hack_chance * 100)}%]"
        )

        counter_hack_triggered = random.random() < counter_hack_chance
        counter_success = True

        if counter_hack_triggered:
          if cynosure == 1:
            print(
                "\n[+] CYNOSURE DECK ACTIVE: Rival hacker group automatically"
                " wiped out! (+$10,000 bounty)"
            )
            balance = round(balance + 10000.00, 2)
          elif icebreaker == 1:
            print(
                "\n[+] NETRUNNER ICEBREAKER ACTIVE: Counter-hack instantly"
                " neutralized!"
            )
          else:
            counter_success = run_counter_hack()
            if not counter_success:
              penalty = round(random.uniform(15000.00, 25000.00), 2)
              print(
                  f"[X] BREACHED BY RIVAL HACKERS! They drained -${penalty:,.2f}"
                  " from your account!"
              )
              (
                  balance,
                  pies,
                  hacks_success,
                  hacks_failed,
                  internet,
                  decrypter,
                  vpn,
                  keylogger,
                  crawler,
                  insider,
                  oven,
                  sandevistan,
                  davids_jacket,
                  icebreaker,
                  berserk,
                  cynosure,
                  heat,
                  difficulty,
                  loan,
                  theme,
                  blackmail_time,
              ) = process_hack_outcome(
                  -penalty,
                  balance,
                  pies,
                  hacks_success,
                  hacks_failed,
                  False,
                  internet,
                  decrypter,
                  vpn,
                  keylogger,
                  crawler,
                  insider,
                  oven,
                  sandevistan,
                  davids_jacket,
                  icebreaker,
                  berserk,
                  cynosure,
                  heat,
                  difficulty,
                  loan,
                  theme,
                  blackmail_time,
                  username,
                  password,
              )
              continue

        auto_bypassed = False
        if crawler == 1 and random.random() < 0.20:
          print("\n[+] AI SUBNET CRAWLER: Minigame automatically bypassed!")
          auto_bypassed = True

        success = True
        if not auto_bypassed:
          success = run_hack_minigame(
              internet, decrypter, sandevistan, difficulty
          )

        if not success and berserk == 1 and random.random() < 0.50:
          print(
              "\n[+] BERSERK OS OVERRIDE: Firewall failure ignored! Forcing"
              " hack success!"
          )
          success = True

        if difficulty == "easy":
          raw_amount = (
              random.uniform(0.00, 3000.00)
              if success
              else random.uniform(-3000.00, 0.00)
          )
        elif difficulty == "hard":
          raw_amount = (
              random.uniform(0.00, 25000.00)
              if success
              else random.uniform(-25000.00, 0.00)
          )
        else:  # normal
          raw_amount = (
              random.uniform(0.00, 10000.00)
              if success
              else random.uniform(-10000.00, 0.00)
          )

        profit = round(raw_amount, 2)
        (
            balance,
            pies,
            hacks_success,
            hacks_failed,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            heat,
            difficulty,
            loan,
            theme,
            blackmail_time,
        ) = process_hack_outcome(
            profit,
            balance,
            pies,
            hacks_success,
            hacks_failed,
            success,
            internet,
            decrypter,
            vpn,
            keylogger,
            crawler,
            insider,
            oven,
            sandevistan,
            davids_jacket,
            icebreaker,
            berserk,
            cynosure,
            heat,
            difficulty,
            loan,
            theme,
            blackmail_time,
            username,
            password,
        )

      else:
        print(
            f"Unknown command: '{command}'. Type 'help' for available"
            " commands."
        )


if __name__ == "__main__":
  main()
