from .utils import pluralise

ALL = 'ALL'
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'
CRUD = 'CRUD'  # shorthand for creating the ALL|GET|POST|PUT|DELETE endpoints in one swoop

METHOD_ORDER = [ALL, GET, POST, PUT, DELETE]

ENDPOINTS = {
    'Banking/': {
        'name': 'banking',
        'methods': [
            (ALL, '', 'banking type'),
            (CRUD, 'SpendMoneyTxn/', 'spend money transaction'),
            (CRUD, 'ReceiveMoneyTxn/', 'receive money transaction'),
            (CRUD, 'TransferMoneyTxn/', 'transfer money transaction'),
            (CRUD, 'BankAccount/', 'bank accounts'),
            (CRUD, 'Statement/', 'bank statements'),
        ],
    },
    'Contact/': {
        'name': 'contacts',
        'methods': [
            (ALL, '', 'contact type'),
            (CRUD, 'Customer/', 'customer contact'),
            (CRUD, 'Employee/', 'employee card'),
            (CRUD, 'Supplier/', 'supplier contact'),
        ],
    },
    'Sale/CustomerPayment/': {
        'name': 'customer_payments',
        'methods': [
            (ALL, '', 'sale customer payment'),
            (GET, '', 'sale customer payment'),
            (POST, '', 'sale customer payment'),
            (DELETE, '', 'sale customer payment'),
        ]
    },
    'Sale/CreditRefund/': {
        'name': 'credit_refunds',
        'methods': [
            (ALL, '', 'credit notes refunded to customers'),
            (GET, '', 'credit notes refunded to customers'),
            (POST, '', 'credit notes refunded to customers'),
            (DELETE, '', 'credit notes refunded to customers'),
        ]
    },
    'Sale/CreditSettlement/': {
        'name': 'credit_settlements',
        'methods': [
            (ALL, '', 'settled customer credits'),
            (GET, '', 'settled customer credits'),
            (POST, '', 'settled customer credits'),
            (DELETE, '', 'settled customer credits'),
        ]
    },
    'Sale/Invoice/': {
        'name': 'invoices',
        'methods': [
            (ALL, '', 'sale invoice type'),
            (CRUD, 'Item/', 'item type sale invoice'),
            (CRUD, 'Service/', 'service type sale invoice'),
            (CRUD, 'Miscellaneous/', 'miscellaneous type sale invoice'),
            (CRUD, 'Professional/', 'professional type sale invoice'),
            (CRUD, 'TimeBilling/', 'timebilling type sale invoice'),
        ]
    },
    'Sale/Order/': {
        'name': 'orders',
        'methods': [
            (ALL, '', 'sale order type'),
            (CRUD, 'Item/', 'item type sale order'),
            (CRUD, 'Service/', 'service type sale order'),
        ]
    },
    'Sale/Quote/': {
        'name': 'quotes',
        'methods': [
            (ALL, '', 'sale quote type'),
            (CRUD, 'Item/', 'item type sale quote'),
            (CRUD, 'Service/', 'service type sale quote'),
        ]
    },
    'GeneralLedger/': {
        'name': 'general_ledger',
        'methods': [
            (CRUD, 'TaxCode/', 'tax code'),
            (CRUD, 'Account/', 'account'),
            (CRUD, 'Category/', 'cost center tracking category'),
            (CRUD, 'Job/', 'job'),
            (ALL, 'JournalTransaction/', 'transaction journal'),
            (GET, 'JournalTransaction/', 'transaction journal'),
            (CRUD, 'Currency/', 'currency'),  # TODO: Added
            (ALL, 'GeneralJournal/', 'general journal transactions'),  # TODO: Added
            (GET, 'AccountingProperties/', 'information on the financial year details'),  # TODO: Added
            (GET, 'LinkedAccount/', 'account links and defaults'),  # TODO: Added
        ]
    },
    'Inventory/': {
        'name': 'inventory',
        'methods': [
            (CRUD, 'Item/', 'inventory item'),
            (ALL, 'ItemPriceMatrix/', 'inventory item price matrix'),
            (GET, 'ItemPriceMatrix/', 'inventory item price matrix'),
            (PUT, 'ItemPriceMatrix/', 'inventory item price matrix'),
            (CRUD, 'Location/', 'inventory location'),
            (CRUD, 'Adjustment/', 'inventory adjustment')
        ]
    },
    'Purchase/Order/': {
        'name': 'purchase_orders',
        'methods': [
            (ALL, '', 'purchase order type'),
            (CRUD, 'Item/', 'item type purchase order'),
        ]
    },
    'Purchase/Bill/': {
        'name': 'purchase_bills',
        'methods': [
            (ALL, '', 'purchase bill type'),
            (CRUD, 'Item/', 'item type purchase bill'),
            (CRUD, 'Service/', 'service type purchase bill'),
            (CRUD, 'Miscellaneous/', 'miscellaneous type purchase bill'),
            (CRUD, 'Professional/', 'professional type purchase bill'),
        ]
    },
    'Purchase/DebitRefund/': {
        'name': 'debit_refunds',
        'methods': [
            (ALL, '', 'debit refunds paid from suppliers'),
            (GET, '', 'debit refunds paid from suppliers'),
            (POST, '', 'debit refunds paid from suppliers'),
            (DELETE, '', 'debit refunds paid from suppliers'),
        ]
    },
    'Purchase/DebitSettlement/': {
        'name': 'debit_settlements',
        'methods': [
            (ALL, '', 'debit settlements'),
            (GET, '', 'debit settlements'),
            (POST, '', 'debit settlements'),
            (DELETE, '', 'debit settlements'),
        ]
    },
    'Purchase/SupplierPayment/': {
        'name': 'supplier_payments',
        'methods': [
            (ALL, '', 'purchase supplier payment'),
            (GET, '', 'purchase supplier payment'),
            (POST, '', 'purchase supplier payment'),
            (DELETE, '', 'purchase supplier payment'),
        ]
    },
    'Company/': {
        'name': 'company',
        'methods': [
            (ALL, 'Preferences/', 'company data file preference'),
            (GET, 'CustomList/', 'Returns CustomLists and their CustomListValues'),
        ]
    },
    # https://github.com/uptick/pymyob/pull/76/files
    'Report/': {
        'name': 'reports',
        'methods': [
            (ALL, 'BalanceSheetSummary/?AsOfDate=[AsOfDate]&YearEndAdjust=[YearEndAdjust]&ReportingBasis=[ReportingBasis]', 'balance sheet summary'),
            (ALL, 'ProfitAndLossSummary/?StartDate=[StartDate]&EndDate=[EndDate]&ReportingBasis=[ReportingBasis]&YearEndAdjust=[YearEndAdjust]', 'profit loss summary'),
        ]
    }
}

METHOD_MAPPING = {
    ALL: {
        'endpoint': lambda base: base,
        'hint': lambda name: 'Return all %s for an AccountRight company file.' % pluralise(name)
    },
    GET: {
        'endpoint': lambda base: base + '[uid]/',
        'hint': lambda name: 'Return selected %s.' % name
    },
    PUT: {
        'endpoint': lambda base: base + '[uid]/',
        'hint': lambda name: 'Update selected %s.' % name
    },
    POST: {
        'endpoint': lambda base: base,
        'hint': lambda name: 'Create new %s.' % name
    },
    DELETE: {
        'endpoint': lambda base: base + '[uid]/',
        'hint': lambda name: 'Delete selected %s.' % name
    },
}
