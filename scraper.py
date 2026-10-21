from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://uae.dubizzle.com/motors/new-cars/mercedes-benz/",
        wait_until="networkidle"
    )

    content = page.content()

    print("PAGE LENGTH:", len(content))

    if "Pardon Our Interruption" in content:
        print("BLOCKED_BY_IMPERVA")
    elif "Mercedes-Benz" in content:
        print("SUCCESS")
    else:
        print("UNKNOWN_RESPONSE")

    browser.close()
