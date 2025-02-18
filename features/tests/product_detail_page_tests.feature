
Feature: Off plan feature tests


  Scenario: User can open product detail and see three options of visualization
    Given Open Reelly main page
    When Enter email fgin86@gmail.com
    And Enter password Alexey1986!
    And Click on off-plan butn at the left side menu
    When Click on off_plan product
    Then Verify option “architecture”, “interior”, “lobby” are present and clickable
