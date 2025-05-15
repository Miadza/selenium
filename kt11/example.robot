***Settings***
Library           SeleniumLibrary

***Variables***
${URL}             https://www.saucedemo.com/
${USERNAME}        standard_user
${PASSWORD}        secret_sauce

***Test Cases***
Login with Valid Credentials
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    Title Should Be    Swag Labs
    Close Browser

Login with Invalid Credentials
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      locked_out_user
    Input Text      id:password       secret_sauce
    Click Element   id:login-button
    ${error_message_locator} =    Set Variable    xpath=//h3[text()='Epic sadface: Username and password do not match any user in this demo account']
    Wait Until Element Is Visible    ${error_message_locator}    timeout=10
    Element Should Be Visible    ${error_message_locator}
    Close Browser

Add Item to Cart
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    Click Button    id:add-to-cart-sauce-labs-backpack
    Element Should Be Visible    xpath=//span[@class='shopping_cart_badge' and text()='1']
    Close Browser

Remove Item from Cart
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    Click Button    id:add-to-cart-sauce-labs-backpack
    Click Button    id:remove-sauce-labs-backpack
    Element Should Not Be Visible    xpath=//span[@class='shopping_cart_badge' and text()='1']
    Close Browser

Verify Item Details Page
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    ${item_link_locator} =    Set Variable    xpath=//div[@class='inventory_item'][1]//a[@id='item_4_img_link']
    Wait Until Element Is Visible    ${item_link_locator}    timeout=10
    Click Element    ${item_link_locator}
    Page Should Contain    Sauce Labs Backpack
    Close Browser

Sort Items by Price (Low to High)
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    Select From List By Value    css:.product_sort_container    lohi
    ${first_item_price}=    Get Text    xpath=//div[@class='inventory_item'][1]//div[@class='inventory_item_price']
    Should Contain    ${first_item_price}    $7.99
    Close Browser

Checkout Process (Simple)
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    Click Button    id:add-to-cart-sauce-labs-backpack
    Click Element   id:shopping_cart_container
    Click Element   id:checkout
    Input Text      id:first-name      Test
    Input Text      id:last-name       User
    Input Text      id:postal-code     12345
    Click Element   id:continue
    ${checkout_overview_locator} =    Set Variable    xpath=//span[text()='Checkout: Overview']
    Wait Until Element Is Visible    ${checkout_overview_locator}    timeout=10
    Element Should Be Visible    ${checkout_overview_locator}
    Close Browser

Verify Logout
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    Click Element   id:react-burger-menu-btn
    Click Element   id:logout_sidebar_link
    Element Should Be Visible    id:login-button
    Close Browser

Check Product Image Load
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    Element Should Be Visible    xpath=//img[@alt='Sauce Labs Backpack']
    Close Browser

Verify Reset App State
    Open Browser    ${URL}    firefox
    Input Text      id:user-name      ${USERNAME}
    Input Text      id:password       ${PASSWORD}
    Click Element   id:login-button
    Click Button    id:add-to-cart-sauce-labs-backpack
    Click Element   id:react-burger-menu-btn
    Click Element   id:reset_sidebar_link
    Element Should Not Be Visible    xpath=//span[@class='shopping_cart_badge']
    Close Browser