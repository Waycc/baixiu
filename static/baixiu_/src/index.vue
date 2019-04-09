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
                    <a href="/adminLogout">
                        <i class="fa fa-sign-out"></i>退出
                    </a>
                </li>
            </ul>
        </nav>

        <transition name="slide-fade">
            <router-view class="main"></router-view>
        </transition>
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
.slide-fade{
  position: absolute;
    /*left:0;right: 0;*/
}
.slide-fade-enter-active {
  transition: all 1.2s ease;
}
.slide-fade-leave-active {

  transition: all .1s cubic-bezier(2.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
{
  /*left:0;right: 0;*/
  transform: translateX(50px);
  opacity: 0;
}
</style>
