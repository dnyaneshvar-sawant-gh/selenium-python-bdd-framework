import os
import time

from behave import *

from pageObjects.AddToCart import AddToCartPage

use_step_matcher("re")

@when('User adds "(?P<product_name>.+)" to the cart')
def step_impl(context, product_name):
    AddToCartPage.click_add_to_cart(context, product_name)
    time.sleep(1)

@then('Validate Cart icon should show "(?P<value>.+)" item')
def step_impl(context, value):
    count=AddToCartPage.get_cart_item_count(context)
    assert count ==value;


@step('Validate "(?P<button>.+)" button should be visible for "(?P<product_name>.+)"')
def step_impl(context, button, product_name):
    add_to_cart = AddToCartPage(context.driver)
    add_to_cart.click_cart_option()
    time.sleep(1)
    actual_button=add_to_cart.check_remove_button(product_name)
    assert actual_button==button;


@when('User adds the following items to the cart')
def add_multiple_products(context):
    add_to_cart = AddToCartPage(context.driver)
    for row in context.table:
        product = row['Product Name']
        add_to_cart.click_add_to_cart(product)


@then('User Remove "(?P<product_name>.+)" from the cart')
def remove_item(context,product_name):
    add_to_cart = AddToCartPage(context.driver)
    add_to_cart.click_cart_option()
    time.sleep(1)
    add_to_cart.click_remove(product_name)


