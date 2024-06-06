import re 
import pytest
from playwright.sync_api import Page,expect
from configuration_properties import go_to_amazon,negative_login


def test_get_started_link(page:Page):
   
    # Expects page to have a heading with the name of installation
    expect(page.locator("css=[type='submit']")).to_be_visible()

