set ANSYSEM_FEATURE_SF6694_NON_GRAPHICAL_COMMAND_EXECUTION_ENABLE=1
set ANSYSEM_FEATURE_SF159726_SCRIPTOBJECT_ENABLE=1
set RUN_UNITTESTS_ARGS=%*
set ANSYSEM_INSTALL_DIR=%ANSYSEM_ROOT221%
"%ANSYSEM_ROOT221%\ansysedt.exe" -ng -RunScriptAndExit "_unittest_ironpython\run_unittests.py"