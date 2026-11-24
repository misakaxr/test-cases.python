Feature: Bank account

  Scenario: Deposit money
    Given an account with a balance of 100
    When I deposit 50
    Then the balance should be 150

  Scenario: Withdraw money
    Given an account with a balance of 100
    When I withdraw 30
    Then the balance should be 70

  Scenario: Withdraw more than the balance
    Given an account with a balance of 50
    When I try to withdraw 100
    Then I should see an insufficient funds error
    And the balance should be 50