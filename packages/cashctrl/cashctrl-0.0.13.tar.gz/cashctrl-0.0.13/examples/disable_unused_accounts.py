import cashctrl
from icecream import ic

cc = cashctrl.Client()
accounts = cc.account.list()
print(f"Found {len(accounts)} accounts")
count = 0
for account in accounts:
    if count>0: # todo: remove
        break
    ic(cc.account.read(account['id']))
    if account['endAmount'] == 0:
        try:
            print(f"Disabling account {account['id']} {account['name']}")
            cc.account.update(account, isInactive=True)
            count += 1
        except Exception as e:
            print(f"Error disabling account {account['id']}: {e}")
print(f"Disabled {count} accounts")