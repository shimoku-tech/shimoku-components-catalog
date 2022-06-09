"""HTML beautiful components"""


def create_h1_title(title: str) -> str:
	html = (
	    "<head>"
	    "<style>.title{height:100%; width:100%; border-radius:16px; padding:16px; background-color:#FAFAFB; color:#4C72F9;}</style>"
	    "<style>.base{color:#202A36;}</style>"
	    "</head>"
	    "<div class='title'>"
	    "<h1>Real-time</h1>"
	    "<p class='base'>"
	    "Users"
	    "</p>"
	    "</div>"
	)

	return (
	    f"<div class='title'>"
	    f"<h1>Summary</h1>"
	    f"<p class='base'>"
	    f"{title}"
	    f"</p>"
	    f"</div>"
	)


def beautiful_indicator(title: str, background_url: Optional[str] = None) -> str:
	if not background_url:
		background_url = 'https://uploads-ssl.webflow.com/619f9fe98661d321dc3beec7/62a07a6d9e984908a5aca6a1_shim-anomaly-bg-s.jpg'
	return (
	    f"<head>"
	    f"<style>.anomaly{height:121px; width:100%; border-radius:8px; padding:45px; background-position: center; background-size: cover; background-image: url({background_url}); color:#FFFFFF;}</style>"
	    f"</head>"
	    f"<a href='https://develop.shimoku.io/big-bang'>"
	    f"<div class='anomaly'>"
	    f"<h3>"
	    f"{title}"
	    f"</h3>"
	    f"</div>"
	    f"</a>"

	)


def button_click_to_new_tab(title: str, background_url: str, link_url: Optional[str] = None) -> str:
	if not link_url:
		link_url = background_url
	return (
	    f"<head>"
	    f"<style>.pug{height:180px; width:100%; border-radius:8px; padding:24px; background-position: center; background-size: cover; background-image: url({background_url}); color:#FFFFFF;}</style>"
	    f"<style>.crea{font-size:24px; color:#FFFFFF; font-weight: 400;}</style>"
	    f"</head>"
	    f"<a href={link_url} target='_blank'>"
	    f"<div class='pug'>"
	    f"<p class='crea'>"
	    f"{title}"
	    f"</p>"
	    f"</div>"
	    f"</a>"

	)

