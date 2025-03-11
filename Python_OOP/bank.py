import os
import pickle
DATA_FILE = "banks.accounts.dat"

def load_accounts():
	try:
		with open(DATA_FILE, 'rb') as f:
			return pickle.load(f)
	except (FileNotFoundError, EOFError):
		return {}

def save_accounts(accounts):
	with open(DATA_FILE, "wb") as f:
		pickle.dump(accounts, f)

class CheckingAccount:
	def __init__(self, account_number: str,
				owner_name: str, password: str,
				balance: float = 0.0):
		self.account_number = account_number
		self.owner_name = owner_name
		self.balance = balance
		self.password = password

	def authenticate(self):
		userpassword = input("Enter your password: ")

		if userpassword == self.password:
			return True
		else:
			print("Invalid password")
			return False

	def deposit(self, amount: float):
		if amount <= 0:
			print("Deposit must be more than 0")
			return

		self.balance += amount
		print(f"Deposited ${amount:.2f} successfully. New balance is {self.balance:.2f}")

	def withdraw(self, amount:float):
		if amount <= 0:
			print("Withdrawal must be more than 0")
			return

		if amount > self.balance:
			print("Insufficient funds.")
			return

		self.balance -= amount
		print("Cha-ching!!")
		print(f"Successfully withdrew ${amount:.2f}. New balance is {self.balance:.2f}")

	def check_balance(self):
		print(f"Your balance is {self.balance:.2f}")

	def audit(self):
		print ("--------------------------------------------------------------") 
		print(f"account_number: {self.account_number}")
		print(f"owner_name: {self.owner_name}")
		print(f"balance: {self.balance}")

class SavingsAccount(CheckingAccount):
	def __init__(
		self,
		account_number: str,
		owner_name: str,
		password: str,
		balance: float = 0.0,
		interest_rate: float = 0.1,
		max_withdrawals_per_month: int = 3
	):

		super().__init__(account_number, owner_name, password, balance)

		self.interest_rate = interest_rate
		self.max_withdrawals_per_month = max_withdrawals_per_month
		self.withdrawals_this_month = 0

	def apply_interest(self):
		interest_amount = self.balance * self.interest_rate
		self.balance += interest_amount

		print(
			f"Interest of %{interest_amount:.2f} applied at rate {self.interest_rate:.2f}."
			f"New balance os ${self.balance:.2f}.")

	def withdraw(self, amount:float):
		if self.withdrawals_this_month >= self.max_withdrawals_per_month:
			print(
				"Withdrawal limit reached! You can only withdraw "
				f"{self.max_withdrawals_per_month} times per month.")
			return

		prev_balance = self.balance
		super().withdraw(amount)

		''' Check if withdrawal was successfull '''
		if self.balance < prev_balance:
			self.withdrawals_this_month += 1

	def reset_withdrawals(self):
		self.withdrawals_this_month = 0

	def audit(self):
		super().audit()
		print(f"interest rate: {self.interest_rate}")
		print(f"max_withdrawals per month: {self.max_withdrawals_per_month}")
		print(f"withdrawals this month: {self.withdrawals_this_month}")


def main():
	accounts = load_accounts()
	start = 1

	while True:

		if not start:
			input("Continue:")

		os.system("clear")

		start = 0

		print("\n=== Simple Bank Account Sim ===")
		print("1. Create Checking Account")
		print("2. Create Savings Account")
		print("3. Deposit")
		print("4. Withdraw")
		print("5. Check Balance")
		print("6. Apply interest to savings")
		print("7. Reset Monthly withdraw count")
		print("8. Audit")
		print("9. EXIT")

		choice = input("\nEnter your choice: ").strip()

		if choice == "1":
			account_number = input("Enter new checking account number: ").strip()
			if account_number in accounts:
				print("Account exists")
				continue
			owner = input("Enter owners name: ").strip()
			password = input("Enter password: ")

			''' Add account to list
			'''
			accounts[account_number] = CheckingAccount(account_number=account_number, 
													owner_name=owner, password = password)
			save_accounts(accounts)
			print(f"Account {account_number} successfully created")

		elif choice == "2":
			account_number = input("Enter new savings account number: ").strip()
			if account_number in accounts:
				print("Account exists")
				continue
			owner = input("Enter owners name: ").strip()
			password = input("Enter password: ")

			try:
				rate = float(input("Enter interest rate: ").strip())
			except ValueError:
				print("Invalid interest rate. Defaulting to 1%")
				rate = .01

			try:
				max_withdrawals = int(input("Enter the max withdrawals per month: ").strip())
			except ValueError:
				print("Invalid input. Defaulting to 3")
				max_withdrawals = 3

			''' Add account to list
			'''
			accounts[account_number] = SavingsAccount(account_number=account_number,
													owner_name=owner,
													password = password,
													interest_rate = rate,
													max_withdrawals_per_month = max_withdrawals)
			save_accounts(accounts)
			print(f"Account {account_number} successfully created")

		elif choice == "3":
			account_number = input("Enter account number: ").strip()
			if account_number not in accounts:
				print("Account not found")
				continue

			if not accounts[account_number].authenticate():
				continue

			try:
				amount = float(input("Enter deposit amount: ").strip())
			except ValueError:
				print("Invalid amount.")
				continue

			accounts[account_number].deposit(amount)
			save_accounts(accounts)

		elif choice == "4":
			account_number = input("Enter account number: ").strip()
			if account_number not in accounts:
				print("Account not found")
				continue

			if not accounts[account_number].authenticate():
				continue

			try:
				amount = float(input("Enter withdrawal amount: ").strip())
			except ValueError:
				print("Invalid amount.")
				continue

			accounts[account_number].withdraw(amount)
			save_accounts(accounts)

		elif choice == "5":
			account_number = input("Enter account number: ").strip()
			if account_number not in accounts:
				print("Account not found")
				continue

			accounts[account_number].check_balance()

		elif choice == "6":
			account_number = input("Enter account number: ").strip()
			if account_number not in accounts:
				print("Account not found")
				continue

			if not isinstance(accounts[account_number], SavingsAccount):
				print("Option only valid with Savings accounts.")
				continue
			else:
				accounts[account_number].apply_interest()
				save_accounts(accounts)

			print("interest added successfully")

		elif choice == "7":
			account_number = input("Enter account number: ").strip()
			if account_number not in accounts:
				print("Account not found")
				continue

			if not isinstance(accounts[account_number], SavingsAccount):
				print("Option only valid with Savings accounts.")
				continue
			else:
				save_accounts(accounts)
				accounts[account_number].withdrawals_this_month =  0

			print("interest added successfully")

		elif choice == "8":
			print("SYSTEM AUDIT **************")
			for key in accounts:
				accounts[key].audit()
				print("")

		elif choice == "9":
			break

		else:
			print("Invalid choice")

main()


