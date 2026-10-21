from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://uae.dubizzle.com/motors/new-cars/mercedes-benz/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(10000)

    content = page.content()

    print("PAGE LENGTH:", len(content))

    if "Pardon Our Interruption" in content:
        print("BLOCKED_BY_IMPERVA")
    elif "Mercedes-Benz" in content:
        print("SUCCESS")
    else:
        print("UNKNOWN_RESPONSE")

    print(content[:5000])

    browser.close()
