# library
from library.loan.test import accounts

# Standard def exceeds 30 characters
INTERNAL_CAPITALISED_INTEREST_RECEIVABLE = "CAPITALISED_INT_RECEIVABLE"
INTERNAL_INTEREST_RECEIVED = accounts.INTERNAL_INTEREST_RECEIVED
INTERNAL_CAPITALISED_INTEREST_RECEIVED = accounts.INTERNAL_CAPITALISED_INTEREST_RECEIVED
INTERNAL_CAPITALISED_PENALTIES_RECEIVED = accounts.INTERNAL_CAPITALISED_PENALTIES_RECEIVED
INTERNAL_PENALTY_INTEREST_RECEIVED = accounts.INTERNAL_PENALTY_INTEREST_RECEIVED
INTERNAL_EARLY_REPAYMENT_FEE_INCOME = accounts.INTERNAL_EARLY_REPAYMENT_FEE_INCOME
INTERNAL_LATE_REPAYMENT_FEE_INCOME = accounts.INTERNAL_LATE_REPAYMENT_FEE_INCOME
INTERNAL_OVERPAYMENT_FEE_INCOME = accounts.INTERNAL_OVERPAYMENT_FEE_INCOME
INTERNAL_UPFRONT_FEE_INCOME = accounts.INTERNAL_UPFRONT_FEE_INCOME
INTERNAL_ACCRUED_INTEREST_RECEIVABLE = accounts.INTERNAL_ACCRUED_INTEREST_RECEIVABLE

internal_accounts_tside = {
    "TSIDE_ASSET": [
        INTERNAL_ACCRUED_INTEREST_RECEIVABLE,
        INTERNAL_CAPITALISED_INTEREST_RECEIVABLE,
    ],
    "TSIDE_LIABILITY": [
        INTERNAL_INTEREST_RECEIVED,
        INTERNAL_CAPITALISED_INTEREST_RECEIVED,
        INTERNAL_CAPITALISED_PENALTIES_RECEIVED,
        INTERNAL_PENALTY_INTEREST_RECEIVED,
        INTERNAL_EARLY_REPAYMENT_FEE_INCOME,
        INTERNAL_LATE_REPAYMENT_FEE_INCOME,
        INTERNAL_OVERPAYMENT_FEE_INCOME,
        INTERNAL_UPFRONT_FEE_INCOME,
    ],
}
