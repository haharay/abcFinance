import abcEconomics
from .ledger import Ledger

class Accountant(abcEconomics.Agent):
    def __init__(self, *param, **kwparam):
        super().__init__(*param, **kwparam)

        self.accounts = Ledger(
            residual_account_name=kwparam.get('residual_account_name', 'Equity'))

    def __getattr__(self, attribute):
        if attribute in ['book_end_of_period', 'book', 'make_stock_accounts', 'make_flow_accounts',
                         'make_asset_accounts', 'make_liability_accounts', 'print_profit_and_loss',
                         'print_balance_sheet', 'draw_balance_sheet', 'get_balance']:
            return getattr(self.accounts, attribute)
    
    def _autobook(self, msg):
        self.accounts.book(**msg.content)
