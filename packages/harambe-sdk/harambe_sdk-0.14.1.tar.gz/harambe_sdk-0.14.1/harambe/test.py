
import asyncio
from typing import Any, Optional

from playwright.async_api import Page, ElementHandle

from harambe import SDK


async def scrape(sdk: SDK, current_url: str, *args: Any, **kwargs: Any) -> None:
    page: Page = sdk.page
    await page.wait_for_load_state('networkidle')
    await page.wait_for_selector("div#dependents > div.Box")
    link_elements = await page.query_selector_all(
        "div.Box-row.d-flex.flex-items-center > span > a"
    )
    for i in range(0, len(link_elements), 2):
        username_link = await link_elements[i].get_attribute("href")
        project_link = await link_elements[i + 1].get_attribute("href")
        await sdk.save_data(
            {
                "username_link": "https://github.com" + username_link,
                "project_link": "https://github.com" + project_link,
            }
        )

    async def pager() -> Optional[str | ElementHandle]:
        next_page_link = await page.query_selector(
            "div.paginate-container > div.BtnGroup > a.btn.BtnGroup-item:nth-child(2)"
        )
        print(await next_page_link.inner_text())
        if next_page_link and "Next" in await next_page_link.inner_text():
            return await next_page_link.get_attribute("href")

    await sdk.paginate(pager)


if __name__ == "__main__":
    asyncio.run(SDK.run(scrape, "https://github.com/microsoft/autogen/network/dependents", {}))
