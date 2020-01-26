import lldb

def flushUI(debugger, command, result, internal_dict):
    frame = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame()
    options = lldb.SBExpressionOptions()
    options.SetLanguage(lldb.eLanguageTypeObjC)
    options.SetTrapExceptions(False)
    options.SetTryAllThreads(False)
    frame.EvaluateExpression('@import UIKit', options)
    frame.EvaluateExpression("(void)[CATransaction flush]", options)
    


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f try_one.flushUI xxxx')
    print("OK for the first")