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
                        <vue-editor v-model="content"></vue-editor>
                    </div>
                    <div class="form-group">
                        <button class="btn btn-primary" id="article-save" @click.prevent="savePost">保存</button>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="form-group">
                        <label for="category">所属分类</label>
                        <select id="category" class="form-control" name="category" v-model="postCategory">
                            <option value="1">未分类</option>
                            <option value="2">潮生活</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="created">发布时间</label>
                        <input id="created" class="form-control" name="created" type="datetime-local">
                    </div>
                    <div class="form-group">
                        <label for="status">状态</label>
                        <select id="status" class="form-control" name="status" v-model="postStatus">
                            <option value="drafted">草稿</option>
                            <option value="published">已发布</option>
                        </select>
                    </div>
                </div>
            </form>

        </div>
    </div>

</template>

<script>
    import vueEditor from './vue-editor.vue'
    let cvm = {
        name: 'postAdd',
        components: {
            vueEditor
        },
        data:function () {
            return {
                content: '',
                postTitle: '',
                postCategory: '1',
                postStatus: 'drafted',

            }
        },
        methods: {
            savePost(event) {
                console.log(this.content)
            },
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