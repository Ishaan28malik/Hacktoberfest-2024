# GOOGLE Spelling Suggestion (Did you mean?) Example

import google

#  You can retrieve you license key here: https://code.google.com/
google.LICENSE_KEY = '...'

phrase = 'I said something wring'

did_you_mean = google.doSpellingSuggestion(phrase, license_key=None, http_proxy=None)

# Did you mean..
# I said something *wrong*
print(did_you_mean)
