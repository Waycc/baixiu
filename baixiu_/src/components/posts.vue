<template>
    <div>
        <div class="container-fluid">
            <div class="page-title">
                <h1>所有文章</h1>
                <router-link to="/post-add" class="btn btn-primary btn-xs">写文章</router-link>
            </div>
            <!-- 有错误信息时展示 -->
            <!-- <div class="alert alert-danger">
              <strong>错误！</strong>发生XXX错误
            </div> -->
            <div class="page-action">
                <!-- show when multiple checked -->
                <a class="btn btn-danger btn-sm" href="javascript:;" @click="batchDelete">批量删除</a>
                <form class="form-inline">
                    <select v-model="postCategory" name="" class="form-control input-sm">
                        <option value="all">所有分类</option>
                        <option v-for="category in categoriesList" :key="category.id" :value="category.id">{{category.name}}</option>
                    </select>
                    <select v-model="postStatus" name="" class="form-control input-sm">
                        <option value="all">所有状态</option>
                        <option value="drafted">草稿</option>
                        <option value="published">已发布</option>
                    </select>
                    <button class="btn btn-default btn-sm" @click.prevent="postFilter">筛选</button>
                </form>

                <!-- 分页 -->
                <el-pagination
                        class="pull-right"
                        background
                        layout="prev, pager, next, sizes"
                        :page-sizes="[1, 20, 50, 100, 150]"
                        :page-size="pageSize"
                        :total="postTotal"
                        @size-change="sizeChange"
                        @current-change="currentPageChange"
                >
                </el-pagination>
            </div>
            <table class="table table-striped table-bordered table-hover">
                <thead>
                <tr>
                    <th class="text-center" width="40">
                        <input :checked="postList.length === postIds.length && postIds.length"
                               type="checkbox"
                               @click="checkAll"
                        >
                    </th>
                    <th>标题</th>
                    <!--<th>作者</th>-->
                    <th>分类</th>
                    <th class="text-center">发表时间</th>
                    <th class="text-center">状态</th>
                    <th class="text-center" width="100">操作</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="post in postList" :key="post.id">
                    <td class="text-center">
                        <input :checked="postIds.includes(post.id)"
                               type="checkbox"
                               @click.stop="handleCheck(post.id)"
                        >
                    </td>
                    <td>{{ post.title }}</td>
                    <!--<td>{{ post.author && post.author.alias }}</td>-->
                    <td>{{ post.category && post.category.name || '未分类'}}</td>
                    <td class="text-center">{{ post.created }}</td>
                    <td class="text-center">{{ statusMap[post.status]}}</td>
                    <td class="text-center">
                        <a href="javascript:;" class="btn btn-info btn-xs" @click="updatePost(post.id)">编辑</a>
                        <a href="javascript:;" class="btn btn-danger btn-xs" @click.stop="deletePost(post.id)">删除</a>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>


</template>

<script>
    import reqHandler from '@/modules/index'

    export default {
        name: "profile",
        data: function () {
            return {
                postList: [],
                statusMap: {
                    published: '已发布',
                    drafted: '草稿'
                },
                postCategory: "all",
                postStatus: "all",
                postIds: [],
                currentPage:1,
                pageSize: 20,
                postTotal:0,
                categoriesList: [],
            }
        },
        computed:{
            postListParams(){
                return {
                    page: this.currentPage,
                    pageSize: this.pageSize,
                    category_id: this.postCategory,
                    status: this.postStatus,
                }
            }
        },
        methods: {
            updatePost(postId){
                this.$router.push({
                    name: 'postAdd',
                    params: {
                        postId: postId
                    }
                })
            },
            postFilter() {
                this.getPost()
                this.postIds = []
            },
            checkAll() {
                if (this.postList.length === this.postIds.length) {
                    this.postIds = []
                    return
                }
                this.postList.map(item => {
                    if (!this.postIds.includes(item.id)) {
                        this.postIds.push(item.id)
                    }
                })
            },
            handleCheck(postId) {
                let index = this.postIds.indexOf(postId);
                if (index >= 0) {
                    this.postIds.splice(index, 1)
                } else {
                    this.postIds.push(postId)
                }
            },
            sizeChange(val){
                this.pageSize = val
                this.getPost()
            },
            currentPageChange(val){
                this.currentPage = val
                this.getPost()
            },
            getPost(){
                return reqHandler.getPost(this.postListParams).then(res => {
                    this.postList = res.data.data
                    this.postTotal = res.data.count
                })
            },
            getCategory() {
                reqHandler.getCategory().then(res => {
                    if (!res.data.status) {
                        alert(res.data.message || '获取类别失败')
                        return
                    }
                    this.categoriesList = res.data.data
                })
            },
            deletePost(postId){
                let isDelete = confirm("是否删除")
                if (!isDelete) return
                reqHandler.deletePost({postId: postId}).then(res => {
                    if (res.data.status){
                        alert('删除成功')
                        this.getPost()
                    }
                })
            },
            batchDelete(){
                if (this.postIds.length === 0){
                    alert('请先选择删除项')
                    return
                }
                let isDelete = confirm('是否批量删除已选中项？')
                if (!isDelete) return
                reqHandler.batchDeletePost({postIds: this.postIds}).then(res => {
                    alert('批量删除成功')
                    this.getPost()
                })
                console.log(this.postIds)
            }
        },
        created() {
            this.getPost()
            this.getCategory()
        }
    }
</script>

<style scoped>

</style>