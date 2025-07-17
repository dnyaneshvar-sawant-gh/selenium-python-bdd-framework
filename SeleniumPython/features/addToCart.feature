Feature: Test add to cart functionality

  Background: User Navigate to SauceDemo application
    Given User launches the browser and opens the application

  @addToCart @SingleProduct
  Scenario: Add a single item to the cart
    Given User Enter "standard_user" and "secret_sauce" and clicks on login
    When User adds "Sauce Labs Bike Light" to the cart
    Then Validate Cart icon should show "1" item
    And Validate "Remove" button should be visible for "Sauce Labs Bike Light"

  @addToCart @MultipleProducts
  Scenario: Add a multiple item to the cart
    Given User Enter "standard_user" and "secret_sauce" and clicks on login
    When User adds the following items to the cart
      | Product Name            |
      | Sauce Labs Backpack     |
      | Sauce Labs Bike Light   |
      | Sauce Labs Bolt T-Shirt |
    Then Validate Cart icon should show "3" item
    And Validate "Remove" button should be visible for "Sauce Labs Backpack"
    And Validate "Remove" button should be visible for "Sauce Labs Bike Light"
    And Validate "Remove" button should be visible for "Sauce Labs Bolt T-Shirt"

  @addToCart @RemoveProduct
  Scenario: Add and Remove item from the cart
    Given User Enter "standard_user" and "secret_sauce" and clicks on login
    When User adds "Sauce Labs Bike Light" to the cart
    Then Validate Cart icon should show "1" item
    Then User Remove "Sauce Labs Bike Light" from the cart
    Then Validate Cart icon should show "0" item