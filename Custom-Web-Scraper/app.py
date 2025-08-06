from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


def init():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://rcdb.com/")

    driver.close()
    driver.quit()


def scrape():
    name = driver.find_element(By.XPATH, value="//*[@id=\"rrc_text\"]/p[1]/a").text
    park = driver.find_element(By.XPATH, value="//*[@id=\"rrc_text\"]/p[2]/a").text
    location = driver.find_element(by=By.XPATH, value="//*[@id=\"rrc_text\"]/p[3]/a[1]").text
    status = driver.find_element(by=By.XPATH, value="//*[@id=\"rrc_text\"]/p[4]").text
    height = driver.find_element(by=By.XPATH, value="//*[@id=\"rrc_text\"]/p[4]").text
    roller_coaster = {
        "Roller Coaster": name,
        "Park": park,
        "Location": location,
        "Status": status,
        "Height": f"{height} ft"
    }
    return roller_coaster


def write_to_file(roller_coaster):
    with open("resources/random_roller_coaster.csv", "w") as f:
        f.write(
            f"Roller Coaster: {roller_coaster['name']}\n"
            f"Park: {roller_coaster['park']}\n"
            f"Location: {roller_coaster['location']}\n"
            f"Status: {roller_coaster['status']}\n"
            f"Height: {roller_coaster['height']} ft"
        )

def write_to_csv(file):
    df = pd.read_fwf(file)
    df.to_csv('resources/roller_coaster.csv')


def main():
    init()
    roller_coaster = scrape()
    write_to_file(roller_coaster)
    write_to_csv("resources/random_roller_coaster.csv")

main()

