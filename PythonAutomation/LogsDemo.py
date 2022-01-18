from PythonAutomation.AllDataVariable import AllDataVariable


class LogsLearning(AllDataVariable):
    ALD = AllDataVariable()
    Str1 = "Nikhil"
    Str2 = "Mathur"
    Logs = ALD.getlogs()
    if Str1 == Str2:
        Logs.info("String Match")
    else:
        Logs.error("String not matched")

