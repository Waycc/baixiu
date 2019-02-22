<template>
    <div class="my-aside">
        <div class="profile">
            <img class="avatar" src="/src/static/uploads/avatar.jpg" id="user-icon" title="头像">
            <h3 class="name" id="user-name">布头儿</h3>
        </div>

        <el-collapse v-model="activeNames" class="my-nav">
            <router-link to="/index" class="el-collapse-item__header">
                <span>仪表盘</span>
            </router-link>
            <el-collapse-item title="文章" name="1">
                <ul id="menu-posts">
                    <li>
                        <router-link to="/posts"><span>所有文章</span></router-link>
                    </li>
                    <li>
                        <router-link to="/post-add"><span>写文章</span></router-link>
                    </li>
                    <li>
                        <router-link to="/categories">分类目录</router-link>
                    </li>
                </ul>
            </el-collapse-item>
            <router-link to="/comments" class="el-collapse-item__header">
                <span>评论</span>
            </router-link>
            <router-link to="/users" class="el-collapse-item__header">
                <span>用户</span>
            </router-link>
            <el-collapse-item title="设置" name="2">
                <ul id="menu-settings">
                    <li>
                        <router-link to="/nav-menus">导航菜单</router-link>
                    </li>
                    <li>
                        <router-link to="/slides">图片轮播</router-link>
                    </li>
                    <li>
                        <router-link to="/settings">网站设置</router-link>
                    </li>
                </ul>
            </el-collapse-item>
        </el-collapse>
    </div>
</template>

<script>
    export default {
        name: "myAside",
        data: function () {
            return {
                currentPath: '',
                postTabs: ['menu-posts', 'posts', 'post-add', 'categories'],
                settingTabs: ['nav-menus', 'slides', 'settings'],
                commentTabs: ['comments'],
                userTabs: ['users'],
                indexTabs: ['index'],
                activeNames: [],
            };
        },
        methods: {
            initTab() {
                this.currentPath = this.$route.path.replace('/', '');
                switch (true) {
                    case (this.postTabs.includes(this.currentPath)): {
                        this.activeNames.push('1')
                    }break;
                    case (this.settingTabs.includes(this.currentPath)): {
                        this.activeNames.push('2')
                    }break;
                    default: {
                        console.log(2222222)
                    }
                }
            },
        },
        created() {
            this.initTab()
        },
        watch: {
            '$route': 'initTab'
        }
    }
</script>

<style lang="scss">
    .my-aside {
        position: fixed;
        top: 0;
        left: 0;

        width: 180px;
        height: 100%;

        background-color: #2f4050;

        .el-collapse {
            border-top: none;
            border-bottom: none;
        }

        .el-collapse-item__header {
            margin-top: 1px;
            padding: 10px 20px;
            color: #a9b0c2;
            text-decoration: none;
            background-color: #2f4050;
            display: -webkit-box;
            display: -ms-flexbox;
            display: flex;
            -webkit-box-align: center;
            -ms-flex-align: center;
            align-items: center;
            height: 48px;
            line-height: 30px;
            cursor: pointer;
            border-bottom: none;
            font-size: 13px;
            font-weight: 500;
            -webkit-transition: border-bottom-color .3s;
            transition: border-bottom-color .3s;
            outline: 0;

            &.is-active,
            &:hover{
                color: #f6f6f6;
                background-color: #213140;
            }
        }


        .el-cascader-menu,
        .el-cascader-menu__item.is-disabled:hover,
        .el-collapse-item__header,
        .el-collapse-item__wrap {
            background-color: #2f4050;
            color: #a9b0c2;
            border-bottom: none;
        }

        .el-collapse-item__content {
            color: #a9b0c2;
            overflow: hidden;
            padding: 0;
            list-style: none;
            background-color: #243443;
            box-shadow: inset 0 1px 3px #111e29;
            font-size: .9em;

            ul {
                li{
                    &:first-child{
                        margin-top: 10px;
                    }
                    &:last-child{
                        margin-bottom: 10px;
                    }
                }

            }
        }

        .profile {
            padding: 25px;
            text-align: center;
            background-color: #243443;

            .avatar {
                width: 80px;
                height: 80px;
                border: 3px solid rgba(255, 255, 255, .3);
                border-radius: 50%;
                object-fit: cover;
                margin: 0 auto;
            }

            .name {
                color: #a9b0c2;
                font-size: 16px;
            }
        }

        .my-nav {
            li + li {
                margin-top: 1px;
            }

            a {
                display: block;
                padding: 10px 20px;
                color: #a9b0c2;
                text-decoration: none;

                &.active,
                &.router-link-active,
                &:hover {
                    color: #f6f6f6;
                    background-color: #213140;
                }
            }

        }
    }
</style>