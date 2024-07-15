"""
Future use: JSON data for requests that we load from this to the cli args.

example:

--load_pattern CDS_RQ_JSON_NORM_FRESH

"""

CDS_RQ_JSON_FULL="""
{
  "use_full": true,
  "use_fresh": false,
  "mfi_flag": true,
  "balligator_flag": true,
  "talligator_flag": true,
  "quotescount": -1,
  "dropna_volume": true,
  "keep_bid_ask": true
}
"""


CDS_RQ_JSON_FULL_FRESH="""
{
  "use_full": true,
  "use_fresh": true,
  "mfi_flag": true,
  "balligator_flag": true,
  "talligator_flag": true,
  "quotescount": -1,
  "dropna_volume": true,
  "keep_bid_ask": true
}
"""

CDS_RQ_JSON_NORM_FRESH="""
{
  "use_full": false,
  "use_fresh": true,
  "mfi_flag": true,
  "balligator_flag": true,
  "talligator_flag": true,
  "quotescount": -1,
  "dropna_volume": true,
  "keep_bid_ask": true
}
"""

CDS_RQ_JSON_NORM_FRESH__NO_MFI="""
{
  "use_full": false,
  "use_fresh": true,
  "mfi_flag": false,
  "balligator_flag": true,
  "talligator_flag": true,
  "quotescount": -1,
  "dropna_volume": false,
  "keep_bid_ask": true
}
"""
