# features
import library.features.common.fetchers as fetchers
import library.features.v4.common.interest_accrual_common as interest_accrual_common

# Events
ACCRUAL_EVENT = interest_accrual_common.ACCRUAL_EVENT
ACCRUED_INTEREST_RECEIVABLE = interest_accrual_common.ACCRUED_INTEREST_RECEIVABLE

event_types = interest_accrual_common.event_types
scheduled_events = interest_accrual_common.scheduled_events

# Fetchers
data_fetchers = [fetchers.EOD_FETCHER]

# Parameters
PARAM_DAYS_IN_YEAR = interest_accrual_common.PARAM_DAYS_IN_YEAR
PARAM_ACCRUAL_PRECISION = interest_accrual_common.PARAM_ACCRUAL_PRECISION
INTEREST_ACCRUAL_PREFIX = interest_accrual_common.INTEREST_ACCRUAL_PREFIX
PARAM_INTEREST_ACCRUAL_HOUR = interest_accrual_common.PARAM_INTEREST_ACCRUAL_HOUR
PARAM_INTEREST_ACCRUAL_MINUTE = interest_accrual_common.PARAM_INTEREST_ACCRUAL_MINUTE
PARAM_INTEREST_ACCRUAL_SECOND = interest_accrual_common.PARAM_INTEREST_ACCRUAL_SECOND

schedule_parameters = interest_accrual_common.schedule_parameters
accrual_parameters = interest_accrual_common.accrual_parameters