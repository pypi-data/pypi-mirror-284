## -*- coding: utf-8; -*-
<%inherit file="/page.mako" />
<%namespace name="base_meta" file="/base_meta.mako" />

<%def name="title()">Home</%def>

<%def name="render_this_page()">
  ${self.page_content()}
</%def>

<%def name="page_content()">
  <div style="height: 100%; display: flex; align-items: center; justify-content: center;">
    <div class="logo">
      ## ${h.image(image_url, "{} logo".format(capture(base_meta.app_title)))}
      <h1 class="is-size-1">Welcome to ${base_meta.app_title()}</h1>
    </div>
  </div>
</%def>


${parent.body()}
