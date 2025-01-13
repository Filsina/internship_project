Feature: Verification page test


  Scenario:  User can click on verifications settings option and verify the right page opensEnter scenario name here
    Given Open Reelly main page
    When Enter email fgin86@gmail.com
    And Enter password Alexey1986!
    And Click setting butn
    And Click verification butn
    Then Verify URL contains verification
    Then Verify Upload image butn is present
    Then Verify Next step butn is present

