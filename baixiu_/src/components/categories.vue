<template>

    <div>
        <div class="container-fluid">
            <div class="page-title">
                <h1>分类目录</h1>
            </div>
            <!-- 有错误信息时展示 -->
            <!-- <div class="alert alert-danger">
              <strong>错误！</strong>发生XXX错误
            </div> -->
            <div class="row">
                <div class="col-md-4">
                    <form>
                        <h2>添加新分类目录</h2>
                        <div class="form-group">
                            <label for="name">名称</label>
                            <input id="name" v-model="categoriesName" class="form-control" name="name" type="text"
                                   placeholder="分类名称">
                        </div>
                        <div class="form-group">
                            <label for="slug">描述</label>
                            <input id="slug" class="form-control" v-model="categoriesDes" name="slug" type="text"
                                   placeholder="描述">
                        </div>
                        <div class="form-group">
                            <button class="btn btn-primary" type="submit" @click.prevent="addCategory">添加</button>
                        </div>
                    </form>
                </div>
                <div class="col-md-8">
                    <div class="page-action">
                        <!-- show when multiple checked -->
                        <a class="btn btn-danger btn-sm" href="javascript:;" style="">批量删除</a>
                    </div>
                    <table class="table table-striped table-bordered table-hover">
                        <thead>
                        <tr>
                            <th class="text-center" width="40">
                                <input :checked="categoriesList.length === categoriesIds.length && categoriesIds.length"
                                       type="checkbox"
                                       @click="checkAll"
                                >
                            </th>
                            <th>名称</th>
                            <th>描述</th>
                            <th class="text-center" width="100">操作</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="category in categoriesList" :key="category.id">
                            <td class="text-center">
                                <input :checked="categoriesIds.includes(category.id)"
                                       type="checkbox"
                                       @click.stop="handleCheck(category.id)"
                                >
                            </td>
                            <td>{{ category.name }}</td>
                            <td>{{ category.des }}</td>
                            <td class="text-center">
                                <a href="javascript:;" class="btn btn-info btn-xs">编辑</a>
                                <a href="javascript:;" class="btn btn-danger btn-xs">删除</a>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
    import reqHandler from '../modules/index'

    export default {
        name: "categories",
        data: function () {
            return {
                categoriesName: "",
                categoriesDes: "",
                categoriesList: [],
                categoriesIds: [],
            }
        },
        created: function () {
            reqHandler.getCategory().then(res => {
                if (!res.data.status) {
                    alert(res.data.message || '获取类别失败')
                    return
                }
                this.categoriesList = res.data.data
            })
        },
        methods: {
            addCategory() {
                reqHandler.addCategory(this.paramsObj).then(res => {
                    if (!res.data.status){
                        alert('添加失败')
                        return
                    }
                    alert('添加成功')
                    this.$router.go(0)
                })
            },
            handleCheck(categoryId) {
                let index = this.categoriesIds.indexOf(categoryId);
                if (index >= 0) {
                    this.categoriesIds.splice(index, 1)
                } else {
                    this.categoriesIds.push(categoryId)
                }
            },
            checkAll(){
                if (this.categoriesList.length === this.categoriesIds.length){
                    this.categoriesIds = []
                    return
                }
                this.categoriesList.map(item => {
                    if (!this.categoriesIds.includes(item.id)){
                        this.categoriesIds.push(item.id)
                    }
                })
            }
        },
        computed: {
            paramsObj() {
                return {
                    name: this.categoriesName,
                    des: this.categoriesDes
                }
            }
        }
    }
</script>

<style scoped>

</style>