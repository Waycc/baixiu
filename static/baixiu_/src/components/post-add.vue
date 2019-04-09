<template>


    <div>
        <div class="container-fluid">
            <div class="page-title">
                <h1>写文章</h1>
            </div>
            <!-- 有错误信息时展示 -->
            <!-- <div class="alert alert-danger">
              <strong>错误！</strong>发生XXX错误
            </div> -->
            <form class="row">
                <div class="col-md-9" style="position: relative">
                    <div class="form-group">
                        <label for="title">标题</label>
                        <input id="title" class="form-control" v-model="postTitle"
                               name="title" type="text" placeholder="文章标题">
                    </div>
                    <div class="form-group">
                        <vue-editor :content="content" @sendParent="changeContent"></vue-editor>
                    </div>
                    <div class="form-group">
                        <button class="btn btn-primary" id="article-save" @click.prevent="savePost">保存</button>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="form-group">
                        <label for="category">所属分类</label>
                        <select id="category" class="form-control" name="category" v-model="postCategory">
                            <option value=0>未分类</option>
                            <option v-for="category in categoriesList" :key="category.id" :value="category.id">{{category.name}}</option>
                        </select>
                    </div>
                    <!--<div class="form-group">-->
                    <!--<label for="created">发布时间</label>-->
                    <!--<input id="publish-date" class="form-control" name="created" type="test">-->
                    <!--</div>-->
                    <div class="form-group">
                        <label for="status">状态</label>
                        <select id="status" class="form-control" name="status" v-model="postStatus">
                            <option value="drafted">草稿</option>
                            <option value="published">发布</option>
                        </select>
                    </div>
                </div>
            </form>

        </div>

    </div>

</template>

<script>
    import vueEditor from './vue-editor'
    import reqHandler from '@/modules/index'

    let cvm = {
        name: 'postAdd',
        components: {
            vueEditor
        },
        data: function () {
            return {
                content: '',
                postTitle: '',
                postCategory: 0,
                postStatus: 'drafted',
                categoriesList: [],
                postId: '',

            }
        },
        computed: {
            paramsObj() {
                return {
                    postId: this.postId,
                    content: this.content,
                    title: this.postTitle,
                    category_id: this.postCategory,
                    status: this.postStatus,
                    author_id: this.$store.state.userInfo.id,
                    tags: '',
                    views: '',

                }
            }
        },
        methods: {
            savePost(event) {
                console.log(this.paramsObj)
                switch (true) {
                    case (!this.postTitle): {
                        alert('标题不能为空')
                        return
                    }
                    case (!this.content): {
                        alert('内容不能为空')
                        return
                    }
                }
                if (this.postId){
                    reqHandler.updatePost(this.paramsObj).then(res => {
                        if (res.data.status){
                            alert('修改文章成功')
                            this.$router.go(0)
                        }
                    })
                    return
                }

                reqHandler.addPost(this.paramsObj).then(res => {
                    if (res.data.status) {
                        alert('添加文章成功')
                        this.$router.go(0)
                    } else {
                        alert(res.data.message || '添加文章失败')
                    }
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
            changeContent(val) {
                this.content = val
            }
        },
        created() {
            this.getCategory()
        },
        beforeRouteEnter(to, from, next){
            if (to.params.postId){
                reqHandler.getPost({postId: to.params.postId}).then(res => {
                    let data = res.data
                    if (data.status){
                        next(vm => {
                            console.log(data.data.title)
                            vm.postId = data.data.id
                            vm.content = data.data.content
                            vm.postTitle = data.data.title
                            vm.postStatus = data.data.status
                            vm.postCategory = data.data.category_id || 0
                        })
                    }
                })
                return
            }
            next()
        }
    };
    export default cvm

</script>

<style scoped>
    #article-save {
        position: absolute;
        bottom: 16px;
        right: -72px;
    }

    .container-fluid {
        position: relative;
    }
</style>