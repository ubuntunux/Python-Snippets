[Previous](..)
## Hide Input Code Toggle
방법1

    from IPython.display import display
    from IPython.display import HTML
    import IPython.core.display as di # Example: di.display_html('<h3>%s:</h3>' % str, raw=True)

    # This line will hide code by default when the notebook is exported as HTML
    di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)

    # This line will add a button to toggle visibility of code blocks, for use with the HTML export version
    di.display_html('''<button onclick="jQuery('.input_area').toggle(); jQuery('.prompt').toggle();">Toggle code</button>''', raw=True)


방법 2

    from IPython.display import HTML
    HTML('''<script>
    code_show=true; 
    function code_toggle() {
     if (code_show){
     $('div.input').hide();
     } else {
     $('div.input').show();
     }
     code_show = !code_show
    } 
    $( document ).ready(code_toggle);
    </script>