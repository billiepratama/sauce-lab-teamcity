# Created by Billie Pratama at 11/19/2020
Feature: Test if the reward detail screen is displayed
#  PST-8 : Handle Stamp Card Section
  Scenario: Display three sections in rewards page
    Given I am in the login page
    And Enter the credentials
    When Click Rewards button
    And Pull the screen to refresh
    Then Three sections will be displayed : Stamp Card, Voucher, Referral Section
