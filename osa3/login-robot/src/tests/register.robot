*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command 
    Create User  pekka  pekka123

Register With Already Taken Username And Valid Password
    Input New Command
    Run Keyword And Expect Error  User with username kalle already exists  Create User  kalle  kalle123

Register With Too Short Username And Valid Password
    Input New Command
    Run Keyword And Expect Error  Username is too short  Create User  ka  kalle123

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Run Keyword And Expect Error  Invalid username  Create User  kalle?  kalle123

Register With Valid Username And Too Short Password
    Input New Command
    Run Keyword And Expect Error  Password is too short  Create User  pekka  kalle12

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Run Keyword And Expect Error  Invalid password  Create User  pekka  kalleyksi

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123