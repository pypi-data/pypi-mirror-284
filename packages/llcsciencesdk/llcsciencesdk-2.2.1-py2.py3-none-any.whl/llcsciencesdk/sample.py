from llcsciencesdk.llc_api import ScienceSdk

llc_api = ScienceSdk(environment="production")
llc_api.login("username", "password")
sample = llc_api.llc_analyzer({})
print(sample)
