import axios from 'axios'

let instance = axios.create({
    baseURL: "http://94.191.27.38:8000/",
    headers: {
    "Content-Type": "application/json;charset=UTF-8",
  },
    // withCredentials: true
});
// var params = new URLSearchParams();
// params.append('userName', 111);
// params.append('phone', 222);
export default {
    // 获取文章
    getPost(params) {return instance.get('admin/post/list', {params:params})},
    // 添加新文章
    addPost(params) {return instance.post('admin/post/add', JSON.stringify(params))},
    // 获取当前登录用户
    getUser(params) {return instance.get('account/user', {params: params})},
    // 添加用户
    addUser(params) {return instance.post('account/user/add', JSON.stringify(params))},
    // 获取类别
    getCategory(params) {return instance.get('admin/category/list', {params:params})},
    // 添加类别
    addCategory(params) { return instance.post('admin/category/add', JSON.stringify(params))
    }
}