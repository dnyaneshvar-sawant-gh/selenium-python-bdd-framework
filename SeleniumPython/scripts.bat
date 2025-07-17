@echo off
setlocal

:: === Configuration ===
set TAG=@RemoveProduct
set BROWSER_NAME=chrome
set CLEAR_REPORT=yes
set CLEAR_SCREENSHOT=yes

:: === Paths ===
set REPORT_BASE=reports
set ALLURE_RESULTS_DIR=%REPORT_BASE%\allure-results
set ALLURE_REPORT_DIR=%REPORT_BASE%\allure-report
set SCREENSHOT_DIR=screenshots

:: === Export Environment Variables ===
set BROWSER_NAME=%BROWSER_NAME%
set CLEAR_REPORT=%CLEAR_REPORT%

:: === Clear old reports if enabled ===
if /I "%CLEAR_REPORT%"=="yes" (
    echo [INFO] Clearing old report files...
    if exist %REPORT_BASE% (
        rmdir /S /Q %REPORT_BASE%
    )
    mkdir %REPORT_BASE%
    mkdir %ALLURE_RESULTS_DIR%
) else (
    if not exist %ALLURE_RESULTS_DIR% (
        mkdir %ALLURE_RESULTS_DIR%
    )
)

:: === Clear screenshots if enabled ===
if /I "%CLEAR_SCREENSHOT%"=="yes" (
    echo [INFO] Clearing screenshots in '%SCREENSHOT_DIR%'...
    if exist %SCREENSHOT_DIR% (
        del /Q %SCREENSHOT_DIR%\*
    )
)

:: === Run Behave tests with Allure ===
echo [INFO] Running Behave tests with tag %TAG% on browser: %BROWSER_NAME%
behave --no-capture --no-skipped -f allure_behave.formatter:AllureFormatter -o %ALLURE_RESULTS_DIR% -t %TAG%

:: === Generate Report ===
echo [INFO] Generating Allure report...
allure generate %ALLURE_RESULTS_DIR% --clean -o %ALLURE_REPORT_DIR%
if %ERRORLEVEL% EQU 0 (
    echo [INFO] Allure report generated successfully.
) else (
    echo [WARNING] Report generated with errors or incomplete results.
)

:: === Open Allure Report ===
echo [INFO] Opening Allure report in default browser...
allure open %ALLURE_REPORT_DIR%

echo.
echo [INFO] Test execution completed. Press any key to close this window.
pause
endlocal
