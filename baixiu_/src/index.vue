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
    import myAside from "./components/aside.vue"

    export default {
        name: 'index2',
        components: {myAside},

    };
</script>

<style scoped>

</style>
