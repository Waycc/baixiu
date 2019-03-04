<template>
    <div class="main">
        <nav class="navbar">
            <button class="btn btn-default navbar-btn fa fa-bars"></button>
            <ul class="nav navbar-nav navbar-right">
                <li>
                    <a href>
                        <i class="fa fa-user"></i>个人中心
                    </a>
                </li>
                <li>
                    <a href="#">
                        <i class="fa fa-sign-out"></i>退出
                    </a>
                </li>
            </ul>
        </nav>

        <router-view class="main"></router-view>
        <my-aside></my-aside>

    </div>
</template>

<script>
    import myAside from "./components/aside"
    import reqHandler from './modules/index'

    export default {
        name: 'index2',
        components: {myAside},
        mounted(){
            let userInfo;
            reqHandler.getUser({userId: 1}).then(res => {
                if (!res.data.status){
                    alert(res.data.message);
                    return
                }
                userInfo = res.data.data;
                console.log(userInfo);
                this.$store.commit('changeUserInfo', userInfo);
            });

        }

    };
</script>

<style scoped>

</style>
