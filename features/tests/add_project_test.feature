Feature: Add project test

  Scenario: User can add a project through the settings
    Given Open Reelly main page
    When Enter email fgin86@gmail.com
    And Enter password Alexey1986!
    And Click setting butn
    And Click add project butn
    Then Verify add-a-project page opens
    When Email input mariyagin@gmail.com
    When Enter phone +19172242120
    Then Verify application buttn is available and clickable




#Feature: # Enter feature name here
  # Enter feature description here

  #Scenario: # Enter scenario name here
    # Enter steps here