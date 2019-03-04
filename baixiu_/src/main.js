import Vue from 'vue'
import app from './index'
import router from './router'
import VueRouter from 'vue-router'
import store from './store/store'
import { Collapse, CollapseItem, Pagination } from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css'
// import 'bootstrap/dist/css/bootstrap.css'
import './static/css/style.css'
import './static/css/admin.css'

//Vue.use(ElementUI)
Vue.use(Collapse);
Vue.use(CollapseItem);
Vue.use(Pagination);
Vue.use(VueRouter);

new Vue({
    el : '#app',
    render: c => c(app),
    router,
    store
});