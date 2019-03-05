import axios from 'axios'

let instance = axios.create({
    baseURL: "http://94.191.27.38:8000/",
    headers: {
    "Content-Type": "application/json;charset=UTF-8",
  },
    // withCredentials: true
});

let formInstance = axios.create({
    baseURL: "http://94.191.27.38:8000/",
    headers: {
    "Content-Type": "application/x-www-form-urlencoded",
  },
    // withCredentials: true
});
// var params = new URLSearchParams();
// params.append('userName', 111);
// params.append('phone', 222);

let getFormParams = function (params) {
    let param = new URLSearchParams()
    Object.keys(params).forEach(key => {
        param.append(key, params[key])
    })
    return param
}
export default {
    // 获取文章
    getPost(params) {return instance.get('admin/post/list', {params:params})},
    // 添加新文章
    addPost(params) {return instance.post('admin/post/add', JSON.stringify(params))},
    // 修改文章
    updatePost(params) {return instance.post('admin/post/update', JSON.stringify(params))},
    //删除文章
    deletePost(params) {
        let param = getFormParams(params)
        return formInstance.post('admin/post/delete', param)
    },
    // 批量删除文章
    batchDeletePost(params) {
        let param = getFormParams(params)
        return formInstance.post('admin/post/batchDelete', param)
    },
    // 获取当前登录用户
    getUser(params) {return instance.get('account/user', {params: params})},
    // 添加用户
    addUser(params) {return instance.post('account/user/add', JSON.stringify(params))},
    // 获取类别
    getCategory(params) {return instance.get('admin/category/list', {params:params})},
    // 添加类别
    addCategory(params) { return instance.post('admin/category/add', JSON.stringify(params))},
    //删除类别
    deleteCategory(params) {
        let param = getFormParams(params)
        return formInstance.post('admin/category/delete', param)
    },
    // 批量删除类别
    batchDeleteCategory(params) {
        let param = getFormParams(params)
        return formInstance.post('admin/category/batchDelete', param)
    },
}