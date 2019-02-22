import VueRouter from 'vue-router'
import comments from './components/comments.vue'
import categories from './components/categories.vue'
import navMenus from './components/nav-menus.vue'
import postAdd from './components/post-add.vue'
import posts from './components/posts.vue'
import settings from './components/settings.vue'
import index from './components/index.vue'

var router = new VueRouter({
    routes:[
        {'path': '/', redirect: "/index"},
        {'path': '/index', component: index},
        {'path': '/comments', component: comments},
        {'path': '/categories', component: categories},
        {'path': '/nav-menus', component: navMenus},
        {'path': '/post-add', component: postAdd},
        {'path': '/posts', component: posts},
        {'path': '/settings', component: settings},
    ]
})

export default router