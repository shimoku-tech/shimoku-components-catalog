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
		href: str, text: str,
		button_panel: Optional[str] = None,
		symbol_name: str = 'insights',
) -> str:
	if button_panel:
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
	else:
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


def work_in_progress(image: Optional[str] = None, image_option: Optional[str] = 'animated') -> str:
	if not image:
		if image_option == 'animated':
			image = 'https://uploads-ssl.webflow.com/619f9fe98661d321dc3beec7/62c8196512d1ac5113742150_illus-work-in-chart-anim.svg'
		elif image_option == 'cone':
			image = 'https://uploads-ssl.webflow.com/619f9fe98661d321dc3beec7/62c811d712348c0fc80c12f0_img-work-in-cone.png'
		else:
			image = 'https://uploads-ssl.webflow.com/619f9fe98661d321dc3beec7/62c814c2b026f0861723e339_illus-work-in-line.svg'
	return (
		f"<head>"
		# Start styles BG
		f"<style>.bg-work-v2"
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
		f"background-color: var(--color-primary); opacity: 0.7;"  # Change BG color
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
		f"<div class='bg-work-v2'>"
		f"</div>"
		f"<div class='hint'>"
		f"<span class='material-symbols-rounded'>check_circle</span>"  # Change icon on https://fonts.google.com/icons?icon.style=Rounded
		f"<div>"
		f"<h3 class='title-hint'>Awesome</h3>"
		f"<p class='text-hint'>This page is being calculated and can take 10 hours to exist</p>"  # Text hint
		f"</div>"
		f"</div>"
	)


def go_back_button(
		note: Optional[str] = None, h1: Optional[str] = None,
		subtitle: Optional[str] = None,
) -> str:
	init_html: str = (
		f"<head>"
		f"<link rel='stylesheet'"
	    f"href='https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0' />"
		# Start styles bg
		f"<style>.head-block"
		f"{{height:100%; width:100%;"
		f"padding:24px; font-style: italic;"
		f"background: var(--color-black); "
		f"color:var(--color-white);}}"
		f"</style>"
		# End styles bg
		f"<style>.note{{font-size: 12px; color: #E6E6E6;}}</style>"  # Styles note text
		f"<style>.subtitle{{font-size: 20px; font-style: italic; color: #E6E6E6;}}</style>"  # Styles subtitle text
		# Start styles button bg
		f"<style>.button-xs"
		f"{{padding:16px; background: var(--color-grey-800);"
		f"border-radius: 8px;"
		f"display: inline-flex;"
		f"margin-bottom: 8px;"
		f"transition-duration: 0.3s;}}"
		f".button-xs:hover {{background-color: var(--color-grey-800); opacity: 0.4;}}"
		f"</style>"
		# End styles button bg
		f"</head>"
		f"<div class='head-block'>"
		f"<div class='button-xs' onclick='history.back()'>"
		f"<span class='material-symbols-rounded'>arrow_back</span>"
		f"</div>"
	)

	variable_html: str = ''
	if note:
		variable_html = f"<p class='note'>{note}<p>"
	if h1:
		variable_html = variable_html + f"<h1>{h1}</h1>"
	if subtitle:
		variable_html = variable_html + f"<p class='subtitle'>{subtitle}</p>"
	variable_html = variable_html + "</div>"

	return init_html + variable_html


