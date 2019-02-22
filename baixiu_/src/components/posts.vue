<template>
<div >
    <div class="container-fluid">
        <div class="page-title">
            <h1>所有文章</h1>
            <a href="post-add.html" class="btn btn-primary btn-xs">写文章</a>
        </div>
        <!-- 有错误信息时展示 -->
        <!-- <div class="alert alert-danger">
          <strong>错误！</strong>发生XXX错误
        </div> -->
        <div class="page-action">
            <!-- show when multiple checked -->
            <a class="btn btn-danger btn-sm" href="javascript:;" style="display: none">批量删除</a>
            <form class="form-inline">
                <select v-model="postCategory" name="" class="form-control input-sm">
                    <option value="all">所有分类</option>
                    <option value="1">未分类</option>
                </select>
                <select v-model="postStatus" name="" class="form-control input-sm">
                    <option value="all">所有状态</option>
                    <option value="drafted">草稿</option>
                    <option value="published">已发布</option>
                </select>
                <button class="btn btn-default btn-sm" @click.prevent="postFilter">筛选</button>
            </form>
            <ul class="pagination pagination-sm pull-right">
                <li><a href="#">上一页</a></li>
                <li><a href="#">1</a></li>
                <li><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">下一页</a></li>
            </ul>
        </div>
        <table class="table table-striped table-bordered table-hover">
            <thead>
            <tr>
                <th class="text-center" width="40"><input type="checkbox"></th>
                <th>标题</th>
                <th>作者</th>
                <th>分类</th>
                <th class="text-center">发表时间</th>
                <th class="text-center">状态</th>
                <th class="text-center" width="100">操作</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="post in postList" :key="post.id">
                <td class="text-center"><input type="checkbox"></td>
                <td>{{ post.title }}</td>
                <td>{{ post.author }}</td>
                <td>{{ post.category }}</td>
                <td class="text-center">{{ post.create }}</td>
                <td class="text-center">{{ post.actived?'已发布': '审核'}}</td>
                <td class="text-center">
                    <a href="javascript:;" class="btn btn-default btn-xs">编辑</a>
                    <a href="javascript:;" class="btn btn-danger btn-xs">删除</a>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</div>


</template>

<script>
    export default {
        name: "profile",
        data: function () {
            return {
                postList:[],
                postCategory:"all",
                postStatus: "all",
            }
        },
        methods:{
            postFilter(){
                console.log(this.postCategory)
                console.log(this.postStatus)
            },
        }
    }
</script>

<style scoped>

</style>