from behave import *
from selenium import webdriver
import time

@given('I Luch Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I Open Rokomari Browser')
def step_impl(context):
    context.driver.get('https://www.rokomari.com/book')


@when('Assert Logo')
def step_impl(context):
    logo = context.driver.find_element_by_xpath('//*[@id="js--main-header"]/div/div/div[1]/div/a/img').is_displayed()
    assert logo is True


@when('Scrolldown')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@when('Assert Copyright Text')
def step_impl(context):
    copyright = context.driver.find_element_by_xpath('/html/body/footer/div[4]/p').text
    assert copyright == "© 2012-2021 Rokomari.com"


@then('Close Browser')
def step_impl(context):
    context.driver.close()


