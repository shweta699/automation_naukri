from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# Load credentials from .env file
load_dotenv()
email = os.getenv("NAUKRI_EMAIL")
password = os.getenv("NAUKRI_PASSWORD")
job_title = os.getenv("JOB_TITLE")
job_location = os.getenv("JOB_LOCATION")
experience = os.getenv("EXPERIENCE")
salary = os.getenv("SALARY")

print("✅ Credentials Loaded Successfully!")
print(f"Email: {email}")
print(f"Password: {password}")  # Avoid printing passwords in real projects
print(f"Job Titles: {job_title}")
print(f"Job Locations: {job_location}")
print(f"Experience: {experience} years")
print(f"Salary: ₹{salary}")
def apply_for_jobs():
    print("🚀 Starting Job Application Process...")

    # Set up Chrome WebDriver using WebDriver Manager
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Open Chrome in full screen
    driver = webdriver.Chrome(service=service, options=options)

    wait = WebDriverWait(driver, 15)

    # Step 1: Open Naukri Login Page
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    try:
        # Enter login credentials
        username = wait.until(EC.presence_of_element_located((By.ID, "usernameField")))
        username.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "passwordField")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        print("✅ Logged into Naukri successfully!")
        time.sleep(5)

    except Exception as e:
        print(f"⚠️ Error during login: {e}")
        driver.quit()
        return

# Step 2: Search for Jobs
    driver.get("https://www.naukri.com/")
    time.sleep(5)  # Wait for the page to fully load

    try:
        # Step 1: Click on Placeholder to Activate Search Box
        placeholder = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nI-gNb-sb__placeholder")))
        placeholder.click()
        time.sleep(2)

        # Step 2: Click and Fill Job Title
        search_box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "suggestor-input")))
        search_box.click()  # Click first to activate the field
        search_box.clear()
        search_box.send_keys(job_title)
        time.sleep(2)
        search_box.send_keys(Keys.TAB)  # Move to the next field

        # Step 3: Click and Select Experience Level
# Step 3: Click and Select Experience Level
        experience_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "experienceDD")))
        experience_dropdown.click()  # Click to open dropdown
        time.sleep(2)  # Wait for the dropdown to appear

        # Wait for the dropdown options container to load
        dropdown_options = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nI-gNb-sb__expDD")))

        # Find all experience options
        exp_options = dropdown_options.find_elements(By.TAG_NAME, "li")

        # Clean experience string (removing "years" if mistakenly present in .env file)
        experience_number = experience.split()[0]  # Get only the number (e.g., "3" from "3 years")
        experience_str = f"{experience_number} years" if experience_number != "1" else "1 year"

        # Loop through options and select the correct one
        for option in exp_options:
            spans = option.find_elements(By.TAG_NAME, "span")  # Get all <span> elements inside <li>
            
            for span in spans:  # Check all <span> elements inside each <li>
                if experience_str in span.text.strip():  # Match with text
                    option.click()
                    print(f"✅ Selected Experience Level: {experience_number} years")
                    break
            else:
                continue
            break
        else:
            print("⚠️ Experience level not found, selecting default (Fresher).")
            exp_options[0].click()  # Select first option as fallback

        time.sleep(2)


        # Step 4: Click and Enter Location

        location_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter location']")))
        location_box.click()  # Click inside the input field
        location_box.clear()  # Clear any pre-filled text
        location_box.send_keys(job_location)
        time.sleep(2)
        location_box.send_keys(Keys.TAB)  # Move to the next field


        # Step 5: Click the Search Button
       # Step 5: Click the Search Button
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'nI-gNb-sb__icon-wrapper')]")))
        search_button.click()
        time.sleep(5)  # Wait for search results

        print(f"🔍 Searching for {job_title} jobs in {job_location}")

    except Exception as e:
        print(f"⚠️ Error during job search: {e}")
        driver.quit()
        return

        # Apply filters for Experience & Salary
    #     try:
    #         exp_filter = wait.until(EC.presence_of_element_located((By.XPATH, f"//label[@for='exp-{experience}']")))
    #         exp_filter.click()
    #         time.sleep(2)
    #         print(f"✅ Applied experience filter: {experience} years")

    #         salary_filter = wait.until(EC.presence_of_element_located((By.XPATH, f"//label[@for='sal-{salary}']")))
    #         salary_filter.click()
    #         time.sleep(2)
    #         print(f"✅ Applied salary filter: {salary} INR")
    #     except Exception as e:
    #         print(f"⚠️ Experience or salary filter not found, skipping... {e}")

    # except Exception as e:
    #     print(f"⚠️ Error during job search: {e}")
    #     driver.quit()
    #     return

        # Step 3: Apply to Jobstry:
