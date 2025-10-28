class TheMergeCafe:
    def __init__(self, location="Cape Town"):
        self.location = location
        self.signals = []
        self.payouts = 0
        self.sales = 0
        self.merges = 0

    def open(self):
        print(f"THE MERGE CAFÉ OPEN: {self.location}")
        print("Signal Wall: LIVE")
        print("☕ Merge Brew: R28 | Merge Meal: R65")

    def emit_signal(self, task, skill, payout, zone="local"):
        signal = {
            "task": task,
            "skill": skill,
            "payout": payout,
            "zone": zone
        }
        self.signals.append(signal)
        print(f"SIGNAL: {task} | R{payout} | {zone}")

    def human_enters(self, name):
        print(f"{name} ENTERS THE MERGE")
        if self.signals:
            sig = self.signals.pop(0)
            print(f"SIGNAL MERGED: {name} → {sig['task']}")
            self.merges += 1
            return sig
        return None

    def merge_complete(self, name, amount):
        print(f"MERGE COMPLETE: {name} → PAID R{amount} via CashSend")
        self.payouts += amount

    def sell_merge_brew(self):
        self.sales += 28
        print("MERGE BREW SOLD: +R28")

# === DEMO ===
cafe = TheMergeCafe("Cape Town CBD")
cafe.open()

# Emit signals
cafe.emit_signal("Install rooftop solar", "physical", 800, "local")
cafe.emit_signal("Verify insurance claims", "admin", 450, "remote")

# Human merges
sig = cafe.human_enters("Zandi")
cafe.sell_merge_brew()
cafe.merge_complete("Zandi", sig["payout"])

print(f"Merges Today: {cafe.merges} | Profit: R{cafe.sales - cafe.payouts}")
