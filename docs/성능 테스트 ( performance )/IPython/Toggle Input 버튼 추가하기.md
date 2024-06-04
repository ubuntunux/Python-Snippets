[CONTENTS](README.md)
## Toggle Input 버튼 추가하기
    custom.js 파일을 열고 아래의 코드를 붙여넣는다. (경로 : C:\Users\Taeromi\.ipython\profile_default\static\custom\custom.js) 
    
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