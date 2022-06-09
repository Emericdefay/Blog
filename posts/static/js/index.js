import jQuery from 'jquery';
import 'bootstrap/dist/css/bootstrap.css';
import '@fortawesome/fontawesome-free/css/all.css';

require('popper.js');
require('bootstrap');
require('mermaid');
require('../scss/styles.scss');


global.jQuery = jQuery;
global.$ = global.jQuery;

import {makeBackground} from './background';
import {makeComments} from './comment';
import {setTheme} from './theme';
import {copyButton} from './copy-button';

window.app = (function app () {
    return {
      models: {},
      collections: {},
      views: {},
      router: null,
      icons: [],
    };
  }(jQuery));
  

window.app.makeBackground = makeBackground;
window.app.setTheme = setTheme;
window.app.makeComments = makeComments;
window.app.copyButton = copyButton;