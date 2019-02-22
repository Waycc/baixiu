import Vue from 'vue'
import app from './index.vue'
import router from './router.js'
import VueRouter from 'vue-router'
// import jQuery from 'jquery';
//     window.jQuery = jQuery;
// import 'bootstrap/dist/js/bootstrap.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'bootstrap/dist/css/bootstrap.css'
import './static/css/style.css'
import './static/css/admin.css'
import './static/css/font-awesome/css/font-awesome.css'

Vue.use(ElementUI)
Vue.use(VueRouter)

new Vue({
    el : '#app',
    render: c => c(app),
    router,
})