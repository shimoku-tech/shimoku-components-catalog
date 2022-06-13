"""HTML beautiful components"""

from typing import Optional
from re import sub


def create_h1_title(title: str, subtitle: str) -> str:
	title_style: str = sub(r"\s+", '', title)
	return (
		f"<head>"
		f"<style>.{title_style}{{height:100%; width:100%; border-radius:16px; padding:16px; background-color:#FAFAFB; color:#4C72F9;}}</style>"
		f"<style>.base{{color:#202A36;}}</style>"
		f"</head>"
		f"<div class={title_style}>"
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


def box_with_button(
		href: str, title: str, line: str,
		background: Optional[str] = None,
		button_text: str = 'Visit now',
) -> str:
	if not background:
		background = 'https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?ixlib=rb-1.2.1&raw_url=true&q=80&fm=jpg&crop=entropy&cs=tinysrgb&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3000'

	return (
		f"<head>"
		f"<style>.rectangle"
		f"{{height:350px; width:100%; border-radius:8px; padding:24px;"
		f"background-size: cover;"
		f"background-image: url('{background}');"
		f"color:#FFFFFF;}}"
		f"</style>"
		f"<style>.button"
		f"{{display: inline-block; position: absolute; background-color: var(--color-white);"
		f"bottom: 10%; padding: 2% 10%; border-radius: var(--border-radius-m);"
		f"font-size: 14px; color: var(--chart-C1); box-shadow: var(--box-shadow-m); transition-duration: 0.3s;}}"
		f".button:hover{{background-color: var(--chart-C1); color: var(--color-white);}}"
		f"</style>"
		f"</head>"
		f"<div class='rectangle'>"
		f"<h1>{title}</h1>"  # Title
		f"<p>{line}</p>"  # Li 1
		f"<a href='{href}' target='_blank'>"  # link button
		f"<div class='button'>{button_text}</div>"  # Text button
		f"</a>"
		f"</div>"
	)
