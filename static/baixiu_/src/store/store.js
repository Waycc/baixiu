import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const state = {
    userInfo: {}
};

const mutations = {
    changeUserInfo(state, userInfo){
        state.userInfo = userInfo
    }
};

export default new Vuex.Store({
    state,
    mutations
})