# Apply to jobs (max 5 jobs)
# Apply to jobs (max 5 jobs)
    # Apply to jobs (max 5 jobs)
# Define your questions and answers
    applied_jobs = []
    predefined_questions = [
        "What is your highest qualification?",
        "How many years of experience do you have?",
        "What is your current salary?",
        "How many years of experience do you have in Python Development?"
    ]

    predefined_answers = [
        "Bachelor's Degree",  # Answer for the first question
        "2 years",           # Answer for the second question
        "800000",
        "yes"             # Answer for the third question
    ]

        # Apply to jobs (max 5 jobs)
# Apply to jobs (max 50 jobs)
    try:
        job_links = driver.find_elements(By.CLASS_NAME, "title")
        applied_count = 0
        max_jobs = 5000  # Change this to apply for more jobs
        applied_jobs = []

        for job in job_links[:max_jobs]:
            try:
                job_name = job.text.strip()  # Get the job name
                job.click()  # Click the job link
                time.sleep(2)

                # Switch to the new tab
                driver.switch_to.window(driver.window_handles[1])

                # Check if already applied
                already_applied = driver.find_elements(By.ID, "already-applied")
                if already_applied:
                    print(f"⚠️ Already applied for {job_name}, skipping.")
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    continue

                # Wait for the Apply button to be clickable
                wait = WebDriverWait(driver, 10)
                apply_btn = wait.until(EC.element_to_be_clickable((By.ID, 'apply-button')))

                # Click the Apply button using JavaScript
                driver.execute_script("arguments[0].click();", apply_btn)
                time.sleep(3)  # Wait for application confirmation

                # Handle pop-up questions if they appear
                try:
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "botItem chatbot_ListItem")))  # Wait for pop-up

                    question_elements = driver.find_elements(By.CLASS_NAME, "botMsg msg")  # Find questions

                    for question_element in question_elements:
                        question_text = question_element.text.strip()
                        print(f"❓ Question: {question_text}")

                        if question_text in predefined_questions:
                            index = predefined_questions.index(question_text)
                            predefined_answer = predefined_answers[index]

                            # Answer input fields
                            answer_field = question_element.find_element(By.XPATH, ".//following-sibling::input")
                            if answer_field:
                                answer_field.send_keys(predefined_answer)
                                print(f"✅ Answered: {predefined_answer}")

                        else:
                            # Select "Yes" for radio button questions
                            radio_buttons = question_element.find_elements(By.XPATH, ".//input[@type='radio']")
                            for radio in radio_buttons:
                                if radio.get_attribute("value") == "Yes":
                                    radio.click()
                                    print("✅ Selected: Yes")
                                    break

                    # Click the submit button for the pop-up
                    submit_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-button-class-name")))
                    submit_button.click()
                    time.sleep(3)

                except Exception:
                    print(f"⚠️ No pop-up questions for {job_name}, proceeding.")

                # ✅ Move count update and CSV addition here (works even if no pop-up)
                applied_jobs.append({"Company": job_name, "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                applied_count += 1
                print(f"✅ Successfully applied for job {applied_count}: {job_name}")

            except Exception as e:
                print(f"⚠️ Error during job application for {job_name}: {e}")

            finally:
                # Close the current job tab and switch back to the original tab
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            # Stop applying if max count is reached
            if applied_count >= max_jobs:
                break

        print(f"✅ Successfully applied for {applied_count} jobs.")

        # Save applied jobs to a CSV file
        if applied_jobs:
            file_exists = os.path.isfile("applied_jobs.csv")  # Check if file already exists
            df = pd.DataFrame(applied_jobs)
            df.to_csv("applied_jobs.csv", mode="a", index=False, header=not file_exists)
            print("✅ Applied jobs saved to applied_jobs.csv")
        else:
            print("⚠️ No jobs were applied for, nothing to save.")

    except Exception as e:
        print(f"⚠️ Error while applying for jobs: {e}")

        

    # Step 4: Close Browser
    driver.quit()
    

# Run the script immediately to test
apply_for_jobs()
