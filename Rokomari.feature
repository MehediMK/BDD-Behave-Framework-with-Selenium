Feature: Rokomari Website

    Scenario: Logo veryfied
        Given I Luch Chrome Browser
        When I Open Rokomari Browser
        And Assert Logo
        And Scrolldown
        And Assert Copyright Text
        Then Close Browser
