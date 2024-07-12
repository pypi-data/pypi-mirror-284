import asyncio
from typing import Any

from playwright.async_api import Page

from harambe import SDK, Schemas


async def scrape(sdk: SDK, current_url: str, *args: Any, **kwargs: Any) -> None:
    page: Page = sdk.page
    await page.wait_for_selector('ul > li.css-1q2dra3')
    faculty_rows = await page.query_selector_all('ul > li.css-1q2dra3')
    for row in faculty_rows:
        title_element = await row.query_selector("a.css-19uc56f")
        if title_element:
            await title_element.click()
            await page.wait_for_timeout(3000)
        await page.wait_for_selector('.css-oplht1')
        job_id_element = await row.query_selector(".css-14a0imc > .css-h2nt8k")
        job_description_element = await page.query_selector(".css-oplht1")
        locations_elements = await page.query_selector_all('.css-k008qs > dl:has(dt:has-text("locations")) > .css-129m7dg')
        date_posted_element = await row.query_selector('.css-k008qs > dl:has(dt:has-text("posted")) > dd.css-129m7dg')
        apply_url_element = await page.query_selector("a.css-rlib17") #Get attribute href
        employment_type_element = await page.query_selector('.css-k008qs > dl:has(dt:has-text("time")) > dd.css-129m7dg')
        job_id = await job_id_element.inner_text() if job_id_element else None
        title = await title_element.inner_text() if title_element else None
        job_description = await job_description_element.text_content() if job_description_element else None
        locations = [await x.inner_text() for x in locations_elements if x]
        sub_points = job_description.split("\xa0")
        sub_points = [x for x in sub_points if x.strip()]
        qualifications = [x for x in sub_points if "qualifications" in x][0] if [x for x in sub_points if "qualifications" in x] else None
        skills = [x for x in sub_points if "Skills" in x][0] if [x for x in sub_points if "Skills" in x] else None
        preferred_skills = [x for x in sub_points if "Additional qualifications" in x][0] if [x for x in sub_points if "Additional qualifications" in x] else None
        job_benefits = [x for x in sub_points if "benefits" in x.lower()][0] if [x for x in sub_points if "benefits" in x.lower()] else None
        date_posted = await date_posted_element.inner_text() if date_posted_element else None
        apply_url = await apply_url_element.get_attribute("href") if apply_url_element else None
        employment_type = await employment_type_element.inner_text() if employment_type_element else None
        close_button = await page.query_selector("#jobDetailsCloseButton")
        await close_button.click()
        await page.wait_for_timeout(1000)
        await sdk.save_data(
            {
                "job_id": job_id,
                "department": None,
                "title": title,
                "job_description": job_description,
                "locations": locations,
                "job_type": None,
                "date_posted": date_posted,
                "apply_url": apply_url,
                "job_benefits": job_benefits,
                "qualifications": qualifications,
                "preferred_skills": preferred_skills,
                "skills": skills,
                "recruiter_email": None,
                "application_deadline": None,
                "language": "English",
                "employment_type": employment_type,
                "tags": [],
            }
        )

    async def pager():
        next_page_link = await page.query_selector(
            ".css-qnaoii > div > .css-1oatwy4"
        )
        return next_page_link

    await sdk.paginate(pager)

if __name__ == '__main__':
    asyncio.run(SDK.run(scrape, "https://3m.wd1.myworkdayjobs.com/en-US/Search", Schemas.job_postings))
