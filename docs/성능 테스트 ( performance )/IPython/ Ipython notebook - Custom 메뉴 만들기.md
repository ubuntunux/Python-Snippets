> [Python Snippets](../../README.md) / [성능 테스트 ( performance )](../README.md) / [IPython](README.md) /  Ipython notebook - Custom 메뉴 만들기.md
##  Ipython notebook - Custom 메뉴 만들기
```
custom.js 파일을 열고 아래의 코드를 붙여넣는다. (경로 : C:\Users\Taeromi\.ipython\profile_default\static\custom\custom.js)

%%file C:\Users\Taeromi\.ipython\profile_default\static\custom\custom.js
    
// leave at least 2 line with only a star on it below, or doc generation fails
/**
 *
 *
 * Placeholder for custom user javascript
 * mainly to be overridden in profile/static/custom/custom.js
 * This will always be an empty file in IPython
 *
 * User could add any javascript in the `profile/static/custom/custom.js` file
 * (and should create it if it does not exist).
 * It will be executed by the ipython notebook at load time.
 *
 * Same thing with `profile/static/custom/custom.css` to inject custom css into the notebook.
 *
 * Example :
 *
 * Create a custom button in toolbar that execute `%qtconsole` in kernel
 * and hence open a qtconsole attached to the same kernel as the current notebook
 *
 *    $([IPython.events]).on('app_initialized.NotebookApp', function(){
 *        IPython.toolbar.add_buttons_group([
 *            {
 *                 'label'   : 'run qtconsole',
 *                 'icon'    : 'icon-terminal', // select your icon from http://fortawesome.github.io/Font-Awesome/icons
 *                 'callback': function () {
 *                     IPython.notebook.kernel.execute('%qtconsole')
 *                 }
 *            }
 *            // add more button here if needed.
 *            ]);
 *    });
 *
 * Example :
 *
 *  Use `jQuery.getScript(url [, success(script, textStatus, jqXHR)] );`
 *  to load custom script into the notebook.
 *
 *    // to load the metadata ui extension example.
 *    $.getScript('/static/notebook/js/celltoolbarpresets/example.js');
 *    // or
 *    // to load the metadata ui extension to control slideshow mode / reveal js for nbconvert
 *    $.getScript('/static/notebook/js/celltoolbarpresets/slideshow.js');
 *
 *
 * @module IPython
 * @namespace IPython
 * @class customjs
 * @static
 */
            
// Toggle Input 버튼
$([IPython.events]).on('notebook_loaded.Notebook', function(){
    IPython.toolbar.add_buttons_group([
        {
             'label'   : 'toggle input cells',
             'icon'    : 'icon-refresh', 
             'callback': function(){$('.input').slideToggle()}
        }
    ]);
});

// qtconsole을 실행시키는 스크립트
$([IPython.events]).on('app_initialized.NotebookApp', function(){
     IPython.toolbar.add_buttons_group([
         {
              'label'   : 'run qtconsole',
              'icon'    : 'icon-terminal', // select your icon from http://fortawesome.github.io/Font-Awesome/icons
              'callback': function () {
                  IPython.notebook.kernel.execute('%qtconsole')
              }
         }
         // add more button here if needed.
         ]);
 });

// Line number 출력하기
IPython.Cell.options_default.cm_config.lineNumbers = true;
```