def pop_up_button(text: str = 'Aprender más') -> str:
	return (
		f"<head>"
		f"<link rel='stylesheet'"
		f"href='https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0' />"
		# Start styles container
		f"<style>.container"
		f"{{text-align: left;}}"
		f"</style>"
		# Start styles button
		f"<style>.button-modal"
		f"{{appearance: none;"
		f"background: var(--color-primary);"
		f"border-radius: var(--border-radius-m);"
		f"color: white;"
		f"cursor: pointer;"
		f"display: inline-block;"
		f"font-size: 14px;"
		f"font-weight:400;"
		f"height: 3em;"
		f"line-height: 3em;"
		f"padding: 0.5em 2em;}}"
		f".button-modal:hover{{background-color: var(--color-primary-dark); transition:0.2s;}}"
		f"</style>"
		# Start styles modal
		f"<style>.details-modal"
		f"{{background: var(--color-white);"
		f"border-radius: 24px;"
		f"padding: 32px;"
		f"z-index:9999;"
		f"box-shadow: var(--box-shadow-xl);"
		f"top: 50%;"
		f"left: 50%;"
		f"pointer-events: none;"
		f"position: fixed;"
		f"transform: translate(-50%, -50%);"
		f"width: 60%;"
		f"text-align: left;"
		f"max-height: 70vh;"
		f"display: flex;"
		f"flex-direction: column;}}"
		f"</style>"
		# Start styles modal close
		f"<style>.details-modal-close"
		f"{{align-items: center;"
		f"color: #111827;"
		f"display: flex;"
		f"height: 2.5em;"
		f"padding:16px;"
		f"justify-content: center;"
		f"cursor: pointer;"
		f"pointer-events: none;"
		f"position: absolute;"
		f"right: 0;"
		f"top: 0;"
		f"width: 2.5em;}}"
		f".details-modal-close:hover {{background-color: var(--color-grey-300); opacity: 0.7;}}"
		f"</style>"
		# Start styles modal content
		f"<style>.details-modal-content"
		f"{{pointer-events: all;"
		f"overflow: auto;}}"
		f"</style>"
		# Start styles modal overlay
		f"<style>.details-modal-overlay"
		f"{{transition: opacity 0.2s ease-out;"
		f"pointer-events: none;"
		f"background:#0f172a;"
		f"z-index:99;"
		f"position: fixed;"
		f"opacity: 0;"
		f"bottom: 0; right: 0; left: 0; top: 0;}}"
		f"details[open] .details-modal-overlay {{pointer-events: all;opacity: 0.5; z-index: 9999;}}"
		f"</style>"
		# Start styles details generals
		f"<style>details summary {{"
		f"list-style: none;}}"
		f"details summary:focus {{"
		f"outline: none;}}"
		f"details summary::-webkit-details-marker {{"
		f"display: none;}}"
		f"</style>"
		f"</head>"
		f"<div class='container'>"
		f"<details>"
		f"<summary>"
		f"<div class='button-modal'>"
		f"{text}"
		"</div>"
		"<div class='details-modal-overlay'></div>"
		"</summary>"
		"<div class='details-modal'>"
		"<div class='details-modal-close'>"
		"<span class='material-symbols-rounded'>close</span>"
		"</div>"
		"<div class='details-modal-title'>"
		"<h5>This is a modal information</h5>"
		"</div>"
		"<div class='details-modal-content'>"
		"<p class='base'>"
		"You can click the X in the corner or click the overlay to close this modal."
		"Something like this could be useful as a nice way to show additional information,"
		"but that's about as far as I would take it. It's just a nice way of styling the details element."
		"</p>"
		"</div>"
		"</div>"
		"</details>"
		"</div>"
	)


def accordion_button(
		main_text: str = 'Más información',
		internal_text: str = 'Lorem fistrum te voy a borrar el cerito pecador a gramenawer diodeno papaar papaar por'
) -> str:
	return (
		f"<head>"
		f"<link rel='stylesheet'"
		f"href='https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0' />"
		# Start styles container
		f"<style>"
		f"input[type=checkbox] {{display: none;}}"
		f"</style>"
		f"<style>"
		f".wrap-collapsible {{width:100%; height:auto;}}"
		f"</style>"
		f"<style>"
		f".lbl-toggle {{"
		f"display: block;"
		f"font-weight: bold;"
		f"font-size: 1.2rem;"
		f"text-transform: none;"
		f"text-align: left;"
		f"padding: 16px;"
		"color: var(--color-white);"
		f"background: var(--chart-C1);"
		f"cursor: pointer;"
		f"border-radius: var(--border-radius-m);"
		f"transition: all 0.25s ease-out;}}"
		f".lbl-toggle:hover {{"
		f"color: #fff;}}"
		f".lbl-toggle::before {{"
		f"content: url(https://uploads-ssl.webflow.com/619f9fe98661d321dc3beec7/62d6e16e1d9d7444dfb3826e_chevron-down-white.svg);"
		f"display: inline-block;"
		f"width:24px;"
		f"height:24px;"
		f"vertical-align: middle;"
		f"margin-right: 16px;"
		f"transition: transform 0.2s ease-out;}}"
		f".toggle:checked + .lbl-toggle::before {{"
		f"transform: rotate(180deg);}}"
		f"</style>"
		f"<style>"
		f".collapsible-content {{"
		f"max-height: 0px;"
		f"overflow: hidden;"
		f"transition: max-height 0.25s ease-in-out;"
		f"</style>"
		f"<style>"
		f".toggle:checked + .lbl-toggle + .collapsible-content {{max-height: 350px;}}"
		f".toggle:checked + .lbl-toggle {{"
		f"border-bottom-right-radius: 0;"
		f"border-bottom-left-radius: 0;}}"
		f"</style>"
		f"<style>"
		f".collapsible-content .content-inner {{"
		f"background: var(--color-grey-100);"
		f"padding: 16px;"
		f"border-radius: 0px 0px 16px 16px;}}"
		f"</style>"
		f"<style>"
		f".collapsible-content p {{margin-bottom: 0;}}"
		f"</style>"
		f"</head>"
		f"<div class='wrap-collapsible'>"
		f"<input id='collapsible' class='toggle' type='checkbox'>"
		f"<label for='collapsible' class='lbl-toggle'>{main_text}</label>"
		f"<div class='collapsible-content'>"
		f"<div class='content-inner'>"
		f"<p class='base'>{internal_text}</p>"
		f"</div>"
		f"</div>"
		f"</div>"
	)
