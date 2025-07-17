Feature: Test Login functionality

  Background: User Navigate to SauceDemo application
    Given User launches the browser and opens the application

  @login @ValCredentials
  Scenario Outline: Successful login with valid credential "<TC_NO>"
    Given User Enter "<username>" and "<password>" and clicks on login
    And Validate Successful login
    Then User Logout from the Application

    Examples:
      | TC_NO | username      | password     |
      | TC_01 | standard_user | secret_sauce |
      | TC_02 | problem_user  | secret_sauce |
      | TC_03 | error_user    | secret_sauce |
      | TC_04 | visual_user   | secret_sauce |

  @login @InvalidCredentials
  Scenario Outline: Successful login with Invalid credential "<TC_NO>"
    Given User Enter "<username>" and "<password>" and clicks on login
    And Validate Error Message as "<expected_error>"

    Examples:
      | TC_NO | username        | password     | expected_error                                                            |
      | TC_01 | standard_user   | secret123    | Epic sadface: Username and password do not match any user in this service |
      | TC_02 | standard        | secret_sauce | Epic sadface: Username and password do not match any user in this service |
      | TC_03 | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.                       |
      | TC_03 | ""             | secret_sauce | Epic sadface: Username is required                                        |
      | TC_05 | standard_user   | ""           | Epic sadface: Password is required                                        |
      | TC_06 | ""              | ""           | Epic sadface: Username is required                                        |