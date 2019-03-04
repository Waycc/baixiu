<template>
    <div>
        <div class="container-fluid">
            <div class="jumbotron text-center">
                <h1>One Belt, One Road</h1>
                <p>Thoughts, stories and ideas.</p>
                <p>
                    <router-link class="btn btn-primary btn-lg" to="/post-add"
                                 role="button">写文章
                    </router-link>
                </p>
            </div>
            <div class="row">
                <div class="col-md-4">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title">站点内容统计：</h3>
                        </div>
                        <ul class="list-group">
                            <li class="list-group-item"><strong>{{postTotal}}</strong>篇文章（<strong>{{draftedTotal}}</strong>篇草稿）</li>
                            <li class="list-group-item"><strong>{{categoryTotal}}</strong>个分类</li>
                            <li class="list-group-item"><strong>5</strong>条评论（<strong>1</strong>条待审核）</li>
                        </ul>
                    </div>
                </div>
                <div class="col-md-4"></div>
                <div class="col-md-4"></div>
            </div>
        </div>
    </div>
</template>

<script>
    import reqHandler from '@/modules/index'
    export default {
        name: "index",
        data: function () {
            return {
                postData: {},
                categoryData: {},
                commentData: {},
            }
        },
        computed:{
            postTotal(){
                return this.postData.count
            },
            draftedTotal(){
                let result = 0
                this.postData.data.forEach(item => {
                    if (item.status === 'drafted'){
                        result ++
                    }
                })
                return result
            },
            categoryTotal(){
                return this.categoryData.count
            },
            commentTotal(){},
            AuditCommentTotal(){},
        },
        created() {
            reqHandler.getPost().then(res => {
                this.postData = res.data
            })
            reqHandler.getCategory().then(res => {
                this.categoryData = res.data
            })
        }
    }
</script>

<style scoped>

</style>