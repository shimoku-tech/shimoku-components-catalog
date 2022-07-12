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


def panel(
		href: str, text: str, button_panel: str = 'Read more',
		symbol_name: str = 'insights',
) -> str:
	return (
		"<head>"
		# Import icons from g fonts
		f"<link rel='stylesheet'"
		"href='https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0' />"
		# Start styles BG
		"<style>.panel"
		"{display: inline-grid; position: relative;"
		"height: 100%; width:100%; border-radius: var(--border-radius-m); padding:16px;"
		"grid-auto-flow: column; align-items: center;"
		"background-color: var(--color-primary); opacity: 0.7;"  # Change BG panel color
		"color: var(--color-white);}"  # Change text panel color
		"</style>"
		# End styles BG
		# Start icons style
		"<style>.material-symbols-rounded"
		"{display: inline-grid; position: relative;"
		"color: var(--color-white);}"
		"</style>"
		# End icons style
		# Start styles text
		"<style>.text-panel"
		"{display: inline-grid; position: relative; width:100%;"
		"font-size: 14px;"
		"padding-left: 16px;"
		"color:var(--color-white);}"
		"</style>"
		# End styles text
		# Start styles button
		"<style>.button-panel"
		"{display: inline-grid; position: relative;"
		"padding: 8px 16px; border-radius: var(--border-radius-m);"
		"background-color: var(--color-white);"  # Change BG button color
		"font-size: 14px; color: var(--color-primary);"  # Change text button color
		"box-shadow: var(--box-shadow-m); transition-duration: 0.3s;}"
		".button-panel:hover{background-color: var(--color-primary);"  # Change BG button hover color
		"color: var(--color-white);}"  # Change text button hover color
		"</style>"
		# End styles button
		"</head>"
		"<div class='panel'>"
		f"<span class='material-symbols-rounded'>{symbol_name}</span>"  # Search icon name on https://fonts.google.com/icons?icon.style=Rounded
		f"<p class='text-panel'>{text}</p>"  # Text panel
		f"<a href='{href}' target='_blank'>"  # link button
		f"<div class='button-panel'>{button_panel}</div>"  # Text button
		"</a>"
		"</div>"
	)


def not_found(image: Optional[str] = None) -> str:
	if not image:
		image = (
			'https://uploads-ssl.webflow.com/619f9fe98661d321dc3beec7/62cc28b5c21a8d0f1dbbdccc_illus-not-found-line.svg'
		)
	return (
		f"<head>"
		# Start styles BG
		f"<style>.bg-not-found"
		f"{{height: 50vh; width: 100%; border-radius: var(--border-radius-m);"
		f"margin-top: 16px;"
		f"margin-bottom: 32px;"
		f"display: flex;"
		f"justify-content: center;"
		f"align-items: center;"
		f"background-size: auto;"
		f"background-position: center;"
		f"background-repeat: no-repeat;"
		f"background-color: var(--color-grey-100);"
		f"background-image: url('{image}');"
		f"color: var(--color-white);}}"
		f"</style>"
		# End styles BG
		f"<link rel='stylesheet'"
		f"href='https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0'/>"
		# Star hint
		f"<style>.hint"
		f"{{display: flex; position: relative;"
		f"height: 100%; width:100%; border-radius: var(--border-radius-m); padding:16px;"
		f"grid-auto-flow: column; align-items: center;"
		f"background-color: var(--color-warning); opacity: 0.7;"  # Change BG color
		f"color: var(--color-white);}}"  # Change Text color
		f"</style>"
		# Start icons style
		f"<style>.material-symbols-rounded"
		f"{{display: flex; position: relative;"
		f"opacity: 1;"
		f"color: var(--color-white);}}"
		f"</style>"
		# End icons style
		# Start styles text
		f"<style>.title-hint"
		f"{{display: flex; position: relative; width:100%;"
		f"padding-left: 16px;"
		f"opacity: 1;"
		f"color:var(--color-white);}}"
		f"</style>"
		f"<style>.text-hint"
		f"{{display: flex; position: relative; width:100%;"
		f"font-size: 14px;"
		f"padding-left: 16px;"
		f"opacity: 1;"
		f"color:var(--color-white);}}"
		f"</style>"
		# End hint
		f"</head>"
		f"<div class='bg-not-found'>"
		f"</div>"
		f"<div class='hint'>"
		f"<span class='material-symbols-rounded'>info</span>"  # Change icon on https://fonts.google.com/icons?icon.style=Rounded
		f"<div>"
		f"<h3 class='title-hint'>Not found</h3>"
		f"<p class='text-hint'>The page you’re looking for doesn't exist. Try to navigate to another page instead.</p>"  # Text hint
		f"</div>"
		f"</div>"
	)

