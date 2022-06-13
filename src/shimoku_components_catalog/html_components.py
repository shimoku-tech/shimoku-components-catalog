"""HTML beautiful components"""

from typing import Optional
from re import sub


def create_h1_title(title: str, subtitle: str) -> str:
	return (
		f"<head>"
		f"<style>.{title}{{height:100%; width:100%; border-radius:16px; padding:16px; background-color:#FAFAFB; color:#4C72F9;}}</style>"
		f"<style>.base{{color:#202A36;}}</style>"
		f"</head>"
		f"<div class={title}>"
		f"<h1>{title}</h1>"
		f"<p class='base'>"
		f"{subtitle}"
		f"</p>"
		f"</div>"
	)


def beautiful_indicator(
		title: str, background_url: Optional[str] = None,
		href: Optional[str] = None,
) -> str:
	if not background_url:
		background_url: str = (
			'https://uploads-ssl.webflow.com/619f9fe98661d321dc3beec7/62a07a6d9e984908a5aca6a1_shim-anomaly-bg-s.jpg'
		)

	title_style: str = sub(r"\s+", '', title)
	return (
		f"<head>"
		f"<style>.{title_style}{{height:121px; width:100%; border-radius:8px; padding:45px; background-position: center; background-size: cover; background-image: url('{background_url}'); color:#FFFFFF;}}</style>"
		f"</head>"
		f"<a href='{href}'>"
		f"<div class='{title_style}'>"
		f"<h3>"
		f"{title}"
		f"</h3>"
		f"</div>"
		f"</a>"

	)


def button_click_to_new_tab(title: str, background_url: str, href: Optional[str] = None) -> str:
	if not href:
		href = background_url
	return (
		f"<head>"
		f"<style>.{title}{{height:180px; width:100%; border-radius:8px; padding:24px; background-position: center; background-size: cover; background-image: url('{background_url}'); color:#FFFFFF;}}</style>"
		f"</head>"
		f"<a href='{href}' target='_blank'>"
		f"<div class={title}>"
		f"<p class='crea'>"
		f"{title}"
		f"</p>"
		f"</div>"
		f"</a>"
	)
