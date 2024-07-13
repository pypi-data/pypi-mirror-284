## -*- coding: utf-8; -*-

<%def name="app_title()">${app.get_title()}</%def>

<%def name="global_title()">${self.app_title()}</%def>

<%def name="extra_styles()"></%def>

<%def name="favicon()">
  ## <link rel="icon" type="image/x-icon" href="${config.get('tailbone', 'favicon_url', default=request.static_url('wuttaweb:static/img/favicon.ico'))}" />
</%def>

<%def name="header_logo()">
  ## ${h.image(config.get('wuttaweb.header_image_url', default=request.static_url('wuttaweb:static/img/logo.png')), "Header Logo", style="height: 49px;")}
</%def>

<%def name="footer()">
  <p class="has-text-centered">
    powered by ${h.link_to("Wutta Framework", 'https://pypi.org/project/WuttJamaican/', target='_blank')}
  </p>
</%def>
